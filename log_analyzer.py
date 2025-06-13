def analyze_log(log_file_path):
    """
    Analyzes a web server log file for '401 Unauthorized' errors.
    """
    print(f"[*] Analyzing log file: {log_file_path}")
    suspicious_entries = []

    try:
        with open(log_file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                # Check if "401" (Unauthorized) is present in the line
                if " 401 " in line:
                    suspicious_entries.append(f"Line {line_num}: {line.strip()}")
    except FileNotFoundError:
        print(f"[!] Error: Log file not found at '{log_file_path}'")
        return

    if suspicious_entries:
        print("\n[!!!] Found '401 Unauthorized' entries:")
        for entry in suspicious_entries:
            print(entry)
        print(f"\n[Summary] Total '401 Unauthorized' entries found: {len(suspicious_entries)}")
    else:
        print("\n[+] No '401 Unauthorized' entries found. Log appears clean (for 401s).")

if __name__ == "__main__":
    # The name of our log file
    log_filename = "access.log"
    analyze_log(log_filename)
