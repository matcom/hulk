import os
import subprocess
import re
import sys
import glob

# Configuration
UNIT_PREFIX = "gemini-cron-"
USER_UNIT_DIR = os.path.expanduser("~/.config/systemd/user/")
GEMINI_PATH = "/home/apiad/.npm-global/bin/gemini"

def get_tasks_from_toml(toml_path):
    tasks = []
    if not os.path.exists(toml_path):
        return tasks

    current_task = {}
    try:
        with open(toml_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "[[tasks]]":
                    if current_task:
                        tasks.append(current_task)
                    current_task = {}
                elif "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    k = k.strip()
                    v = v.strip().strip('"').strip("'")
                    if v.lower() == "true": v = True
                    elif v.lower() == "false": v = False
                    current_task[k] = v
        if current_task:
            tasks.append(current_task)
    except Exception as e:
        print(f"Error parsing {toml_path}: {e}")
    return tasks

def sanitize_name(name):
    return re.sub(r'[^a-zA-Z0-9_-]', '-', name).lower()

def sync():
    repo_root = os.getcwd()
    cron_toml_path = os.path.join(repo_root, "cron.toml")
    tasks = get_tasks_from_toml(cron_toml_path)
    
    active_units = []

    for task in tasks:
        name = task.get("name")
        schedule = task.get("schedule") # Now expected to be systemd OnCalendar format
        prompt = task.get("prompt")
        yolo = task.get("yolo", False)

        if not name or not schedule or not prompt:
            continue

        safe_name = sanitize_name(name)
        unit_name = f"{UNIT_PREFIX}{safe_name}"
        active_units.append(unit_name)

        service_content = f"""[Unit]
Description=Gemini Cron Task: {name}
After=network.target

[Service]
Type=oneshot
WorkingDirectory={repo_root}
ExecStart={GEMINI_PATH} {"--yolo" if yolo else ""} -p "{prompt}"

[Install]
WantedBy=default.target
"""
        
        timer_content = f"""[Unit]
Description=Timer for Gemini Cron Task: {name}

[Timer]
OnCalendar={schedule}
Persistent=true

[Install]
WantedBy=timers.target
"""

        # Write files
        service_path = os.path.join(USER_UNIT_DIR, f"{unit_name}.service")
        timer_path = os.path.join(USER_UNIT_DIR, f"{unit_name}.timer")

        with open(service_path, "w") as f:
            f.write(service_content)
        with open(timer_path, "w") as f:
            f.write(timer_content)

        print(f"Updated {unit_name}")

    # Cleanup old units
    existing_timers = glob.glob(os.path.join(USER_UNIT_DIR, f"{UNIT_PREFIX}*.timer"))
    for timer_path in existing_timers:
        unit_name = os.path.basename(timer_path).replace(".timer", "")
        if unit_name not in active_units:
            print(f"Removing obsolete unit: {unit_name}")
            subprocess.run(["systemctl", "--user", "stop", f"{unit_name}.timer"], check=False)
            subprocess.run(["systemctl", "--user", "disable", f"{unit_name}.timer"], check=False)
            os.remove(timer_path)
            service_path = os.path.join(USER_UNIT_DIR, f"{unit_name}.service")
            if os.path.exists(service_path):
                os.remove(service_path)

    # Reload and Enable
    subprocess.run(["systemctl", "--user", "daemon-reload"], check=True)
    for unit_name in active_units:
        subprocess.run(["systemctl", "--user", "enable", "--now", f"{unit_name}.timer"], check=True)

    print("Synchronization complete.")

if __name__ == "__main__":
    sync()
