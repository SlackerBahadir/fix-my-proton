from rich import print
import os
import sys

def get_proton_versions():
    compatibilitytoolsd_path = os.path.expanduser("~/.steam/steam/compatibilitytools.d")

    if os.path.exists(compatibilitytoolsd_path):
        protons = os.listdir(compatibilitytoolsd_path)
    else:
        print(f"[bold red]{compatibilitytoolsd_path} was not found. Please verify your Steam installation and reinstall Steam if necessary.[/bold red]")
        sys.exit(1)

    return protons

def print_proton_versions():
    protons = get_proton_versions()

    print("[bold blue]Found Proton installations[/bold blue]:")

    for i, proton in enumerate(protons, start=1):
        print(f"[bold green]{i}[/bold green] - {proton}")