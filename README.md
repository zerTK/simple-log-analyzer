A simple Python script to parse web server access logs and extract only security relevant details from them.

 ## Project Objective
 This project illustrates core cybersecurity concepts in:
 - Log Analysis: Interpreting and picking out details from log files.
 - Basic Scripting: Automating security checks through script in Python.
 - Vulnerability Detection: Determining possible attempts of unauthorized access (e.g. failed logins).

 ## Usage
 The log_analyzer. py script parses the given log file (access. log by default)

 ## Contents of this Repository
 - log_analyzer. py: Primary Python script.
 - access. log: An example log file which can be used to demo and test.

 ## How to Run the Analyzer
 1. Clone the repository (if you hadn't already):
 bash git clone https://github.com/zerTK/simple-log-analyzer.git
 cd simple-log-analyzer

 2. Make sure you have Python 3 installed:
 ``bash python3 --version
 # Output will be similar to: Python 3.x.x

3. Initialize the script from your terminal
''bash
python3 log_analyzer.py

## Expected Output 

The script will print messages indicating its progress and then list any '401 Unauthorized' entries it finds, followed by a summary count.

[*] Analyzing log file: access.log

[!!!] Found '401 Unauthorized' entries:
Line 3: 192.168.1.12 - - [11/Jun/2025:10:00:10 +0000] "POST /admin/login HTTP/1.1" 401 150 - "Failed password for user 'admin'"
Line 5: 192.168.1.12 - - [11/Jun/2025:10:00:20 +0000] "POST /admin/login HTTP/1.1" 401 150 - "Invalid username 'testuser'"
Line 7: 192.168.1.12 - - [11/Jun/2025:10:00:30 +0000] "POST /admin/login HTTP/1.1" 401 150 - "Authentication required"

[Summary] Total '401 Unauthorized' entries found: 3


