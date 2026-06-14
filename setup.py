'''
The setup.py file is an essential part of packaging and 
distributing python projects. It is used by setuptools
(or distutils in older python versions) to define the configuration
of your projects,such as its metadata,dependencies, and more.
'''

from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    This function returns the list of requirements
    from requirements.txt
    """

    requirement_lst = []

    try:
        with open("requirements.txt", "r") as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()

                # Ignore empty lines and -e .
                if requirement and not requirement.startswith("-e"):
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Anurag",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)