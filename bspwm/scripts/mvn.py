#!/usr/bin/python3

import subprocess

#mvn archetype:generate -DgroupId=com.mycompany -DartifactId=HelloWorld -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

artifactId = input("Ingrese el nombre del proyecto: ")

if artifactId == "": 
    artifactId = "GenericName"


subprocess.run(f"mvn archetype:generate -DgroupId=com.marquitos -DartifactId={artifactId} -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false" ,shell=True, text=True)

