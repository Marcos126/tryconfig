import os
from pathlib import Path
import subprocess

home_path = os.environ.get('HOME')
font_url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip"
font_destination = Path("/usr/share/fonts/hack")

def nerd_fonts():
    font_destination.mkdir(parents=True,exist_ok=True)
    p7z_file = Path(font_destination) / "hack.zip"
    subprocess.run(["wget","-O",p7z_file,font_url])
    subprocess.run(["7z","e",p7z_file, f"-o{font_destination}"])
    subprocess.run(["rm", p7z_file])


if __name__ == '__main__': 
    nerd_fonts()


