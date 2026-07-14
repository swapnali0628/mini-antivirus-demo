import os
from utils import log_detection, run_command

SIGNATURES = ["virus123", "malware456"]

def scan_file(filepath):
    try:
        with open(filepath, "r", errors="ignore") as f:
            content = f.read()
            for sig in SIGNATURES:
                if sig in content:
                    log_detection(filepath, sig)
    except Exception as e:
        print(f"Error scanning {filepath}: {e}")

def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            scan_file(os.path.join(root, file))

# --- Intentionally insecure code for CodeQL demo ---
def insecure_eval(user_input):
    # BAD PRACTICE: eval on user input
    eval(user_input)  # CodeQL should flag this

def insecure_command(user_input):
    # BAD PRACTICE: os.system with untrusted input
    run_command(user_input)  # CodeQL should flag this

if __name__ == "__main__":
    print("Scanning current directory...")
    scan_directory(".")
    # Demo insecure calls
    insecure_eval("print('Eval executed!')")
    insecure_command("echo Insecure command executed")
