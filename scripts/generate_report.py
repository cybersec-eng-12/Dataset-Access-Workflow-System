import xml.etree.ElementTree as ET

# Parse the XML log file and extract name, description, & access procedure for each dataset

# Read access_summary.csv & count total events, successes, and denials

# Build HTML String that includes:
# - Header with the report title and generation timestamp
# - Stats summary row (total / successful / denied counts)
# - Color-coded HTML table of all log entries
#    - Green for successful access
#    - Red for denied access
#  - Dataset metadata cards below the table, pulled from XML
# Write the HTML string out to reports/dataset_access_report.html