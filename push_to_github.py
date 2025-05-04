# push_to_github.py

import os
import subprocess
from datetime import datetime

def commit_and_push():
    subprocess.run(["git", "config", "--global", "user.email", "agent@quantai.com"])
    subprocess.run(["git", "config", "--global", "user.name", "QuantAI Agent"])

    subprocess.run(["git", "add", "."])
    commit_msg = f"Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    subprocess.run(["git", "commit", "-m", commit_msg])
    # Push using token authentication if GH_TOKEN is available
    token = os.getenv("GH_TOKEN")
    if token:
        # Retrieve the origin URL and inject token
        repo_url = subprocess.check_output(
            ["git", "remote", "get-url", "origin"], text=True
        ).strip()
        if repo_url.startswith("https://"):
            auth_url = repo_url.replace("https://", f"https://{token}@")
        else:
            auth_url = repo_url
        subprocess.run(["git", "push", auth_url, "HEAD:main"])
    else:
        subprocess.run(["git", "push"])