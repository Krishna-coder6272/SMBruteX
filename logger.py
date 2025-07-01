import csv
import os

def log_success(ip, creds):
    os.makedirs("results", exist_ok=True)
    with open("results/logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ip, creds[0], creds[1]])
