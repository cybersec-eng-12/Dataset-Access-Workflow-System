import csv
from pathlib import Path

# Open & Read log file line by line
access_log_path = Path(__file__).parent.parent / 'logs' / 'access_log.log'
access_log_entries = []

# Split each line on the | delimeter to extract the fields

with open(access_log_path, 'r') as log_file:
    next(log_file)  # Skip header line
    for line in log_file:
        line_data = [line.strip() for line in line.strip().split('|')]
        # Store each entry in a dictionary with keys: timestamp, username, dataset, result
        access_log_entries.append({
            'Timestamp': line_data[0],
            'Username': line_data[1],
            'Dataset': line_data[2],
            'Result': line_data[3]
        })

# Write all entries out to reports/access_summary.csv directly

with open(Path(__file__).parent.parent / 'reports' / 'access_summary.csv', 'w', newline='') as csv_file:
    fieldnames = ['Timestamp', 'Username', 'Dataset', 'Result']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(access_log_entries)

print(f"Parsed {len(access_log_entries)} log entries and saved to access_summary.csv")
