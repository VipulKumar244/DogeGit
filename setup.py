from setuptools import setup
setup(
    name='doge',
    version='1.0',
    packages=['doge'],
    entry_points={
        'console_scripts':['doge=doge.cli:main']
    }
)