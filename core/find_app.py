"""
#  Finds a game according to the entered name or ID and gives the requested information.
# -
#  Created on 10.07.25
"""

import os
import vdf

def find_app(name_or_id: str):
    compatdata_path = os.path.expanduser("~/.steam/steam/steamapps/compatdata")

    if name_or_id not in os.listdir(compatdata_path):
        steamapps_path = os.path.expanduser("~/.steam/steam/steamapps")

        found_apps = []

        for app_manifest in os.listdir(steamapps_path):
            if app_manifest.endswith(".acf"):
                with open(os.path.join(steamapps_path, app_manifest), 'r') as f:
                    data = vdf.load(f)

                app_name = data["AppState"]["name"]
                app_id = data["AppState"]["appid"]

                if name_or_id in app_name:
                    found_apps.append({"name": app_name, "id": app_id})
        return found_apps
    else:
        return name_or_id
