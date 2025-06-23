from setuptools import find_packages,setup
import setuptools

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->list[str]:
    '''
    This function will return list of all requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:          # reading the file
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

__version__ = "0.0.1"
REPO_NAME = "MajorProject"
AUTHOR_USER_NAME = "Manju Patel"
SRC_REPO = "DRPredictionModel"
AUTHOR_EMAIL = "manjuppatel8572@gmail.com"
setup(
    name=SRC_REPO ,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    package_dir={"": "src"},
    packages=find_packages(where= "src"),
    install_requires=get_requirements('requirements.txt'),
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content= "text/markdown",
    url= f"https://github.com/{ AUTHOR_USER_NAME} /{ REPO_NAME }",
    project_urls={
        "Bug Tracker": f"https://github.com/{ AUTHOR_USER_NAME }/{ REPO_NAME} /issues",
        },
    

)