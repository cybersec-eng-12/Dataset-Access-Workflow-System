import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime

# Parse the XML log file and extract name, description, & access procedure for each dataset
metadata_xml_path = Path(__file__).parent.parent / 'data' / 'dataset_metadata.xml'

tree = ET.parse(metadata_xml_path)

dataset_metadata_info = []

root = tree.getroot()
for dataset in root.findall('dataset'):
    name = dataset.find('name').text
    description = dataset.find('description').text
    access_procedure = dataset.find('access_procedure').text
    dataset_metadata_info.append({
        'name': name,
        'description': description,
        'access_procedure': access_procedure
    })

# Read access_summary.csv & count total events, successes, and denials
access_summary_path = Path(__file__).parent.parent / 'reports' / 'access_summary.csv'
total_events = 0
successful_accesses = 0
denied_accesses = 0

access_summary_info = []

with open(access_summary_path, 'r') as f:
    next(f)  # Skip header
    for line in f:
        total_events += 1
        if 'SUCCESS' in line:
            successful_accesses += 1
        elif 'DENIED' in line:
            denied_accesses += 1
        access_summary_info.append(line.strip().split(','))

# Build HTML String that includes:

# - Header with the report title and generation timestamp
# - Stats summary row (total / successful / denied counts)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta timestamp="Report generated on: {current_time}">
    <title>Dataset Access Report</title>
</head>
<body>
    <h1>Dataset Access Report</h1>
    <p>Report generated on: {current_time}</p>
    <h2>Access Summary</h2>
    <ul>
        <li>Total Access Events: {total_events}</li>
        <li>Successful Accesses: {successful_accesses}</li>
        <li>Denied Accesses: {denied_accesses}</li>
    </ul>
    <h2>Access Log Details</h2>
    <table border="1" cellpadding="5" cellspacing="0">
"""

# - Color-coded HTML table of all log entries
#    - Green for successful access
#    - Red for denied access

for entry in access_summary_info:
    timestamp, username, dataset, result = entry
    color = 'green' if 'SUCCESS' in result else 'red'
    html_content += f"""
        <tr style="background-color: {color};">
            <td>{timestamp}</td>
            <td>{username}</td>
            <td>{dataset}</td>
            <td><strong>{result}</strong></td>
        </tr>
    """

#  - Dataset metadata cards below the table, pulled from XML
for metadata in dataset_metadata_info:
    html_content += f"""</table>
    <br>
    <h2>Dataset: {metadata['name']} Metadata</h2>
    <p><strong>Description:</strong> {metadata['description']}</p>
    <p><strong>Access Procedure:</strong> {metadata['access_procedure']}</p>
    """
html_content += f"""
</body>
</html>
"""
# Write the HTML string out to reports/dataset_access_report.html
with open(Path(__file__).parent.parent / 'reports' / 'dataset_access_report.html', 'w') as html_file:
    html_file.write(html_content)
print("Report generated and saved to reports/dataset_access_report.html\n")