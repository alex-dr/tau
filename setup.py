from setuptools import setup

install_requirements = [
    'click>6,<7',
    'flask>=0.12.2,<0.13',
    'pycontracts',
]

test_requirements = [
    'pytest'
]

setup(
    name='tau',
    version='0.0.1.dev0',
    install_requires=install_requirements,
    extras_require={
        'test': test_requirements,
        'testing': test_requirements,
        },
    )
