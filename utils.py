import os

def log_detection(filepath, signature):
    print(f"[ALERT] Detected {signature} in {filepath}")

# --- Intentionally insecure helper ---
def run_command(cmd):
    # BAD PRACTICE: using os.system with untrusted input
    os.system(cmd)
