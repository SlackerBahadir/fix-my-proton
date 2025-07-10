from rich import print
import os
import subprocess
from time import sleep

def stop_steam():
    print("[bold red]Killing Steam...[/bold red]")
    print("[yellow]running: pkill steam[/yellow]")
    subprocess.run(["pkill", "steam"])
    print("[green]Stopped Steam successfully.")

def start_steam():
    print("[bold red]Starting Steam...[/bold red]")
    print("[yellow]running: steam[/yellow]")
    subprocess.Popen(["steam"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    sleep(5)
    print("[green]Started Steam successfully.")
