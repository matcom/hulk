import json
import os
import subprocess
from datetime import datetime

# Configuration
LOG_FILE = os.getenv("GEMINI_LOG_FILE", "gemini.log")

def get_git_status_short():
    """
    Returns the short git status output.
    
    Returns:
        str: The output of 'git status --short' or an error message.
    """
    try:
        return subprocess.check_output(
            ["git", "status", "--short"], 
            stderr=subprocess.STDOUT
        ).decode().strip()
    except Exception:
        return None

def get_modified_files():
    """
    Returns a list of modified and untracked files using git status.
    
    Returns:
        list: A list of file paths.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        files = []
        for line in result.stdout.splitlines():
            if line.strip():
                # Format: 'M  path/to/file' or '?? path/to/file'
                files.append(line[3:].strip())
        return files
    except Exception:
        return []

def log_message(message, mode="a"):
    """
    Logs a message to the GEMINI_LOG_FILE.
    
    Args:
        message (str): The message to log.
        mode (str): The file opening mode ('a' for append, 'w' for write).
    """
    try:
        with open(LOG_FILE, mode, encoding="utf-8") as f:
            f.write(message)
    except Exception:
        pass

def send_hook_decision(decision, reason=None, system_message=None, hook_output=None):
    """
    Prints the standard JSON response for a Gemini CLI hook.
    
    Args:
        decision (str): 'allow' or 'deny'.
        reason (str, optional): The reason for denial.
        system_message (str, optional): A system message to display to the user.
        hook_output (dict, optional): Additional context for the UI.
    """
    response = {"decision": decision}
    if reason:
        response["reason"] = reason
    if system_message:
        response["systemMessage"] = system_message
    if hook_output:
        response["hookSpecificOutput"] = hook_output
    
    print(json.dumps(response))
