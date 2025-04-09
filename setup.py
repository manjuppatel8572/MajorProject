from setuptools import find_packages,setup

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


setup(
    name='mlproject',
    version='0.0.1'
    ,author='Manju',
    author_email='manjuppatel8572@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)