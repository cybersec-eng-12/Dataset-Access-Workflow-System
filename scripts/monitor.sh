#!/bin/bash

# Change directory to the project root
cd "$(dirname "$(dirname "$0")")"

DATE=$(date +"%Y-%m-%d %H:%M:%S")
LOG="logs/monitor_run.log"

echo "$DATE" >> "$LOG"
echo "======== Workflow Run Started ========" >> "$LOG"

# Call Python scripts for processing
python3 scripts/check_expirations.py >> "$LOG" 2>&1
echo >> "$LOG"
python3 scripts/parse_log.py >> "$LOG" 2>&1
echo >> "$LOG"
python3 scripts/generate_report.py >> "$LOG" 2>&1

echo "Path to HTML report: reports/report.html" >> "$LOG"
echo "======== Workflow Run Completed ========" >> "$LOG"
echo >> "$LOG"