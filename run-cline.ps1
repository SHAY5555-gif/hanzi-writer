# PowerShell script to run Cline with system prompt from file
# This avoids ENAMETOOLONG by reading the prompt from a file instead of passing it on command line

$prompt = Get-Content .clinerules/system-instructions.md -Raw
cline -p --system-prompt "$prompt" @args
