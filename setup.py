from setuptools import setup, find_packages

setup(
    name='pyqubit',
    version='0.3',
    description='A lightweight quantum qubit simulator in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aviral Srivastava',
    author_email='your_email@example.com',
    url='http://github.com/aviral-sri/PyQubit',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
