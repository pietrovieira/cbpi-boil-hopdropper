from setuptools import setup

setup(
  name="cbpi-boil-hopdropper-4",
  version='0.0.1',
  description='...',
  author='Pietro Vieira',
  author_email='contatodopietro@gmail.com',
  url='',
  include_package_data=True,
  package_data={
    #if any
    '': ['*.txt', '*.rst', '*.yaml'],
    'cbpi-boil-hopdropper-4': ['*', '*.txt', '*.rst', '*.yaml']},
    packages=['cbpi-boil-hopdropper-4']
)