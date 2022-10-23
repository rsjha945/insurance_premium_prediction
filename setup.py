from setuptools import setup,find_packages
from typing import List


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


#Declaring variables for setup functions
PROJECT_NAME="insurance-premium-predictor"
VERSION="0.0.3"
AUTHOR="Ravi Shankar"
USER_NAME = "rsjha945"
DESRCIPTION="This is a Insurance Premium Prediction Machine Learning Project"
PACKAGES=["insurance"]
REQUIREMENT_FILE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement 
    mention in requirements.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(),
url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
python_requires=">=3.7",
install_requires=get_requirements_list()
)
