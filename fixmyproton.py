import click
from rich import print

from core.fix_menu import app_fix_menu
from core.find_proton_versions import print_proton_versions

@click.command()
@click.option("--app", "-a", help="Enter an app id or name for selecting.")
@click.option("--fix-menu", "-m", is_flag=True, help="Opens fix menu for selected app. (an app with '--app/-p' needs to be selected for it to work.)")
@click.option("--protons", "-p", is_flag=True)
def parser(app, fix_menu, protons):
    if app and fix_menu:
        app_fix_menu(app)

    if protons:
        print_proton_versions()

if __name__ == '__main__':
    parser()