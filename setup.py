from setuptools import find_packages, setup
from typing import List

requriment_file_name = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirements()->List[str]:
    with open(requriment_file_name) as requirement_file:
        requriment_list = requirement_file.readline() #in requirements.txt each line has hidden \n so we need to replace it with "".
    requriment_list = [requriment_name.replace("\n", "") for requriment_name in requriment_list]

    if REMOVE_PACKAGE in requriment_list: #after installation setup.py then we dont need to reinstall it so we need to remove (-e .)
        requriment_list.remove(REMOVE_PACKAGE)
    return requriment_list



setup(name='Insurance',
      version='0.0.1',
      description='Insurance Industry lavel project',
      author='NagendraSethi',
      author_email='pro.nagendrasethi@gmail.com', #email associated with github
      packages=find_packages(), #here it find folder which is associated with __init__.py in insurance folder.
      install_reqires = get_requirements()
     )
