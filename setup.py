from xml.etree.ElementTree import VERSION
from setuptools import setup,find_packages
from typing import List

#declearing the variables for setup function
PROJECT_NAME = "housing price prediction Nepal"
VERSION = "0.0.0.3"
AUTHOR = "kumar dahal"
DESCRIPTION = "This is my first project in term of Nepal housing"
PACKAGES = find_packages()
REQUIREMENT_FILE_NAME = "requirements.txt"


#read the requiremts.txt file in the List format which has string format
def get_requirements_list()->List[str]:
    """
    Description: This function is going to return the list of 
    requirements.txt file

    return: This funciton is goinh to return a list which 
    contain name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")



setup(
    name= PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description= DESCRIPTION,
    packages = PACKAGES,
    install_requires= get_requirements_list()

)

