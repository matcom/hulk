#!/usr/bin/env python3
"""
Hook to display a customized welcome message at the start of a session.

This hook is triggered on session 'startup', 'resume', or 'clear'.
It fetches project info from pyproject.toml and current git status.
"""
import json
import sys
import os
import tomllib

# Add the hooks directory to path for importing utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils

def get_project_info():
    """
    Retrieves project name and description from pyproject.toml.
    
    Returns:
        tuple: (name, description) or ("Unknown", "No description available.").
    """
    try:
        with open("pyproject.toml", "rb") as f:
            data = tomllib.load(f)
            project = data.get("project", {})
            return project.get("name", "Unknown"), project.get("description", "No description available.")
    except Exception:
        return "Unknown", "No description available."

def get_commands():
    """
    Reads the .gemini/commands/ directory and extracts descriptions from .toml files.
    """
    commands_dir = os.path.join(".gemini", "commands")
    if not os.path.isdir(commands_dir):
        return []
    
    commands = []
    for filename in sorted(os.listdir(commands_dir)):
        if filename.endswith(".toml"):
            command_name = filename[:-5]
            file_path = os.path.join(commands_dir, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    first_line = f.readline().strip()
                    if "description =" in first_line:
                        # Extract description from "description = '...'" or "description = \"...\""
                        desc = first_line.split("=", 1)[1].strip().strip('"').strip("'")
                        commands.append((command_name, desc))
            except Exception:
                continue
    return commands

def main():
    """
    Main entry point for the welcome message hook.
    
    Reads stdin and returns JSON response with a systemMessage containing project context.
    """
    # Read stdin though we don't strictly need it for this simple message
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    name, description = get_project_info()
    git_status_str = utils.get_git_status_short()
    
    if git_status_str:
        status_msg = f"⚠️  Uncommitted changes:\n{git_status_str}"
    else:
        status_msg = "✅ Working tree is clean."

    commands = get_commands()
    command_lines = [f"- `/{cmd_name}`: {desc}" for cmd_name, desc in commands if cmd_name != "onboard"]
    
    message_lines = [
        f"🚀 Welcome to Gemini CLI for `{name}`",
        f"📝 {description}",
        " ",
        "📊 Git Status:",
        status_msg,
        " ",
        "🛠️  Available Commands:",
        *command_lines,
        " ",
    ]
    
    if any(cmd[0] == "onboard" for cmd in commands):
        message_lines.append("💡 Tip: Run `/onboard` for a brief explanation of the project.")

    system_message = "\n".join(message_lines)

    hook_output = {
        "additionalContext": (
            f"The user has started a Gemini CLI session for the project '{name}'. "
            f"Description: {description}. Git Status: {status_msg}"
        )
    }

    utils.send_hook_decision(
        "allow", 
        system_message=system_message,
        hook_output=hook_output
    )

if __name__ == "__main__":
    main()
