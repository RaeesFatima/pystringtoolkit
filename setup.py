from setuptools import setup, find_packages

setup(
    name="pystringtoolkit",
    version="0.1.3",
    author="Raees Fatima",
    description="Handy string utilities for Python",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    url="https://github.com/RaeesFatima/pystringtoolkit",
    project_urls={
        "Source": "https://github.com/RaeesFatima/pystringtoolkit",
        "Bug Tracker": "https://github.com/RaeesFatima/pystringtoolkit/issues",
    },
)
