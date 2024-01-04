from setuptools import setup, find_packages

setup(
    name='fastapilogger',
    version='0.1.0',
    author='Kevin Saltarelli',
    author_email='kevinqz@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/kevinqz/fastapilogger',
    license='LICENSE.md',
    description='An awesome logger for FastAPI.',
    long_description=open('README.md').read(),
    install_requires=[
        "fastapi",
        "rich",
        "uuid",
        "json",
        "time",
    ],
)