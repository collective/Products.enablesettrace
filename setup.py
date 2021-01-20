from setuptools import setup, find_packages

version = "1.2.0"

with open("README.rst") as myfile:
    readme = myfile.read()
with open("CHANGES.rst") as myfile:
    changes = myfile.read()
long_description = readme + "\n" + changes

setup(
    name="Products.enablesettrace",
    version=version,
    description="Allow import of pdb in restricted code.",
    long_description=long_description,
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 7 - Inactive",
        "Intended Audience :: Developers",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Zope Public License",
    ],
    keywords="Python Zope Plone skin script debugging",
    author="Mark van Lent",
    author_email="m.van.lent@zestsoftware.nl",
    url="http://github.com/collective/Products.enablesettrace",
    license="ZPL 2.1",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
    ],
)
