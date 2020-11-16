from setuptools import setup, find_packages
from domain-name-generator.__version__ import __version__


setup(
    name="domain-name-generator",
    author="James Campbell",
    author_email="james@jamescampbell.us",
    version=__version__,
    license="MIT",
    description="Generate domain names fast.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=["domain-name-generator"],
    py_modules=["domain-name-generator"],
    keywords=["nlp", "domains", "name-generator", "naming", "branding"],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["pprint"],
    entry_points={"console_scripts": ["domain-name-generator = domain-name-generator.domain-name-generator:main"]},
    url="https://github.com/jamesacampbell/domain-name-generator",
    download_url="https://github.com/jamesacampbell/findpi/archive/{}.tar.gz".format(
        __version__
    ),
)
