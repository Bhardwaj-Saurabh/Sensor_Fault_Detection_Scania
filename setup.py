from typing import List
from setuptools import find_packages, setup

# function to get requirements as a list
def get_requirements()->List[str]:
    """
    Returns list of requirements
    """
    requirements = []
    with open('requirements.txt', 'r') as req:
        content = req.read()

    for req in content.split('\n'):
        requirements.append(req)

    return requirements

# setup definition
setup(
    name="sensor",
    version="0.0.1",
    author="Saurabh Bhardwaj",
    author_email="aryan.saurabhbhardwaj@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements(),
)
