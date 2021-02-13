# Usage: 
#
# -- Build the project for distribution:
#   python3 setup.py sdist bdist_wheel
# 
# -- Run unit tests:
#   python3 setup.py test


import setuptools

# Change the 'project_name' here to the correct one.
from src import __version__

# Set the project name here.
PROJECT_NAME = 'src'

setuptools.setup(
    name=PROJECT_NAME,
    version=__version__,
    license='MIT License',
    author='William Abreu',
    author_email='contato@williamabreu.net',
    description='Final project for master\'s discipline Algorithm Analysis and Data Structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/williamabreu/graph-tsp',
    install_requires=open('requirements.txt').read().splitlines(),
    platforms='any',
    packages=setuptools.find_packages('.', exclude=(f'{PROJECT_NAME}.tests',)),
    python_requires='>=3.9',
    test_suite=f'{PROJECT_NAME}.tests',
    keywords='graph algorithms tsp optimization',
    entry_points={
        'console_scripts': [
            f'{PROJECT_NAME}={PROJECT_NAME}.__main__:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
