from setuptools import setup, find_packages

setup(
    name='Galact',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'galact = galact.__main__:main',
        ],
    },
)
