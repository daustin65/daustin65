# Set execution policy to allow the module to run
Set-ExecutionPolicy RemoteSigned -Force

# Install the PSWindowsUpdate module
Install-Module -Name PSWindowsUpdate -Force
Get-WindowsUpdate
Install-WindowsUpdate -AcceptAll
# Install a specific update using its KB (Knowledge Base) number:
#  Install-WindowsUpdate -KBArticleID KB50XXXXX -AcceptAll
