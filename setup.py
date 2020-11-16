#! usr/bin/env python3

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="api-crved-tutorial", # Replace with your own username
    version="0.0.1",
    author="Ferro Mauro",
    author_email="postmaster@ferromauro.it",
    description="Tutorial for API Cerved.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ferromauro/api-cerved-tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)