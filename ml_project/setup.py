from setuptools import find_packages, setup


with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name="ml_example",
    packages=find_packages(),
    version="0.1.0",
    description="Project 1: heart decease",
    author=" made-ml-in-prod-2021/greasygoose",
    install_requires=required,
)
