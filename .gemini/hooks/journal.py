#!/usr/bin/env python3
"""
Hook to enforce project journaling for all significant changes.

This hook is triggered 'AfterAgent' and checks if the daily journal entry has been updated
whenever there are uncommitted changes in the repository.
"""
import sys
import os
from datetime import datetime

# Add the hooks directory to path for importing utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils

def main():
    """
    Main entry point for the journal enforcement hook.
    
    Checks git status for uncommitted changes and identifies if the current daily journal
    has been updated accordingly. Returns 'deny' if it's missing.
    """
    try:
        modified_files = utils.get_modified_files()
        
        today = datetime.now().strftime("%Y-%m-%d")
        journal_file = f"journal/{today}.md"

        # Check if there are changes other than the daily journal
        significant_changes = [
            f for f in modified_files
            if f != journal_file
        ]

        # Check if the daily journal was updated
        journal_updated = journal_file in modified_files

        if significant_changes and not journal_updated:
            utils.send_hook_decision(
                "deny",
                reason=(
                    f"Please add a one-line entry to {journal_file} "
                    "describing the changes you just made. Do not stop until this file is updated."
                )
            )
        else:
            utils.send_hook_decision("allow")

    except Exception:
        # Failsafe: always allow if something goes wrong
        utils.send_hook_decision("allow")

if __name__ == "__main__":
    main()
