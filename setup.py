from setuptools import setup, find_packages

setup(
    name='ml-eng',
    version='0.1',
    packages=find_packages(),
    author='Mohan Gandhi',
    author_email='learn.ai.ml.eng@gmail.com',
    description='This package is used to learn the basics of ml from engineering prespective',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mohanasudhan/ml-eng',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)