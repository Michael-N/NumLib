from setuptools import setup

setup(
   name='NumLib',
   version='1.0',
   description='Provides easy access to large quantities of digits from numerical constants as well as plotting functionality',
   author='Michael S. Naguib',
   author_email='1michael.naguib@gmail.com',
   install_requires=['colorcet','matplotlib','numpy','pandas','bokeh'], #external packages as dependencies
)
