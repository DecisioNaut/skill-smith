#!/usr/bin/env python3
"""
Generate a new Agent Skill from a template.

This script creates a new skill directory with:
- SKILL.md with proper frontmatter and structure
- Optional scripts/, references/, assets/ directories
- README.md
- Basic .gitignore

Usage:
    python generate_skill.py --name my-skill --description "What this skill does"
    python generate_skill.py --name my-skill --description "..." --complexity full
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path


def validate_skill_name(name: str) -> bool:
    """Check if skill name follows the format rules."""
    import re

    if not name or len(name) > 64:
        return False
    if name != name.lower():
        return False
    if name.startswith("-") or name.endswith("-"):
        return False
    if "--" in name:
        return False
    if not re.match(r"^[a-z0-9-]+$", name):
        return False

    return True


def create_skill_md(name: str, description: str, author: str = "") -> str:
    """Generate SKILL.md content."""
    metadata_section = ""
    if author:
        metadata_section = f"""metadata:
  author: {author}
  version: "1.0.0"
  created: "{datetime.now().strftime("%Y-%m-%d")}"
"""

    return f"""---
name: {name}
description: {description}
{metadata_section}---

# {name.replace("-", " ").title()}

[Brief overview of what this skill enables]

## When to Use This Skill

Use this skill when:
- [Clear criterion 1]
- [Clear criterion 2]
- [Clear criterion 3]

## Prerequisites

- [Required tool or access 1]
- [Required tool or access 2]

## Core Concepts

[Key terminology or concepts that agents need to understand]

## Step-by-Step Instructions

### Task 1: [Clear Action Name]

1. [Specific, actionable step]
2. [Another specific step with command example]
   ```bash
   # Example command
   command --option value
   ```
3. [Continue with next step]

### Task 2: [Another Action]

1. [Next set of steps]
2. [Include concrete examples]

## Examples

### Example 1: [Common Use Case]

**Input:**
```
[Show sample input]
```

**Steps:**
```bash
# Commands to execute
[command 1]
[command 2]
```

**Expected Output:**
```
[Show expected output]
```

### Example 2: [Edge Case or Variation]

[Show how to handle less common scenarios]

## Troubleshooting

**Problem:** [Common error or issue]
**Solution:** [How to resolve it step by step]

**Problem:** [Another common issue]
**Solution:** [Resolution steps]

## Additional Resources

- [Link to relevant documentation]
- [Link to related skills or tools]
"""


def create_readme(name: str, description: str) -> str:
    """Generate README.md content."""
    return f"""# {name}

{description}

## Overview

[Detailed description of what this skill does and why it exists]

## Installation

This is an Agent Skill. To use it with a skills-compatible agent:

1. Clone or download this skill to your skills directory
2. Ensure the directory name matches the skill name: `{name}/`
3. Your agent will automatically discover it at startup

## Usage

Agents will activate this skill when tasks match the description. You can also explicitly reference it:

\"Use the {name} skill to [describe task]\"

## Examples

### Example 1: [Task Name]

[Show a complete example of using this skill]

### Example 2: [Another Task]

[Show another example]

## Requirements

- [List any prerequisites: tools, libraries, API keys, etc.]

## Validation

Validate this skill using the Agent Skills reference library:

```bash
pip install skills-ref
skills-ref validate {name}/
```

Or use the included validation script:

```bash
python scripts/validate_skill.py .
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Specify license - e.g., Apache-2.0, MIT, etc.]

## Resources

- [Agent Skills Specification](https://agentskills.io/specification)
- [Best Practices](https://agentskills.io/)
- [Example Skills](https://github.com/anthropics/skills)

## Support

[Add contact information or links to issue tracker]
"""


def create_reference_md() -> str:
    """Generate references/REFERENCE.md template."""
    return """# Detailed Reference

This file contains detailed technical reference information that supplements the main SKILL.md.

## API Reference

### Endpoint 1: [Name]

**URL:** `/path/to/endpoint`

**Method:** `GET` / `POST` / `PUT` / `DELETE`

**Parameters:**
- `param1` (string, required): Description
- `param2` (integer, optional): Description

**Example Request:**
```bash
curl -X GET "https://api.example.com/endpoint?param1=value"
```

**Example Response:**
```json
{
  "status": "success",
  "data": {}
}
```

### Endpoint 2: [Name]

[Continue with more endpoints...]

## Data Structures

### Structure 1

```json
{
  "field1": "type and description",
  "field2": "type and description"
}
```

## Additional Details

[Include any other detailed information that doesn't fit in the main SKILL.md]
"""


def create_forms_md() -> str:
    """Generate references/FORMS.md template."""
    return """# Forms and Templates

This file contains structured data formats, schemas, and templates.

## JSON Schema: [Name]

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "field1": {
      "type": "string",
      "description": "Description of field1"
    },
    "field2": {
      "type": "number",
      "description": "Description of field2"
    }
  },
  "required": ["field1"]
}
```

## Template: [Name]

```json
{
  "field1": "example value",
  "field2": 42
}
```

