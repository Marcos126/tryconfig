def reading():
    with open("Packages.txt",'r') as file:
        packages = [line.strip() for line in file if line.strip()]
    return packages
    

package_list = reading()

for package in package_list:
    print(package)
