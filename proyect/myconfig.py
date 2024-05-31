import os
from pathlib import Path
import subprocess

home_path = os.environ.get('HOME')
packages = ["nvim","kitty","picom","polybar" , "sxhkd", "bspwm"]

def tryconfig(package):
    repo = "https://github.com/Marcos126/tryconfig"   
    destination_repo = f"{home_path}/Documents/tests"
    subprocess.run(["git","clone",repo, destination_repo])
   
    configs_destiny = f"{home_path}/Documents/configs/hola" 
    Path(configs_destiny).mkdir(parents=True,exist_ok=True)
    pool_configs = Path(destination_repo) / package
    print(f"\n\n{pool_configs}")
    configs = Path(configs_destiny) / package
    print(f"{configs}")
    subprocess.run(["mv", pool_configs, configs])

if __name__ == '__main__':

    for package in packages:
        tryconfig(package) 



