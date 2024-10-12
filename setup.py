import sys
import os
from cx_Freeze import setup, Executable

# Determine the base for the executable
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Determine the executable name
target_name = "DiceJobScraper.exe" if sys.platform == "win32" else "DiceJobScraper"

# Create an improved launcher script with more debugging
with open("launcher.py", "w") as f:
    f.write(
        """
import streamlit.web.cli as stcli
import sys
import threading
import time
import webbrowser
import os

def open_browser():
    print("Waiting for Streamlit to start...")
    time.sleep(2)  # Wait for the server to start
    url = 'http://localhost:8501'
    print(f"Opening browser at {url}")
    webbrowser.open_new(url)

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())
    print("Contents of current directory:", os.listdir())
    print("Contents of .streamlit directory:", os.listdir('.streamlit') if os.path.exists('.streamlit') else "No .streamlit directory")
    print("Starting Streamlit application...")
    threading.Thread(target=open_browser).start()
    sys.argv = ["streamlit", "run", "dash.py", "--server.port=8501", "--server.headless=true"]
    print(f"Running with arguments: {sys.argv}")
    sys.exit(stcli.main())
    """
    )

build_exe_options = {
    "packages": [
        "streamlit",
        "pandas",
        "matplotlib",
        "undetected_chromedriver",
        "webdriver_manager",
        "selenium",
        "requests",
        "bs4",
        "webbrowser",
    ],
    "excludes": [],
    "include_files": [
        "dash.py",
        (".streamlit/config.toml", ".streamlit/config.toml"),
    ],
    "include_msvcr": True,
}

executables = [
    Executable(
        "launcher.py",
        base=base,
        target_name=target_name,
    )
]

setup(
    name="DiceJobScraper",
    version="1.0",
    description="Dice Job Scraper and Applicator",
    options={"build_exe": build_exe_options},
    executables=executables,
)
