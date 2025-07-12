from rich import print
import os
import subprocess
import requests
from tqdm import tqdm
import shutil

def install_proton_ge(version: str):
    url = f"https://github.com/GloriousEggroll/proton-ge-custom/releases/download/{version}/{version}.tar.gz"
    download_path = f"/tmp/{version}.tar.gz"
    extract_to = "/tmp"
    target_dir = os.path.expanduser("~/.steam/steam/compatibilitytools.d")

    response = requests.get(url, stream=True)

    if response.content == "Not Found":
        print("[bold red]You entered wrong version name[/bold red].")

    total = int(response.headers.get("content-length", 0))

    with open(download_path, "wb") as f, tqdm(
        desc=f"Downloading {version}",
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(1024):
            f.write(data)
            bar.update(len(data))

    print(f"[yellow]Extracting {version}...[/yellow]")
    subprocess.run(["tar", "-xf", download_path, "-C", extract_to])

    extracted_path = os.path.join(extract_to, version)

    os.makedirs(target_dir, exist_ok=True)
    shutil.move(extracted_path, target_dir)

    print(f"[green]Installed to:[/green] {os.path.join(target_dir, version)}")

    os.remove(download_path)
    print("[bold green]Installation completed successfully.[/bold green]")
