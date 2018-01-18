# Copyright (c) 2018, Kevin Rodgers
# Released subject to GNU Lesser General Public License v3
# Please see http://www.gnu.org/licenses

from setuptools import setup, find_packages
import codecs  # To use a consistent encoding

# Get the long description from the relevant file
with codecs.open('DESCRIPTION.rst', encoding='utf-8') as f:
    long_description = f.read()

with open("requirements.txt") as requirements:
    install_requires = requirements.readlines()

setup(
    name='ngrok_rest_cli',
    version='0.1.0',
    description='Simple ngrok CLI',
    long_description=long_description,
    author='Kevin Rodgers',
    author_email='kevin@rodgersworld.com',
    url='https://github.com/kfrodgers/ngrok-rest-cli',
    license='Apache 2.0',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: System Administrators',
                 'Intended Audience :: Developers',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
                 'Programming Language :: Python :: 2.7'],
    keywords='ngrok, cli',
    packages=find_packages(exclude=['test*']),
    scripts=[],
    entry_points={
        'console_scripts': ['ngrok_get = ngrok_rest_cli.ngrok_commands:get_tunnels',
                            'ngrok_start = ngrok_rest_cli.ngrok_commands:start_tunnel',
                            'ngrok_stop = ngrok_rest_cli.ngrok_commands:delete_tunnel',
                            'ngrok_requests = ngrok_rest_cli.ngrok_commands:list_requests']
    },
    install_requires=install_requires,
    data_files=[]
)
