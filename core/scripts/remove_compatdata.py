"""
#  Removes compatdata folder (~/.steam/steam/steamapps/compatdata/{app_id}) of a game
# -
#  Created on 10.07.25
"""

from rich import print
import os
from shutil import rmtree

def remove_compatdata(appid: str):
    apps_compatdata_path = os.path.expanduser(f"~/.steam/steam/steamapps/compatdata/{appid}")

    if os.path.exists(apps_compatdata_path):
        rmtree(apps_compatdata_path)

        print(f"[bold red]Removed[/bold red]: [yellow]{apps_compatdata_path}[/yellow]")
    else:
        print(f"[bold red]{apps_compatdata_path} not found.[/bold red]")