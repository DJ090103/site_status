import requests
import os
import time
from datetime import datetime

# Ensure output files exist
for file_name in ["active_sites.txt", "not_sites.txt"]:
    if not os.path.exists(file_name):
        open(file_name, "w").close()

while True:
    # Read websites.txt
    if not os.path.exists("websites.txt"):
        print("websites.txt does not exist!")
        break

    with open("websites.txt", "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("All URLs have been checked! Waiting 60 seconds...")
        time.sleep(60)
        continue  # wait and check again later

    # Get the first URL
    url = lines[0].strip()
    print(f"\n🔗 Checking: {url}")

    # Try to get status
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        print(f"{url} → Status Code: {status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{url} → Error: {e}")
        status_code = 0  # use 0 for failed sites

    # Get current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save result
    if status_code == 200:
        with open("active_sites.txt", "a") as f:
            f.write(f"{url} | {status_code} | {current_time}\n")
        print("Saved to active_sites.txt")
    else:
        with open("not_sites.txt", "a") as f:
            f.write(f"{url} | {status_code} | {current_time}\n")
        print("Saved to not_sites.txt")

    # Remove the checked URL from websites.txt
    remaining_lines = lines[1:]
    with open("websites.txt", "w") as f:
        f.writelines(remaining_lines)

    # Wait 60 seconds before checking next
    print("Waiting 30 seconds for next check...")
    time.sleep(30)
