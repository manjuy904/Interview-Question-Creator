from setuptools import find_packages, setup

setup(
    name="Generative AI Project",
    version='0.0.0',
    author="Manju Manju",
    author_email="manjuy904@gmail.com",
    packages=find_packages(), #this will help to automatically find the constructor file that is __init__ file
    install_requires = []
    
)
# src is local package as constructor file (init) is present there