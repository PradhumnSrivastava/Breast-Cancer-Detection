from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements





setup(
    name="Breast Cancer Detection",
    version= "0.0.1",
    author="Pradhumn Srivastava",
    author_email="Srivastavapadhumn@gmail.com",
    description="This Model will predict is there one suffering from cancer or not",
    packages= find_packages(),
    
    install_requires = get_requirements('requirements.txt')  
    
    
)