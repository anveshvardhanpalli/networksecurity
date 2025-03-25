'''
the setup.py file is used to package and distribute the project.
It is used by setuptools to package the project to define the configuration of the project such as metadata , dependencies and more.
'''

from setuptools import setup,find_packages
from typing import List
def get_requirements()->List[str]:
    requirement_list=[]
    try:
        with open('requirement.txt','r') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirement.txt file not found')
    return requirement_list

setup(
    name="Networksecurity",
    version="0.0.1",
    author="Anvesh",
    author_email="anveshpalli1304@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)