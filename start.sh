#!/bin/bash

echo "🔄 Checking system dependencies..."

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "⚠️ Python not found. Installing Python..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install python3
    else
        sudo apt update && sudo apt install -y python3 python3-pip
    fi
fi

# Ensure pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "⚠️ pip not found. Installing pip..."
    sudo apt install -y python3-pip
fi

# Set environment variables for Streamlit
export STREAMLIT_SERVER_ENABLE_CORS=false
export STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION=false

# Grant execute permissions to the executable
chmod +x DiceApplyAI

# Install required Python packages
echo "🔧 Installing required packages..."
pip3 install -r requirements.txt

# Launch the application
echo "🚀 Launching the Streamlit application..."
./DiceApplyAI
