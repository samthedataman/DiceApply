
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
    