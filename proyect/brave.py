import subprocess


def add_brave_repository():
    #instalacion de curl en caso de que sea necesario
    subprocess.run(["sudo","apt","install","curl","-y"])

    #Descarga de la llave GPG
    subprocess.run(["sudo", "curl", "-fsSLo", "/usr/share/keyrings/brave-browser-archive-keyring.gpg", "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"])
    
    #Concat de el repositorio de brave al source.list
    repo_entry = "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"
    with open("/etc/apt/sources.list.d/brave-browser-release.list", "w") as file:
        file.write(repo_entry)
    print("Repositorio de Brave añadido correctamente.")

    #Actualizar los repositorios de apt para ver el paquete de brave
    subprocess.run(["sudo", "apt-get", "update"])
    #Instalar brave
    subprocess.run(["sudo", "apt-get", "install","brave-browser","-y"])

if __name__ == '__main__':

    add_brave_repository()
