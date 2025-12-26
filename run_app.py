#!/usr/bin/env python3
"""
Launcher script for Christopher Ton's Resume Website
"""

import os
import subprocess
import sys


def main():
    """Launch the Streamlit resume application"""
    try:
        # Check if we're in the right directory
        if not os.path.exists("src/app.py"):
            print(
                "Error: src/app.py not found. Please run this script from the project root directory."
            )
            sys.exit(1)

        print("Launching Christopher Ton's Resume Website...")
        print("The application will open in your default browser")
        print("URL: http://localhost:8501")
        print("Press Ctrl+C to stop the application")
        print("-" * 50)

        # Run the Streamlit app
        subprocess.run([sys.executable, "-m", "streamlit", "run", "src/app.py"])

    except KeyboardInterrupt:
        print("\nApplication stopped. Thanks for visiting!")
    except Exception as e:
        print(f"Error launching application: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
