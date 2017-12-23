import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'readme.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

install_requires = [
    'django',
    'click',
    'mysqlclient',
]
develop_requires = [
    'ipdb',
    'ipython',
    'readline',
    'mock',
]

setup(
    name='{{ project_name }}',
    version='0.1',
    packages=find_packages(),
    package_dir={'': 'src'},
    license='BSD License',
    description='A tool...',
    long_description=README,
    author='Pawel Kucmus',
    author_email='pkucmus@gmail.com',
    install_requires=install_requires,
    extras_require={
        'develop': develop_requires,
    },
    entry_points={
        'console_scripts': [
            '{{ project_name }} = {{ project_name }}.__main__:cli',
        ],
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Vyze',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
