from setuptools import setup

install_requires = [
    'click>6,<7',
    'flask>=0.12.2,<0.13',
]

setup(name='tau',
      version='0.0.1.dev0',
      install_requires=install_requires,
      )
