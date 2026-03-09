#!/usr/bin/env python3
"""
Hook to log agent model output to the session log file for debugging and auditing.

This hook is triggered after the model response and processes JSON from stdin.
The 'decision' is always 'allow'.
"""
import sys
import os
import json

# Add the hooks directory to path for importing utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import utils

def main():
    """
    Main entry point for the log model output hook.
    
    Reads candidate model responses from stdin and appends them to the log file.
    """
    try:
        input_data = sys.stdin.read()
        if not input_data:
            utils.send_hook_decision("allow")
            return

        data = json.loads(input_data)
        llm_response = data.get("llm_response", {})
        candidates = llm_response.get("candidates", [])
        
        if candidates:
            candidate = candidates[0]
            content_obj = candidate.get("content", {})
            parts = content_obj.get("parts", [])
            finish_reason = candidate.get("finishReason")

            if parts or finish_reason:
                content_to_log = ""
                for part in parts:
                    if isinstance(part, str):
                        content_to_log += part
                    elif isinstance(part, dict) and "text" in part:
                        content_to_log += part["text"]
                if finish_reason:
                    content_to_log += "\n\n"
                
                utils.log_message(content_to_log, mode="a")

        utils.send_hook_decision("allow")

    except Exception:
        # Failsafe: always allow if something goes wrong
        utils.send_hook_decision("allow")

if __name__ == "__main__":
    main()
