import streamlit.web.cli as stcli
import subprocess
import os
import sys
import webbrowser


def resolve_path(filename):
    """Resolve the absolute path for bundled files."""
    if getattr(sys, "frozen", False):  # When packaged with cx_Freeze
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, filename)


def show_loading_screen():
    """Launch the loading screen."""
    try:
        if os.name == "nt":  # Windows
            subprocess.Popen([resolve_path("loading_screen.exe")])
        else:  # macOS / Linux
            subprocess.Popen(["python3", resolve_path("loading_screen.py")])
    except Exception as e:
        print(f"Failed to launch loading screen: {e}")


def main():
    """Main function to launch the Streamlit app."""
    # Set required environment variables
    os.environ["STREAMLIT_SERVER_PORT"] = "8501"
    os.environ["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
    os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

    # Open the app in the browser after a short delay
    webbrowser.open("http://localhost:8501", new=2)

    # Run the Streamlit app without triggering development mode issues
    sys.argv = ["streamlit", "run", resolve_path("dash.py")]
    try:
        sys.exit(stcli.main())
    except Exception as e:
        print(f"Error running Streamlit app: {e}")


if __name__ == "__main__":
    show_loading_screen()
    main()
