import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snowflake",
    version="0.1",
    author="Prashanth Setty",
    description="pip installable",
    long_description=long_description,
    packages=setuptools.find_packages(),
)