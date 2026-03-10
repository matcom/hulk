import yaml
import json
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom
import glob

def generate_textmate(grammar, output_path):
    tm_grammar = {
        "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
        "name": grammar["name"],
        "scopeName": grammar["scopeName"],
        "patterns": [],
        "repository": {}
    }

    for key, value in grammar["tokens"].items():
        if "match" in value or "begin" in value:
            tm_grammar["patterns"].append({"include": f"#{key}"})
            tm_grammar["repository"][key] = {
                "name": value.get("name"),
                "match": value.get("match"),
                "begin": value.get("begin"),
                "end": value.get("end"),
                "patterns": value.get("patterns", [])
            }
        else:
            # Nested tokens (like keywords.control)
            for subkey, subvalue in value.items():
                ref = f"{key}_{subkey}"
                tm_grammar["patterns"].append({"include": f"#{ref}"})
                tm_grammar["repository"][ref] = {
                    "name": subvalue.get("name"),
                    "match": subvalue.get("match"),
                    "begin": subvalue.get("begin"),
                    "end": subvalue.get("end"),
                    "patterns": subvalue.get("patterns", [])
                }

    # Clean up None values
    def clean_dict(d):
        if not isinstance(d, dict):
            return d
        return {k: clean_dict(v) for k, v in d.items() if v is not None}

    tm_grammar = clean_dict(tm_grammar)

    with open(output_path, "w") as f:
        json.dump(tm_grammar, f, indent=4)

def generate_markdown_injection(grammar, output_path, lang_id):
    injection = {
        "$schema": "https://raw.githubusercontent.com/martinring/tmlanguage/master/tmlanguage.json",
        "name": f"{grammar['name']} Injection (Markdown/Quarto)",
        "scopeName": f"markdown.{lang_id}.codeblock",
        "injectionSelector": "L:text.html.markdown, L:text.quarto, L:source.quarto, L:source.qmd, L:source.markdown, L:text.markdown, L:text.html.quarto, L:markup.fenced_code.block.quarto",
        "patterns": [
            {
                "name": "markup.fenced_code.block.markdown",
                "begin": f"(^|\\G)(\\s*)(`{{3,}}|~{{3,}})\\s*(?:\\{{\\s*)?(?i:({lang_id}))\\b[^}}]*(\\?}})",
                "beginCaptures": {
                    "3": { "name": "punctuation.definition.markdown" },
                    "4": { "name": "fenced_code.block.language.markdown" },
                    "5": { "name": "punctuation.definition.markdown" }
                },
                "end": "(^|\\G)(\\s*)(\\3)\\s*$",
                "endCaptures": {
                    "3": { "name": "punctuation.definition.markdown" }
                },
                "contentName": grammar["scopeName"],
                "patterns": [
                    { "include": grammar["scopeName"] }
                ]
            }
        ]
    }

    with open(output_path, "w") as f:
        json.dump(injection, f, indent=4)

def generate_kde_xml(grammar, output_path):
    extensions = ";".join([f"*.{ext}" for ext in grammar.get("fileTypes", [])])
    language = ET.Element("language", {
        "name": grammar["name"],
        "section": "Sources",
        "extensions": extensions,
        "version": "1",
        "kateversion": "5.0",
        "author": "Alejandro Piad Morffis",
        "license": "MIT"
    })

    highlighting = ET.SubElement(language, "highlighting")
    contexts = ET.SubElement(highlighting, "contexts")
    main_context = ET.SubElement(contexts, "context", {"name": "Normal Text", "attribute": "dsNormal", "lineEndContext": "#stay"})

    item_datas = ET.SubElement(highlighting, "itemDatas")
    ET.SubElement(item_datas, "itemData", {"name": "dsNormal", "defStyleNum": "dsNormal"})

    added_attributes = set(["dsNormal"])

    def add_to_kde(token_data):
        if "match" in token_data:
            attr = token_data.get("kde_attribute", "dsNormal")
            ET.SubElement(main_context, "RegExpr", {
                "attribute": attr,
                "context": "#stay",
                "String": token_data["match"]
            })
            if attr not in added_attributes:
                ET.SubElement(item_datas, "itemData", {"name": attr, "defStyleNum": attr})
                added_attributes.add(attr)
        elif "begin" in token_data:
            # Simple handling for strings
            attr = token_data.get("kde_attribute", "dsNormal")
            ctx_name = f"ctx_{attr}"
            ET.SubElement(main_context, "DetectChar", {
                "attribute": attr,
                "context": ctx_name,
                "char": token_data["begin"].replace("\\", "")
            })
            if attr not in added_attributes:
                ET.SubElement(item_datas, "itemData", {"name": attr, "defStyleNum": attr})
                added_attributes.add(attr)
            
            # String context
            str_ctx = ET.SubElement(contexts, "context", {"name": ctx_name, "attribute": attr, "lineEndContext": "#pop"})
            ET.SubElement(str_ctx, "DetectChar", {
                "attribute": attr,
                "context": "#pop",
                "char": token_data["end"].replace("\\", "")
            })
            # Escape chars in strings
            for p in token_data.get("patterns", []):
                p_attr = p.get("kde_attribute", "dsSpecialChar")
                ET.SubElement(str_ctx, "RegExpr", {
                    "attribute": p_attr,
                    "context": "#stay",
                    "String": p["match"]
                })
                if p_attr not in added_attributes:
                    ET.SubElement(item_datas, "itemData", {"name": p_attr, "defStyleNum": p_attr})
                    added_attributes.add(p_attr)

    for key, value in grammar["tokens"].items():
        if "match" in value or "begin" in value:
            add_to_kde(value)
        else:
            for subkey, subvalue in value.items():
                add_to_kde(subvalue)

    # Pretty print XML
    xml_str = ET.tostring(language, encoding="utf-8")
    reparsed = minidom.parseString(xml_str)
    with open(output_path, "w") as f:
        f.write(reparsed.toprettyxml(indent="  "))

if __name__ == "__main__":
    os.makedirs("vscode/syntaxes", exist_ok=True)
    
    for yaml_path in glob.glob("syntax/*.yaml"):
        with open(yaml_path, "r") as f:
            grammar = yaml.safe_load(f)
        
        lang_id = os.path.splitext(os.path.basename(yaml_path))[0]
        
        generate_textmate(grammar, f"vscode/syntaxes/{lang_id}.tmLanguage.json")
        generate_markdown_injection(grammar, f"vscode/syntaxes/{lang_id}-markdown.tmLanguage.json", lang_id)
        generate_kde_xml(grammar, f"syntax/{lang_id}.xml")
        
        print(f"Generated grammars and XML for: {grammar['name']} ({lang_id})")
