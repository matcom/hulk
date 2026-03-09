#!/usr/bin/env python3
"""
Hook to initialize the Gemini CLI session by resetting the log file.

This hook is triggered on session 'startup', 'resume', or 'clear'.
The 'decision' is always 'allow'.
"""
import sys
import os
from datetime import datetime

# Add the hooks directory to path for importing utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils

def main():
    """
    Main entry point for the session start hook.

    Resets the session log file with a timestamped entry.
    """
    try:
        utils.log_message(
            f"--- Session Started ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')}) ---",
            mode="w"
        )
        utils.send_hook_decision("allow")
    except Exception:
        # Failsafe: always allow if something goes wrong
        utils.send_hook_decision("allow")

if __name__ == "__main__":
    main()
