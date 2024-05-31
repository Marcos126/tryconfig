import threading
import subprocess
import os 
import signal
import sys
from pathlib import Path
from pwn import * 


#------------------------------------------CRTL + C-----------------------------------------------

#Esta funcion es para capturar el crtl + c.

def def_handler(sig,frame):
    #Imprimimos "saliendo" en la pantalla
    print("\n\n [!] Saliendo.... \n")
    #Salimos con un codigo de error 1 (erroneo)
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)




#------------------------------------------Globals-----------------------------------------------

home_path = os.environ.get('HOME')

def reading():
    with open("Packages.txt",'r') as file:
        packages = [line.strip() for line in file if line.strip()]
    return packages

package_list = reading()



#------------------------------------------SINCRONOS-----------------------------------------------

def command_run(command):
    command_signal = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if command_signal.returncode != 0:
        print(f"Ocurrion un error en la ejecucion de {command}")

def check_package(package):
    result = subprocess.run(["dpkg","-s",package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode !=0:
        command_run(["sudo","DEBIAN_FRONTEND=noninteractive","apt-get","install",package,"-y"])

#------------------------------------------ASINCRONOS-----------------------------------------------

#En esta funcion se va a instalar brave, el cual es mi navegador favorito.

def brave_install():
    #Descarga de la llave GPG.
    command_run(["sudo", "curl", "-fsSLo", "/usr/share/keyrings/brave-browser-archive-keyring.gpg", "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"])
    #Concat de el repositorio de brave al source.list.
    repo_entry = "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"
    with open("/etc/apt/sources.list.d/brave-browser-release.list", "w") as file:
        file.write(repo_entry)

    #Actualizar los repositorios de apt para ver el paquete de brave.
    command_run(["sudo", "apt-get", "update"])

    #Instalar brave.
    command_run(["sudo", "apt-get", "install","brave-browser","-y"])


#En esta funcion se instala una nerd font que es la que yo utilizo.

def nerd_fonts():
    #Url de la fuente
    font_url = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/Hack.zip"
    #Carpeta destino
    font_destination = Path("/usr/share/fonts/hack")
    #Revisamos que exista y sino existe la creamos
    font_destination.mkdir(parents=True,exist_ok=True)
    #Este va a ser el nombre de el archivo que vamos a descargar
    p7z_file = Path(font_destination) / "hack.zip"
    #Lo descargamos
    command_run(["wget","-O",p7z_file,font_url])
    #Lo extraemos
    command_run(["7z","e",p7z_file, f"-o{font_destination}"])
    #Lo borramos
    command_run(["rm", p7z_file])


#En esta funcion se instala kitty, haciendo uso de el kitty bundle
def zsh_install():

    p5.status("Seteando oh_my_zsh")
    oh_my_zsh = "https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh"
    time.sleep(1)
    p5.status("Seteando ohmy_installer")
    ohmy_installer = "/tmp/install.sh"
    time.sleep(1)

    p5.status("Descargando el installer")
    command_run(["wget","-qO", ohmy_installer, oh_my_zsh])
    time.sleep(1)
    install_path = Path(f"{home_path}/.oh-my-zsh")
    if install_path.exists():
        command_run(["rm","-rf",install_path])
    p5.status("Ejecutando el installer")
    command_run(["bash",ohmy_installer,"--unattended"])
    time.sleep(1)
    p5.status("Eliminando el installer")
    command_run(["rm", ohmy_installer])
    time.sleep(1)
    p5.success("Instalacion Finalizada")
    


def update_path():
    p6.status("Updating path")
    with open(f"{home_path}/.zshrc",'a') as file:
        data = f"\nexport PATH=$PATH:/opt/nvim-linux64/bin:/opt/kitty/bin"
        file.write(data)
    time.sleep(1)
    p6.success("Path updateado")

def change_shell():
    p7.status("Cambiando de shell")
    command_run(["sudo","chsh","-s","/bin/zsh", userName])
    p7.success("Shell cambiada")
    time.sleep(3)

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
    command_run(["wget", "-q",kitty_url,"-O",str(tar_file)])
    #Lo extraemos
    command_run(["tar","-vxf",str(tar_file), "-C",kitty_destination])
    #Lo borramos
    command_run(["rm", str(tar_file)])


#En esta funcion voy a traer unos archivos de configuracion de mi repositorio de github y los voy a instalar en los .config correspondientes

def tryconfig():

    repo_packages = ["nvim","kitty","picom","polybar" , "sxhkd", "bspwm"]
    #Seteando la url del repositorio
    url_config_repo = "https://github.com/Marcos126/tryconfig"   
    #Seteando la carpeta en la que van a ser instalados posteriormente
    configs_destiny = Path(f"{home_path}/.config")
    #Seteando el destino de el git clone
    destination_repo = Path("/tmp/tryconfig")
    #Como esta funcion se va a repetir unas veces y no quiero nuevamente o tire error cuando lo haga, agrego un condicional para que solo haga git clone si la carpeat no existe
    if (destination_repo.exists() == False):
        command_run(["git","clone",url_config_repo, destination_repo])
    configs_destiny.mkdir(parents=True, exist_ok=True)

    for package in repo_packages:
        pool_configs = Path(destination_repo) / package
        configs = Path(configs_destiny) / package
        command_run(["mv", pool_configs, configs])
    
    



def lsd_install():
    lsd_url = "https://github.com/lsd-rs/lsd/releases/download/v1.1.2/lsd-musl_1.1.2_amd64.deb"
    lsd_destination = Path("/tmp/lsd/")
    deb_file = Path(lsd_destination) / "lsd.deb" 
    lsd_destination.mkdir(parents=True,exist_ok=True)
    command_run(["wget", "-q", lsd_url, "-O", deb_file])
    command_run(["sudo","apt-get","install","-y",deb_file])
    command_run(["rm","-rf", lsd_destination])

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
    command_run(["wget", "-q",nvim_url,"-O",str(tar_file)])

    #Extraer el contenido y borrar el archivo
    command_run(["tar","-vxf",str(tar_file), "-C",nvim_destination])
    command_run(["rm", str(tar_file)])

if __name__ == '__main__':

    for package in package_list:
        check_package(package)

    p1 = log.progress("Iniciando instalacion")
    p2 = log.progress("Nombre")
    p3 = log.progress("Nombre")
    p4 = log.progress("Nombre")
    p5 = log.progress("Nombre")
    p6 = log.progress("Nombre")
    p7 = log.progress("Nombre")
    p8 = log.progress("Nombre")
    p9 = log.progress("Nombre")
    p0 = log.progress("Nombre")


    functions = [nvim_install,brave_install]
    threads = []

    for function in functions:
        thread = threading.Thread(target=function)
        thread.start()
        threads.append(thread)


        
    time.sleep(30)

