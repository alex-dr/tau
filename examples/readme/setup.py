from setuptools import find_packages, setup

setup(
    name='readme',
    install_requires=['tau'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'readme=readme.main:cli',
            'readme-serve=readme.main:app',
        ],
    },
)
