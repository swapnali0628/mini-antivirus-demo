# Mini Antivirus Demo Project

This is a simple Python demo project to illustrate how GitHub CodeQL can analyze code for potential vulnerabilities.

## Features
- Scans files for simple "signatures"
- Logs detections
- Contains intentionally insecure code (`eval`, `os.system`) so CodeQL can flag issues

## Usage
Run:
```bash
python scanner.py
