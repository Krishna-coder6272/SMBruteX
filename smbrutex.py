from rich.console import Console
from rich.table import Table
from time import sleep
import os

console = Console()

console.print("[bold blue]🔐 Welcome to SMBruteX[/bold blue]\n", style="bold")

ip = input("🌐 Enter Target IP: ")

# ✅ Validate IP format
if len(ip.split(".")) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip.split(".")):
    console.print(f"[bold red]❌ Invalid IP Address: {ip}[/bold red]")
    exit(1)

# Check for required files
if not os.path.exists("usernames.txt") or not os.path.exists("passwords.txt"):
    console.print("[bold red]❌ Required files 'usernames.txt' or 'passwords.txt' are missing![/bold red]")
    exit(1)

# Load usernames and passwords
with open("usernames.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]
with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

console.print("[bold yellow]\n⚠️ Note: This tool is a simulation and does NOT attempt real SMB connections.[/bold yellow]\n")

results = []
console.print(f"[bold yellow]🔍 Starting simulated brute-force attack on {ip}...[/bold yellow]\n")

for username in usernames:
    for password in passwords:
        console.print(f"[cyan]Trying[/cyan] [bold]{username}[/bold]:[bold]{password}[/bold] on {ip}...")
        sleep(0.2)

        # Simulated success condition
        if username == "admin" and password == "1234":
            console.print(f"[green]✅ Simulated Success:[/] Login worked for {username}:{password}\n")
            results.append((ip, username, password, "✅ Simulated Success"))
        else:
            console.print(f"[red]❌ Simulated Failure:[/] Incorrect {username}:{password}\n")
            results.append((ip, username, password, "❌ Simulated Failure"))

# Show result table
console.print("\n[bold magenta]📋 Final Simulated Results:[/bold magenta]\n")

table = Table(title="SMBruteX Simulated Attack Summary")
table.add_column("Target IP", style="magenta")
table.add_column("Username", style="green")
table.add_column("Password", style="yellow")
table.add_column("Status", style="bold red")

for row in results:
    table.add_row(*row)

console.print(table)
console.print("\n[bold blue]🛡️ Simulated brute-force attempt completed.[/bold blue]")
