from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='HWGraph',
    version='1.1',
    description='A Harvey-Weinberg Simulation Application',
    long_description=long_description,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/Quantum56/HWGraph',  # Optional
    author='Zack Bartley',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Students',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='sample setuptools development graph',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=['matplotlib','pylab', 'numpy', 'pandas'],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Quantum56/HWGraph/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/Quantum56',
        'Source': 'https://github.com/Quantum56/HWGraph',
    },
)