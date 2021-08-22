from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="switch",
    version="1.0.0",
    author="Luka Mamukashvili",
    author_email="ultraluka0@gmail.com",
    description="Switch-Case for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/UltraStudioLTD/Switch",
    project_urls={
        "Bug Tracker": "https://github.com/UltraStudioLTD/Switch/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    py_modules=["switch"],
    packages=find_packages(),
    install_requires = ['typing;python_version<"3.5"'],
)
