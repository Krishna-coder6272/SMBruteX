from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()

# 🟢 Input
console.print("[bold blue]🔐 Welcome to SMBruteX[/bold blue]\n", style="bold")
ip = input("🌐 Enter Target IP: ")
usernames = ["admin", "guest", "user"]
passwords = ["1234", "password", "admin", "guest"]

results = []

# 🚀 Bruteforce Attack Start
console.print(f"\n[bold yellow]🔍 Starting attack on {ip}[/bold yellow]\n")

for username in usernames:
    for password in passwords:
        console.print(f"[cyan]Trying[/cyan] [bold]{username}[/bold]:[bold]{password}[/bold] on {ip}...")
        sleep(0.2)  # Delay to simulate brute force

        # 🧪 Dummy check (replace with real SMB login logic)
        if username == "admin" and password == "1234":
            console.print(f"[green]✅ Success:[/] Login worked for {username}:{password}\n")
            results.append((ip, username, password, "✅ Success"))
        else:
            console.print(f"[red]❌ Failed:[/] Incorrect {username}:{password}\n")
            results.append((ip, username, password, "❌ Failed"))

# 📊 Show Final Table
console.print("\n[bold magenta]📋 Final Results:[/bold magenta]\n")
table = Table(title="SMBruteX Attack Summary")

table.add_column("Target IP", style="magenta")
table.add_column("Username", style="green")
table.add_column("Password", style="yellow")
table.add_column("Status", style="bold red")

for row in results:
    table.add_row(*row)

console.print(table)
console.print("\n[bold blue]🛡️ Brute-force attempt completed![/bold blue]")
