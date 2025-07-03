# Cline Rules Directory

This directory contains configuration files for the Cline CLI tool.

## What Causes `ENAMETOOLONG` in Cline on Windows?

* Windows command line length is limited to ~32,768 characters (including all flags and arguments).
* When passing the entire massive system-prompt via the `--system-prompt` flag to Cline, the command line exceeds this limit and the CLI fails with `spawn ENAMETOOLONG`. ([GitHub Issue #4480](https://github.com/cline/cline/issues/4480))

## Purpose

The `.clinerules` directory is used to store system instructions and other configuration files for Cline. By placing these files in this directory, you can avoid the Windows command line length limitation that causes `ENAMETOOLONG` errors when passing large system prompts via the `--system-prompt` flag.

## Files in this Directory

- `system-instructions.md`: Contains system instructions for Cline that would normally be passed via the `--system-prompt` flag.

## How to Use

When you run Cline in this project directory, it will automatically load the instructions from `system-instructions.md` without requiring you to pass them via the command line.

## Common Solutions for ENAMETOOLONG

| Solution | How to Implement | Sources |
|----------|------------------|---------|
| **`.clinerules/`** - Store instructions as Markdown files in project | Create `.clinerules` directory (or `.clinerules/system-instructions.md` file that already exists). When running Cline inside the directory, it automatically loads instructions without needing `--system-prompt` flag | Official Cline rules documentation ([docs.cline.bot](https://docs.cline.bot/features/cline-rules)), Blog post about migrating to `.clinerules` ([cline.bot](https://cline.bot/blog/clinerules-version-controlled-shareable-and-ai-editable-instructions)) |
| **`--system-prompt-file`** (in newer CLI versions) | Save instructions to a file, e.g. `prompt.md`, and run: `cline -p --system-prompt-file prompt.md ...` | Mentioned in discussions/command line of Cline and similar projects (llama.cpp) ([GitHub](https://github.com/ggml-org/llama.cpp/discussions/8947)) |
| **Environment variable** | `$env:CLINE_SYSTEM_PROMPT = Get-Content prompt.md -Raw`<br/>`cline -p --system-prompt-env CLINE_SYSTEM_PROMPT ...` | Example in documentation and GitHub thread ([GitHub Issue #4480](https://github.com/cline/cline/issues/4480)) |
| **Short PowerShell script** | Put in `run-cline.ps1`:<br/>`$prompt = Get-Content prompt.md -Raw`<br/>`cline -p --system-prompt "$prompt" @args` | User examples in same GitHub issue ([GitHub Issue #4480](https://github.com/cline/cline/issues/4480)) |
| **JSON config file** | `cline --config cline.config.json` with<br/>`{ "systemPrompt": "./prompt.md", "model": "claude-sonnet-4-20250514" }` | Same blog post and tool documentation ([cline.bot](https://cline.bot/blog/clinerules-version-controlled-shareable-and-ai-editable-instructions)) |

## VS Code Extension

If you're using VS Code, the Cline extension can handle these configurations automatically, making it easier to work with long system prompts.

## Troubleshooting

### "PowerShell is not recognized as an internal or external command"

If you encounter this error when running Cline:

1. Ensure PowerShell 7+ is installed (https://aka.ms/PowerShell).
2. Add its install directory (for example `C:\Program Files\PowerShell\7`) to your **PATH**.
3. When using Git Bash / MSYS shells, call `pwsh` explicitly instead of `powershell`.

See the official guide for more details:  
<https://github.com/cline/cline/wiki/TroubleShooting-%E2%80%90-%22PowerShell-is-not-recognized-as-an-internal-or-external-command%22>

### `spawn ENAMETOOLONG`

`spawn ENAMETOOLONG` indicates the command line is still exceeding Windows’ 32 kB limit. Make sure you **do not** pass the full prompt via `--system-prompt`.  
Use one of the techniques above (`.clinerules` file, `--system-prompt-file`, config, env-var, or script) and then run:

```powershell
cline -p --model claude-sonnet-4-20250514   # note: no --system-prompt flag
```

If you launch Cline from a custom wrapper script, edit that script so it reads the prompt from a file or variable instead of embedding it on the command line.

## Quick Implementation Steps

1. **Create/update** `.clinerules/system-instructions.md` with your instructions.
2. Remove the `--system-prompt` flag from your run command, leaving only `cline -p --model ...`.
3. If you must keep instructions outside the project - move to `prompt.md` and use `--system-prompt-file` or environment variable as demonstrated above.

This keeps your command line short, avoids `ENAMETOOLONG`, and gives you version-controlled, shareable instructions.

## Additional Resources

* Official GitHub discussion on Windows error - Issue #4480 ([GitHub](https://github.com/cline/cline/issues/4480))
* In-depth guide on `.clinerules` in documentation ([docs.cline.bot](https://docs.cline.bot/features/cline-rules))
* Cline blog explaining why to migrate to `.clinerules` with examples ([cline.bot](https://cline.bot/blog/clinerules-version-controlled-shareable-and-ai-editable-instructions))
