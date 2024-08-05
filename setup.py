from setuptools import setup
setup(
    name = 'nwrap',
    version = '0.1.0',
    packages = ['nwrap'],
    entry_points = {
        'console_scripts': [
            'nwrap = nwrap.__main__:main'
        ]
    })