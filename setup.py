from setuptools import setup, find_packages

setup(
    name='Galact',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'prompt_toolkit',
    ],
    entry_points={
        'console_scripts': [
            'galact = galact.main:main',
        ],
    },
)
