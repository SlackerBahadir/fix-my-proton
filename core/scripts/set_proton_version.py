from rich import print
import os
import vdf

from core.steam import *
from core.scripts.remove_compatdata import remove_compatdata
from core.scripts.remove_shadercache import remove_shadercache
from core.find_proton_versions import *

def set_proton_version(appid: str):
    configvdf_path = os.path.expanduser("~/.steam/steam/config/config.vdf")

    if os.path.exists(configvdf_path):
        with open(configvdf_path, 'r') as f:
            data: dict = vdf.load(f)
        proton_versions = get_proton_versions()
        print_proton_versions()

        try:
            choice = int(input("Which proton version you want to set? : "))
        except ValueError:
            print("[bold red]Enter a valid integer.[/bold red]")
            return

        if choice < 1 or choice > len(proton_versions):
            print("[bold red]Wrong choice. >:(")
            return

        selected_proton_version = proton_versions[choice - 1]

        print(f"[yellow]Changing version to [cyan]{selected_proton_version}...[/cyan][/yellow]")

        try:
            data["InstallConfigStore"]["Software"]["Valve"]["Steam"]["CompatToolMapping"][appid]["name"] = selected_proton_version

            stop_steam()

            with open(configvdf_path, 'w') as f:
                vdf.dump(data, f, True)

            remove_compatdata(appid)
            remove_shadercache(appid)

            start_steam()

            print(f"[bold green]Proton version set to:[/bold green] {selected_proton_version}")
        except KeyError:
            data["InstallConfigStore"]["Software"]["Valve"]["Steam"]["CompatToolMapping"][appid].setdefault(appid, {
                    "name": selected_proton_version,
                    "config": "",
                    "priority": "250"
                })

            stop_steam()

            with open(configvdf_path, 'w') as f:
                vdf.dump(data, f, True)

            remove_compatdata(appid)
            remove_shadercache(appid)

            start_steam()

            print(f"[bold green]Proton version set to:[/bold green] {selected_proton_version}")
