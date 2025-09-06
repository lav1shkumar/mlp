from setuptools import find_packages,setup
import os
from typing import List


def installPackages(file_path:str)->List[str]:
    req = []
    with open(file_path) as f:
        while True:
            line=f.readline().strip()
            if not line or line=="-e .":
                break
            req.append(line)
    
    return req

print(installPackages("requirements.txt"))

setup(
    name="mlp",
    version="0.1",
    author="Lavish",
    author_email="lavishkumar@outlook.in",
    packages=find_packages(),
    install_requires=installPackages("requirements.txt")
)