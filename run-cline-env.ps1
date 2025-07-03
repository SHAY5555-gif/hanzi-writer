# PowerShell script to run Cline using environment variable for system prompt
# This avoids ENAMETOOLONG by using environment variable instead of command line argument

$env:CLINE_SYSTEM_PROMPT = Get-Content .clinerules/system-instructions.md -Raw
cline -p --system-prompt-env CLINE_SYSTEM_PROMPT @args
