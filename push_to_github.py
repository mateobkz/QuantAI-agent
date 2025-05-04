# push_to_github.py

import subprocess
from datetime import datetime

def commit_and_push():
    subprocess.run(["git", "config", "--global", "user.email", "agent@quantai.com"])
    subprocess.run(["git", "config", "--global", "user.name", "QuantAI Agent"])

    subprocess.run(["git", "add", "."])
    commit_msg = f"Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    subprocess.run(["git", "push"])