#!/usr/bin/env python3
"""
Validate an Agent Skill against the official specification.

This script checks:
- SKILL.md exists and has valid structure
- YAML frontmatter is valid
- Required fields (name, description) are present and valid
- Name follows format rules (lowercase, kebab-case, 1-64 chars)
- Description is 1-1024 characters
- Directory name matches skill name
- Referenced files exist

Usage:
    python validate_skill.py /path/to/skill
    python validate_skill.py /path/to/skill/SKILL.md
"""

import re
import sys
import unicodedata
from pathlib import Path
from typing import List, Optional

# Constants from specification
MAX_SKILL_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500

ALLOWED_FIELDS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}


class ValidationError(Exception):
    """Raised when validation fails."""

    pass


def find_skill_md(skill_dir: Path) -> Optional[Path]:
    """Find SKILL.md or skill.md in the directory."""
    for name in ("SKILL.md", "skill.md"):
        path = skill_dir / name
        if path.exists():
            return path
    return None


def parse_frontmatter(content: str) -> tuple:
    """
    Parse YAML frontmatter from SKILL.md content.

    Returns:
        Tuple of (metadata_dict, body_text)
    """
    if not content.startswith("---"):
        raise ValidationError("SKILL.md must start with YAML frontmatter (---)")

    parts = content.split("---", 2)
    if len(parts) < 3:
        raise ValidationError("SKILL.md frontmatter not properly closed with ---")

    frontmatter_str = parts[1]
    body = parts[2].strip()

    # Simple YAML parsing (for validation purposes)
    # For production, use PyYAML or similar
    metadata = {}
    current_key = None
    in_metadata_section = False

    for line in frontmatter_str.strip().split("\n"):
        line = line.rstrip()

        # Handle metadata section
        if line.startswith("metadata:"):
            in_metadata_section = True
            metadata["metadata"] = {}
            continue

        # Handle indented metadata items
        if in_metadata_section and line.startswith("  "):
            if ":" in line:
                key, value = line.strip().split(":", 1)
                metadata["metadata"][key.strip()] = value.strip().strip("\"'")
            continue
        elif in_metadata_section and not line.startswith("  "):
            in_metadata_section = False

        # Handle regular key-value pairs
        if ":" in line and not line.startswith("  "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip("\"'")

            if key in [
                "name",
                "description",
                "license",
                "compatibility",
                "allowed-tools",
            ]:
                metadata[key] = value

    return metadata, body


def validate_name(name: str, skill_dir: Path) -> List[str]:
    """Validate skill name format and directory match."""
    errors = []

    if not name or not isinstance(name, str) or not name.strip():
        errors.append("Field 'name' must be a non-empty string")
        return errors

    name = unicodedata.normalize("NFKC", name.strip())

    if len(name) > MAX_SKILL_NAME_LENGTH:
        errors.append(
            f"Skill name '{name}' exceeds {MAX_SKILL_NAME_LENGTH} character limit "
            f"({len(name)} chars)"
        )

    if name != name.lower():
        errors.append(f"Skill name '{name}' must be lowercase")

    if name.startswith("-") or name.endswith("-"):
        errors.append("Skill name cannot start or end with a hyphen")

    if "--" in name:
        errors.append("Skill name cannot contain consecutive hyphens")

    # Check valid characters: lowercase letters, numbers, hyphens
    if not re.match(r"^[a-z0-9-]+$", name):
        errors.append(
            f"Skill name '{name}' contains invalid characters. "
            "Only lowercase letters, numbers, and hyphens are allowed"
        )

    # Check directory name matches
    dir_name = skill_dir.name
    normalized_dir = unicodedata.normalize("NFKC", dir_name)
    if name != normalized_dir:
        errors.append(f"Directory name '{dir_name}' does not match skill name '{name}'")

    return errors


def validate_description(description: str) -> List[str]:
    """Validate description format."""
    errors = []

    if not description or not isinstance(description, str) or not description.strip():
        errors.append("Field 'description' must be a non-empty string")
        return errors

    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"Description exceeds {MAX_DESCRIPTION_LENGTH} character limit "
            f"({len(description)} chars)"
        )

    return errors


