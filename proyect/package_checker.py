import subprocess

def check_package(package):
    result = subprocess.run(["dpkg","-s",package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode !=0:
        subprocess.run(["sudo","apt-get","install",package,"-y"])
    return result.returncode == 0 


