from rich import print
import os
import vdf
import sys

from core.steam import *


def reset_launch_option(appid: str):
    userdata_path = os.path.expanduser("~/.steam/steam/userdata")

    users = os.listdir(userdata_path)

    if len(users) > 1:
        print(
            f"[bold yellow]There is {len(users)} users in steam. That's not usually the case, but... which one is your account?[/bold yellow]")

        for i, user in enumerate(users, start=1):
            print(f"[bold green]{i}[/bold green] - [cyan]{user}[/cyan]")

        try:
            choice = int(input("Enter your user's number: "))
        except ValueError:
            print("[bold red]Enter a valid integer.[/bold red]")
            sys.exit(1)

        localconfig_path = os.path.join(userdata_path, users[choice - 1], "config", "localconfig.vdf")

        with open(localconfig_path, 'r') as f:
            data = vdf.load(f)

        try:
            data["UserLocalConfigStore"]["Software"]["Valve"]["Steam"]["apps"][appid]["LaunchOptions"] = ""

            stop_steam()

            with open(localconfig_path, 'w') as f:
                vdf.dump(data, f, True)

            print("[bold green]Launch option reset successfully.[/bold green]")

            start_steam()
        except KeyError:
            print(f"[bold red]Game not found in {localconfig_path}. So there nothing to be fixed.[/bold red]")
    else:
        localconfig_path = os.path.join(userdata_path, users[0], "config", "localconfig.vdf")

        with open(localconfig_path, 'r') as f:
            data = vdf.load(f)

        try:
            data["UserLocalConfigStore"]["Software"]["Valve"]["Steam"]["apps"][appid]["LaunchOptions"] = ""

            stop_steam()

            with open(localconfig_path, 'w') as f:
                vdf.dump(data, f, True)

            print("[bold green]Launch option reset successfully.[/bold green]")

            start_steam()
        except KeyError:
            print(f"[bold red]Game not found in {localconfig_path}. So there nothing to be fixed.[/bold red]")
