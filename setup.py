from setuptools import setup
import os

setup(
    name='codeSnippets',
    version='1.0.3',
    packages=['code_lessons'],
    url='mailto:vince1133@yahoo.fr',
    license='BSD',
    author='Vincent Scherrer',
    author_email='vince1133@yahoo.fr',
    description='This fabulous program lets you print a dataframe',
    entry_points={'console_scripts': ['command=code_lessons.__main__:main']}
)
