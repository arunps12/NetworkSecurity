from setuptools import find_packages,setup
from typing import List

'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It contains metadata about the project
and instructions on how to install it. 
'''

def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Arun Prakash Singh",
    author_email="mail.arun1289@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)