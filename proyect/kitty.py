from pathlib import Path
import subprocess


def kitty_install():
    #URL del bundle
    kitty_url = "https://github.com/kovidgoyal/kitty/releases/download/v0.35.0/kitty-0.35.0-x86_64.txz"
    # Destino de la instalacion
    kitty_destination = "/opt/kitty"
    #Creacion y verificacion de la carpeta /opt/kitty
    Path(kitty_destination).mkdir(parents=True,exist_ok=True)
    #Seteando el destino
    tar_file = Path(kitty_destination) / "kitty.txz"
    #Descargar el archivo kitty.txz a el destino
    subprocess.run(["wget", "-q",kitty_url,"-O",str(tar_file)])

    #Extraer el contenido y borrar el archivo
    subprocess.run(["tar","-vxf",str(tar_file), "-C",kitty_destination])
    subprocess.run(["rm", str(tar_file)])

def lsd_install():
    lsd_url = "https://github.com/lsd-rs/lsd/releases/download/v1.1.2/lsd-musl_1.1.2_amd64.deb"
    lsd_destination = Path("/tmp/lsd/")
    deb_file = Path(lsd_destination) / "lsd.deb" 
    lsd_destination.mkdir(parents=True,exist_ok=True)
    subprocess.run(["wget", "-q", lsd_url, "-O", deb_file])
    subprocess.run(["sudo","apt-get","install","-y",deb_file])
    subprocess.run(["rm","-rf", lsd_destination])

def nvim_install():
    #URL del bundle
    nvim_url = "https://github.com/neovim/neovim/releases/download/v0.10.0/nvim-linux64.tar.gz"
    # Destino de la instalacion
    nvim_destination = "/opt/"
    #Creacion y verificacion de la carpeta /opt/kitty
    Path(nvim_destination).mkdir(parents=True,exist_ok=True)
    #Seteando el destino
    tar_file = Path(nvim_destination) / "nvim.tar.gz"
    #Descargar el archivo kitty.txz a el destino
    subprocess.run(["sudo","wget", "-q",nvim_url,"-O",str(tar_file)])

    #Extraer el contenido y borrar el archivo
    subprocess.run(["sudo","tar","-vxf",str(tar_file), "-C",nvim_destination])
    subprocess.run(["sudo","rm", str(tar_file)])
if __name__ == "__main__":

    nvim_install()
