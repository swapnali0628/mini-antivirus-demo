import os
from utils import log_detection

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

if __name__ == "__main__":
    scan_directory(".")

