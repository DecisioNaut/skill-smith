# Known Issues

This document tracks known issues, workarounds, and common problems users might encounter.

## VS Code Extension: False Positive Markdown Link Warnings

**Severity:** Informational (Severity 4) - Does not affect functionality

**Symptoms:** VS Code Problems panel shows warnings like:
```
File 'references/VALIDATION.md' not found at '~/Desktop/.../references/VALIDATION.md'
Source: prompts-diagnostics-provider
```

**Affected Files:**
- `SKILL.md` (lines 388-390)
- `examples/api-integration/SKILL.md` (lines 485-486)
- References in `README.md` and other markdown files

**Root Cause:** 
The `prompts-diagnostics-provider` (provided by VS Code extensions like GitHub Copilot, Claude Dev, or similar AI assistants) has difficulty resolving relative markdown links. This is a bug in the extension's path resolution logic, not an issue with the repository.

**Verification:**
All files actually exist and are correctly linked. You can verify this:

```bash
# All should pass validation
python scripts/validate_skill.py .
python scripts/validate_skill.py examples/code-review/
python scripts/validate_skill.py examples/api-integration/

# Verify files exist
ls -la references/
ls -la examples/api-integration/references/
```

### Solutions

#### Solution 1: Filter the Problems Panel (Recommended) ⭐

Hide these specific warnings without disabling the extension:

1. Open Problems panel: `Cmd+Shift+M` (Mac) or `Ctrl+Shift+M` (Windows/Linux)
2. Click the **filter icon** (funnel symbol in the top-right)
3. Add filter: `!prompts-diagnostics-provider`
4. Press Enter

The warnings will disappear from view while keeping other diagnostics visible.

#### Solution 2: Workspace Settings

The repository includes `.vscode/settings.json` with:
```json
{
  "markdown.validate.fileLinks.enabled": false
}
```

This disables file link validation. After pulling these settings:
1. Press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
2. Type: "Reload Window"
3. Press Enter

**Note:** `.vscode/` is gitignored, so you need to create this file locally.

#### Solution 3: Identify and Configure the Extension

Find which extension is causing this:

1. Open Extensions view: `Cmd+Shift+X` (Mac) or `Ctrl+Shift+X` (Windows/Linux)
2. Search for: "copilot", "claude", "prompt", or "AI"
3. Look for extensions that provide prompt/diagnostic features

Common extensions that may cause this:
- **GitHub Copilot** (especially Chat features)
- **Claude Dev / Cline**
- **Cursor** (if using Cursor editor)
- Custom AI coding assistants

#### Solution 4: User Settings Override

Add to your **User Settings** (`Cmd+,` → Extensions → search "settings.json" → Edit):

```json
{
  "github.copilot.chat.diagnostics.enabled": false,
  "problems.visibility": {
    "prompts-diagnostics-provider": "off"
  }
}
```

#### Solution 5: Ignore Information-Level Diagnostics

Since these are Severity 4 (Information), they don't indicate actual problems. You can:
- Ignore them visually
- Hide the Problems panel if not needed
- Focus on Errors and Warnings only (use the filter)

---

## Python Version Compatibility

**Issue:** Validation scripts require Python 3.7+

**Solution:** 
```bash
# Check your Python version
python --version

# Use python3 if needed
python3 scripts/validate_skill.py .
```

If you encounter issues, ensure you're using Python 3.7 or later.

---

## Windows Path Issues

**Issue:** Scripts may have issues with Windows path separators

**Symptoms:** Validation fails with path-related errors on Windows

**Solution:**
The scripts use `pathlib` which should handle cross-platform paths automatically. If you encounter issues:

1. Ensure you're running from the repository root
2. Use forward slashes in paths: `python scripts/validate_skill.py examples/code-review/`
3. Consider using WSL (Windows Subsystem for Linux) for better compatibility

---

## Permission Denied on Scripts

**Issue:** `Permission denied` when running validation or generation scripts

**Solution:**
```bash
# Make scripts executable
chmod +x scripts/validate_skill.py
chmod +x scripts/generate_skill.py

# Or run via Python explicitly
python scripts/validate_skill.py .
```

---

## Git Line Ending Issues

**Issue:** Scripts may not execute correctly if line endings are converted (Windows)

**Solution:**
The repository includes a `.gitattributes` file (if you experience issues, add one):
```
*.py text eol=lf
*.sh text eol=lf
```

Then reset your repository:
```bash
git rm --cached -r .
git reset --hard
```

---

## Contributing Issues or Fixes

If you encounter other issues or have solutions to add:

1. Check the [GitHub Issues](../../issues) for existing reports
2. Open a new issue with:
   - Clear description of the problem
   - Your environment (OS, VS Code version, Python version)
   - Steps to reproduce
   - Any error messages or screenshots
3. Submit a PR if you have a fix!

---

**Last Updated:** February 13, 2026
