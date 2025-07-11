"""
#  Shows Fix Menu for a game.
# -
#  Created on 10.07.25
"""

from rich import print
import sys
from time import sleep

from core.find_app import find_app
from core.scripts.remove_compatdata import remove_compatdata
from core.scripts.remove_shadercache import remove_shadercache
from core.scripts.reset_launch_options import reset_launch_option
from core.scripts.set_proton_version import set_proton_version

def app_fix_menu(name_or_id: str):
    apps_datas = find_app(name_or_id)

    if not apps_datas:
        print("[bold red]Game not found.[/bold red]")
        sys.exit(1)

    if len(apps_datas) == 1:
        apps_data = apps_datas[0]
    else:
        print(f"[bold red]There is multiple occurrences for search [yellow]'{name_or_id}'[/yellow]. Please select the correct game[/bold red]:")

        for i, app in enumerate(apps_datas, start=1):
            print(f"[bold green]{i}[/bold green] - {app['name']}({app['id']})")

        try:
            number = int(input("Which game are you trying to fix? : "))
        except ValueError:
            print("[bold red]Enter a valid integer.[/bold red]")
            sys.exit(1)

        if number < 1 or number > len(apps_datas):
            print("[bold red]Wrong choice. >:(")
            sys.exit(1)

        apps_data = apps_datas[number - 1]

    app_name = apps_data["name"]
    app_id = apps_data["id"]

    print("Welcome to [bold green]Fix Menu[/bold green] of [bold red]FixMyPROTON![/bold red]")
    print(
        f"This menu opened for game [yellow]'{app_name}'[/yellow]. [red]Please know what you are doing.[/red]")

    while True:
        print("=====================================")
        print("[bold green]1[/bold green] - [bold red]Remove compatdata and start game[/bold red]\n"
              "  [yellow](to refresh the prefix for new proton versions. prevents broken configurations and conflicts between proton versions.)[/yellow]")
        print("[bold green]2[/bold green] - [bold red]Remove shadercache[/bold red]\n"
              "  [yellow](clears precompiled graphics cache. fixes visual glitches, stutters and GPU usage spikes after proton upgrades.)[/yellow]")
        print("[bold green]3[/bold green] - [bold red]Reset launch options (automatically closes Steam, applies change, then reopens it)[/bold red]\n"
              "  [yellow](removes any custom commands like gamemoderun, DXVK async flags, mangohud etc.\n  If you're unsure what might be breaking your game, this is a safe cleanup step.)[/yellow]")
        print("[bold green]4[/bold green] - [bold cyan]Change Proton version[/bold cyan]\n"
              "  [yellow](sets a specific Proton version for this game. Useful if current version causes bugs or doesn't launch.)[/yellow]")
        print("\n[bold yellow]?[/bold yellow] - [bold green]For exiting, enter 0.[/bold green]")
        print("=====================================")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("[bold red]Enter a valid integer.[/bold red]")
            sys.exit(1)

        if choice == 0:
            print("[green]Ok, bye![/green]")

            sys.exit(0)
        elif choice == 1:
            remove_compatdata(app_id)
            sleep(1)
        elif choice == 2:
            remove_shadercache(app_id)
            sleep(1)
        elif choice == 3:
            reset_launch_option(app_id)
            sleep(1)
        elif choice == 4:
            set_proton_version(app_id)
            sleep(1)