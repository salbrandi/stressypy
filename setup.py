from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='stressypy',
    packages=find_packages(),
    version='0.0.9',
    author='Salvador Brandi',
    author_email='salbrandi@gmail.com',
    url='https://github.com/salbrandi/stressypy',
    download_url='https://github.com/salbrandi/stressypy/archive/0.1.tar.gz',
    py_modules=['cpustresser'],
    description='A simple program for calling stress and/or stress-ng from python',
    long_description=long_description,
    install_requires='click',
    entry_points='''
        [console_scripts]
        stressy=stressypy.cli:stressy
        ''',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='cpu stress cores stress-ng test loads object rq'
)
