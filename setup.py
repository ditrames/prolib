import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prolib",  # Replace with your own username
    version="0.0.1",
    author="ditrames",
    author_email="ditrames@gmail.com",
    description="A small socket wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ditrames/protalib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)