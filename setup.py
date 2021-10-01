import setuptools

setuptools.setup(
    name="dictionarysnek",
    version="0.1.0",
    author="Example Author",
    author_email="author@example.com",
    description="A Dictionary API Wrapper for Python",
    long_description="A Module for those who are lazy as f$#% to find a Dictionary API and extract the data from it. Has numerous functions such as:- getsyn, getant, getdata, getdef and more...",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
