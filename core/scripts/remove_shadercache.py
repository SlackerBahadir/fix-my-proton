"""
#  Removes shadercache folder (~/.steam/steam/steamapps/shadercache/{app_id}) of a game
# -
#  Created on 10.07.25
"""

from rich import print
import os
from shutil import rmtree

def remove_shadercache(appid: str):
    apps_shadercache_path = os.path.expanduser(f"~/.steam/steam/steamapps/shadercache/{appid}")

    if os.path.exists(apps_shadercache_path):
        rmtree(apps_shadercache_path)

        print(f"[bold red]Removed[/bold red]: [yellow]{apps_shadercache_path}[/yellow]")
    else:
        print(f"[bold red]{apps_shadercache_path} not found.[/bold red]")