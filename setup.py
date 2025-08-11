from setuptools import setup, find_packages

def get_requirements(file_path):

    with open(file_path, 'r') as myfile:
        # requirements = myfile.readlines()
        requirements = [req.replace('\n','')  for req in myfile.readlines() if '-e' not in req]
    
    return requirements



setup(

    name= "mlProject",
    version= "0.0.1",
    author='Implement AI',
    author_email= 'alam.john007@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')

)