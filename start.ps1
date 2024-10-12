Write-Host "🔄 Checking system dependencies..."

# Ensure Python is installed
if (-Not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️ Python not found. Installing Python..."
    Start-Process "https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe" -Wait
}

# Ensure pip is installed
if (-Not (Get-Command pip -ErrorAction SilentlyContinue)) {
    Write-Host "⚠️ pip not found. Installing pip..."
    python -m ensurepip --upgrade
}

# Set environment variables for Streamlit
$env:STREAMLIT_SERVER_ENABLE_CORS = "false"
$env:STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION = "false"

# Install required Python packages
Write-Host "🔧 Installing required packages..."
pip install -r requirements.txt

# Grant execute permissions to the executable (optional for Windows)
icacls .\DiceApplyAI.exe /grant Everyone:F

# Launch the application
Write-Host "🚀 Launching the Streamlit application..."
Start-Process -NoNewWindow ./DiceApplyAI.exe
