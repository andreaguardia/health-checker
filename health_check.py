import subprocess                      # Lets Python run Linux commands
import csv                             # Tools to write CSV files
import os                              # Tools to check files/folders
from datetime import datetime          # Tools for date and time

# ===== STAGE 1: one IP (not needed anymore) =====
"""ip = "8.8.8.8"      #The IP to check (Google's DNS server)

result = subprocess.run(    #Runs a command, here: ping
    ["ping", "-c", "1", "-W", "1", ip], #Send 1 packet only /Wait max 1 second for a reply
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL  #Hide ping's output (we only want the result)
)

if result.returncode == 0: # 0 = success = device answered
    print(f"{ip} is UP")
else:
    print(f"{ip} is DOWN") """

# ===== STAGE 2: list on screen only (not needed anymore) =====
"""with open("devices.txt") as file:   # Open the device list (closes it when done)
    for line in file:               # Repeat for each line
        line = line.strip()         # Remove spaces/enter at the ends
        if not line or line.startswith("#"):    #Skip empty lines and comments
            continue                            # Jump to the next line
        name, ip = line.split(",")              #  Cut the line at the comma: name | ip
        status = "UP" if is_up(ip) else "DOWN"  # Short if: UP or DOWN
        print(f"{name:<20} {ip:<16} {status}")  #  Print name using 20 spaces (aligned columns) """

# ===== STAGE 3: list + CSV report =====
REPORT = "report.csv"                  # Report file name (UPPERCASE = setting)

def is_up(ip):                         # Create a reusable function: ping one IP
    result = subprocess.run(           # Runs ping
        ["ping", "-c", "1", "-W", "1", ip],    # 1 packet / wait max 1 second
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL      # Hide ping's output
    )
    return result.returncode == 0      # Give back True (UP) or False (DOWN)

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")   # Date+time as text: 2026-10-23 17:40:05
new_file = not os.path.exists(REPORT)  # True if report doesn't exist yet (first time)

with open("devices.txt") as devices, open(REPORT, "a", newline="") as report:   # Open list + open report in "a" = add at the end
    writer = csv.writer(report)        # Tool that writes CSV rows
    if new_file:
        writer.writerow(["timestamp", "name", "ip", "status"])   # First time only: header row

    for line in devices:               # Repeat for each line
        line = line.strip()            # Remove spaces/enter at the ends
        if not line or line.startswith("#"):   # Skip empty lines and comments
            continue                   # Jump to the next line
        name, ip = line.split(",")     # Cut the line at the comma: name | ip
        status = "UP" if is_up(ip) else "DOWN"   # Short if: UP or DOWN
        print(f"{name:<20} {ip:<16} {status}")   # Show on screen (aligned columns)
        writer.writerow([now, name, ip, status]) # Save one row in the report
print(f"\nResults saved to {REPORT}")