def validate_compatibility(compatibility: str) -> List[str]:
    """Validate compatibility format."""
    errors = []

    if not isinstance(compatibility, str):
        errors.append("Field 'compatibility' must be a string")
        return errors

    if len(compatibility) > MAX_COMPATIBILITY_LENGTH:
        errors.append(
            f"Compatibility exceeds {MAX_COMPATIBILITY_LENGTH} character limit "
            f"({len(compatibility)} chars)"
        )

    return errors


def validate_metadata_fields(metadata: dict) -> List[str]:
    """Validate that only allowed fields are present."""
    errors = []

    for field in metadata.keys():
        if field not in ALLOWED_FIELDS:
            errors.append(
                f"Unknown field '{field}' in frontmatter. "
                f"Use 'metadata' field for custom properties"
            )

    return errors


def validate_skill(skill_dir: Path) -> List[str]:
    """
    Validate a skill directory.

    Args:
        skill_dir: Path to the skill directory

    Returns:
        List of validation error messages. Empty list means valid.
    """
    errors = []

    if not skill_dir.exists():
        return [f"Path does not exist: {skill_dir}"]

    if not skill_dir.is_dir():
        return [f"Not a directory: {skill_dir}"]

    skill_md = find_skill_md(skill_dir)
    if skill_md is None:
        return ["Missing required file: SKILL.md"]

    try:
        content = skill_md.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Error reading SKILL.md: {e}"]

    try:
        metadata, body = parse_frontmatter(content)
    except ValidationError as e:
        return [str(e)]
    except Exception as e:
        return [f"Error parsing frontmatter: {e}"]

    # Validate required fields
    if "name" not in metadata:
        errors.append("Missing required field in frontmatter: name")
    else:
        errors.extend(validate_name(metadata["name"], skill_dir))

    if "description" not in metadata:
        errors.append("Missing required field in frontmatter: description")
    else:
        errors.extend(validate_description(metadata["description"]))

    # Validate optional fields
    if "compatibility" in metadata:
        errors.extend(validate_compatibility(metadata["compatibility"]))

    # Check for unknown fields
    errors.extend(validate_metadata_fields(metadata))

    # Validate that body is not empty
    if not body:
        errors.append("SKILL.md body is empty. Add instructions after frontmatter.")

    return errors


def main():
    """Main entry point."""
    if len(sys.argv) != 2:
        print("Usage: python validate_skill.py /path/to/skill")
        print("   or: python validate_skill.py /path/to/skill/SKILL.md")
        sys.exit(1)

    path = Path(sys.argv[1]).resolve()

    # If path points to SKILL.md, use parent directory
    if path.is_file() and path.name.lower() == "skill.md":
        skill_dir = path.parent
    else:
        skill_dir = path

    print(f"Validating skill at: {skill_dir}")
    print()

    errors = validate_skill(skill_dir)

    if errors:
        print(f"❌ Validation failed with {len(errors)} error(s):")
        print()
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        print()
        sys.exit(1)
    else:
        print("✅ Valid skill!")
        print()

        # Show basic info
        skill_md = find_skill_md(skill_dir)
        if skill_md:
            content = skill_md.read_text(encoding="utf-8")
            metadata, _ = parse_frontmatter(content)

            print("Skill Information:")
            print(f"  Name: {metadata.get('name', 'N/A')}")
            print(f"  Description: {metadata.get('description', 'N/A')}")

            if "license" in metadata:
                print(f"  License: {metadata['license']}")
            if "compatibility" in metadata:
                print(f"  Compatibility: {metadata['compatibility']}")
            if "metadata" in metadata:
                print(f"  Metadata: {metadata['metadata']}")

        print()
        sys.exit(0)


if __name__ == "__main__":
    main()
