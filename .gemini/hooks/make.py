#!/usr/bin/env python3
"""
Hook to run 'make' validation before critical agent actions.

This hook is triggered 'AfterAgent' and ensures that the codebase passes
all linting and testing checks defined in the makefile.
"""
import sys
import os
import subprocess

# Add the hooks directory to path for importing utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils

def main():
    """
    Main entry point for the make validation hook.
    
    Executes 'uv run make' and returns a 'deny' decision if the process fails.
    """
    try:
        # Run make command using uv run to ensure dependencies are available
        result = subprocess.run(
            ["uv", "run", "make"],
            capture_output=True,
            text=True,
            check=False
        )

        if result.returncode != 0:
            # make failed
            error_message = result.stdout + "\n" + result.stderr
            reason = (
                f"Validation failed (make returned {result.returncode}).\n"
                "Please fix the broken tests or linting issues.\n"
                "Output of 'make':\n"
                "```\n" + error_message.strip() + "\n```\n"
                "Fix these issues and ensure 'make' passes before continuing."
            )
            utils.send_hook_decision("deny", reason=reason)
        else:
            # make passed
            utils.send_hook_decision("allow")

    except Exception:
        # Failsafe: always allow if the hook itself fails
        utils.send_hook_decision("allow")

if __name__ == "__main__":
    main()
