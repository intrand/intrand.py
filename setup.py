import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="intrand",
    version="0.0.4",
    author="intrand",
    author_email="intrand@intrand.io",
    description="various handy utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/intrand/intrand.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
