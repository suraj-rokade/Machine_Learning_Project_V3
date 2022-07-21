from setuptools import setup
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Suraj Rokade"
DESCRIPTION ="This is my first project of machine learning"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirement_list()->List[str]:
    """
    Description : This function is going to return list of requirement 
    mentio in requirement.txt

    return This functio is going to return a list which contain
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines().remove('-e .')


PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Suraj Rokade"
DESCRIPTION ="This is my first project of machine learning"
PACKAGES = ["housing"]
REQUIREMNT_FILE_NAME = "requirements.txt"

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requirement = get_requirement_list()
)

