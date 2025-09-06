from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from the given file.
    '''
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()
            if req != HYPHEN_E_DOT:
                requirements.append(req)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Tanveer',
    author_email='tanveermohd010@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

    )