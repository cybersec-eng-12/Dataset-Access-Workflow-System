import xml.etree.ElementTree as ET
from pathlib import Path

# Parse the XML log file and extract name, description, & access procedure for each dataset
metadata_xml_path = Path(__file__).parent.parent / 'data' / 'dataset_metadata.xml'

tree = ET.parse(metadata_xml_path)

root = tree.getroot()
for dataset in root.findall('dataset'):
    name = dataset.find('name').text
    description = dataset.find('description').text
    release_data = dataset.find('release_data').text
    file_format = dataset.find('file_format').text
    size = dataset.find('size').text
    access_procedure = dataset.find('access_procedure').text
    print(f"Dataset: {name}\nDescription: {description}\nAccess Procedure: {access_procedure}\n")
# Read access_summary.csv & count total events, successes, and denials

# Build HTML String that includes:
# - Header with the report title and generation timestamp
# - Stats summary row (total / successful / denied counts)
# - Color-coded HTML table of all log entries
#    - Green for successful access
#    - Red for denied access
#  - Dataset metadata cards below the table, pulled from XML
# Write the HTML string out to reports/dataset_access_report.html