from setuptools import setup

setup(
    name='test',
    version='0.0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'footest=main:cli'
        ],
    },
)
