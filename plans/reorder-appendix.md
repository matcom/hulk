# Execution Plan: Reorder HULK Syntax Appendix

## Objective

The goal is to reorder the sections within the `pages/appendix-hulk-syntax.qmd` file to match the original intended structure of the HULK language's syntactic elements.

## Architectural Impact

This change is confined to a single documentation file. It has no impact on the software's architecture, logic, or functionality. The purpose is to improve the readability and logical flow of the HULK syntax reference documentation.

## File Operations

- **Modify**: `/home/apiad/Projects/matcom/hulk/pages/appendix-hulk-syntax.qmd`

## Step-by-Step Execution

The strategy is to read the appendix file, split it into logical sections based on the current markdown headers, and then write those sections back to the same file in the correct order.

### Step 1: Read and Partition the Appendix File

The file `pages/appendix-hulk-syntax.qmd` consists of an introductory part followed by multiple sections, each starting with a level 1 Markdown header (e.g., `# Expressions`).

1.  Read the entire content of `/home/apiad/Projects/matcom/hulk/pages/appendix-hulk-syntax.qmd`.
2.  Separate the introductory content from the sections that need reordering. The introduction ends just before the first major section header, which is `# Conditionals`.
3.  The rest of the file content contains the sections to be reordered.

### Step 2: Extract Sections into a Dictionary

Create a dictionary (or a hash map) to store the content of each section.

1.  The keys of the dictionary will be the section names (e.g., "Expressions", "Functions", "Variables").
2.  The values will be the full text content of that section, including the header.
3.  Parse the content from Step 1 and populate the dictionary. You can split the content by the section headers.

The sections to look for are:
- `Conditionals`
- `Expressions`
- `Functions`
- `Functors`
- `Type inference`
- `Iterables`
- `Loops`
- `Macros`
- `Protocols`
- `Types`
- `Type checking`
- `Variables`
- `Vectors`

### Step 3: Reassemble the File in the Correct Order

A new file content will be constructed in memory before writing it back to the file.

1.  Define the correct order of sections as a list of strings:
    ```
    correct_order = [
        "Expressions",
        "Functions",
        "Variables",
        "Conditionals",
        "Loops",
        "Types",
        "Type checking",
        "Type inference",
        "Protocols",
        "Iterables",
        "Vectors",
        "Functors",
        "Macros",
    ]
    ```
2.  Start the new file content with the introductory part that was separated in Step 1.
3.  Iterate through the `correct_order` list. For each section name, retrieve the corresponding section content from the dictionary created in Step 2 and append it to the new file content. Ensure there is a blank line between sections for proper rendering.

### Step 4: Write the Changes to the File

Overwrite the original file with the newly assembled content.

1.  Open `/home/apiad/Projects/matcom/hulk/pages/appendix-hulk-syntax.qmd` in write mode.
2.  Write the reordered content into the file.

## Testing Strategy

After the file has been modified, validation can be performed as follows:

1.  **Manual Review**: Open the modified `pages/appendix-hulk-syntax.qmd` and visually inspect that the sections are now in the order specified in Step 3.
2.  **Rendered Output (Optional)**: If you have `quarto` installed, you can render the book to ensure the page displays correctly. Navigate to the `pages` directory and run `quarto preview appendix-hulk-syntax.qmd`. This will confirm that the reordering did not introduce any rendering issues.
3.  **Diff Check**: Use `git diff pages/appendix-hulk-syntax.qmd` to see the changes. The diff should only show movement of large blocks of text, not content modifications within the sections themselves.
