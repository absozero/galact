from setuptools import setup


setup(
    name='Galact',
    version='2.0.0',
    entry_points={
        'console_scripts': [
            'galact=bot.galact:galact'
        ]
    }
)
