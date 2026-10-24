# Network Health Checker

A Python script that monitors the availability of network devices, logs the results with timestamps, and runs automatically every 5 minutes. Built as a first step toward network automation and NOC monitoring.

## Features
- Checks device availability using ICMP (ping)
- Reads the device list from a separate file (`devices.txt`)
- Saves a timestamped history to a CSV report
- Runs automatically with cron

## How to use
1. Add devices to `devices.txt` in the format `name,ip`
2. Run: `python3 health_check.py`
3. Results appear on screen and in `report.csv`

## Automation (every 5 minutes)
Add to `crontab -e`:
`*/5 * * * * cd /path/to/health-checker && /usr/bin/python3 health_check.py >> cron.log 2>&1`

## What I learned
- Running Linux commands from Python (`subprocess`)
- Reading and writing files, CSV reports
- Scheduling tasks with cron
- Troubleshooting a real outage and a VM clock drift using my own reports

## Environment
Ubuntu 26.04 (VMware), Python 3, managed remotely with VS Code over SSH.