## Request Format

```json
{
  "action": "operation_name",
  "parameters": {
    "param1": "value",
    "param2": "value"
  }
}
```

## Response Format

```json
{
  "status": "success",
  "data": {},
  "errors": []
}
```
"""


def create_example_script() -> str:
    """Generate scripts/example.py template."""
    return """#!/usr/bin/env python3
\"\"\"
Example script for [skill-name].

This script demonstrates [what it does].

Usage:
    python example.py --input file.txt --output result.txt
\"\"\"

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Description of what this script does")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    # Validate inputs
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)
    
    # Main logic
    try:
        if args.verbose:
            print(f"Processing {args.input}...")
        
        # TODO: Implement main logic here
        
        if args.verbose:
            print(f"Writing output to {args.output}...")
        
        # Write results
        output_path = Path(args.output)
        output_path.write_text("Result data here")
        
        if args.verbose:
            print("Done!")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
"""


def create_gitignore() -> str:
    """Generate .gitignore content."""
    return """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~
.DS_Store

# Testing
.pytest_cache/
.coverage

# Logs
*.log

# Temporary files
tmp/
temp/
*.tmp
"""


def generate_skill(
    name: str, description: str, complexity: str, output_dir: Path, author: str = ""
):
    """Generate a new skill with the specified structure."""

    # Validate name
    if not validate_skill_name(name):
        print(f"❌ Error: Invalid skill name '{name}'", file=sys.stderr)
        print("Skill names must:", file=sys.stderr)
        print("  - Be 1-64 characters", file=sys.stderr)
        print("  - Be all lowercase", file=sys.stderr)
        print("  - Use only letters, numbers, and hyphens", file=sys.stderr)
        print("  - Not start or end with hyphen", file=sys.stderr)
        print("  - Not contain consecutive hyphens", file=sys.stderr)
        sys.exit(1)

    # Validate description
    if not description or len(description) > 1024:
        print(f"❌ Error: Description must be 1-1024 characters", file=sys.stderr)
        sys.exit(1)

    # Create skill directory
    skill_dir = output_dir / name
    if skill_dir.exists():
        print(f"❌ Error: Directory already exists: {skill_dir}", file=sys.stderr)
        sys.exit(1)

    print(f"Creating skill: {name}")
    print(f"Location: {skill_dir}")
    print(f"Complexity: {complexity}")
    print()

    skill_dir.mkdir(parents=True)

    # Create SKILL.md
    (skill_dir / "SKILL.md").write_text(create_skill_md(name, description, author))
    print("✅ Created SKILL.md")

    # Create README.md
    (skill_dir / "README.md").write_text(create_readme(name, description))
    print("✅ Created README.md")

    # Create .gitignore
    (skill_dir / ".gitignore").write_text(create_gitignore())
    print("✅ Created .gitignore")

    # Create optional directories based on complexity
    if complexity in ("medium", "full"):
        refs_dir = skill_dir / "references"
        refs_dir.mkdir()
        (refs_dir / "REFERENCE.md").write_text(create_reference_md())
        (refs_dir / "FORMS.md").write_text(create_forms_md())
        print("✅ Created references/")

    if complexity == "full":
        scripts_dir = skill_dir / "scripts"
        scripts_dir.mkdir()
        example_script = scripts_dir / "example.py"
        example_script.write_text(create_example_script())
        example_script.chmod(0o755)  # Make executable
        print("✅ Created scripts/")

        assets_dir = skill_dir / "assets"
        (assets_dir / "templates").mkdir(parents=True)
        print("✅ Created assets/")

    print()
    print(f"🎉 Skill '{name}' created successfully!")
    print()
    print("Next steps:")
    print(f"  1. cd {name}/")
    print("  2. Edit SKILL.md to add your instructions")
    print("  3. Add examples and test your skill")
    print("  4. Validate: python ../scripts/validate_skill.py .")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Generate a new Agent Skill from a template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Simple skill (SKILL.md only)
  python generate_skill.py --name my-skill --description "What it does"
  
  # Medium skill (with references/)
  python generate_skill.py --name my-skill --description "..." --complexity medium
  
  # Full skill (with scripts/ and assets/)
  python generate_skill.py --name my-skill --description "..." --complexity full --author john-doe
""",
    )

    parser.add_argument(
        "--name",
        required=True,
        help="Skill name (lowercase, hyphens only, e.g., 'pdf-processor')",
    )
    parser.add_argument(
        "--description",
        required=True,
        help="Skill description (what it does and when to use it)",
    )
    parser.add_argument(
        "--complexity",
        choices=["simple", "medium", "full"],
        default="simple",
        help="Skill complexity level (default: simple)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path.cwd(),
        help="Output directory (default: current directory)",
    )
    parser.add_argument(
        "--author", default="", help="Author name (optional, added to metadata)"
    )

    args = parser.parse_args()

    generate_skill(
        name=args.name,
        description=args.description,
        complexity=args.complexity,
        output_dir=args.output,
        author=args.author,
    )


if __name__ == "__main__":
    main()
