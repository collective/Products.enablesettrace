from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='Products.enablesettrace',
      version=version,
      description="Allow import of pdb in restricted code.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
      "Intended Audience :: Developers",
      "Framework :: Plone",
      "Framework :: Zope2",
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "License :: OSI Approved :: Zope Public License",
      ],
      keywords='',
      author='Mark van Lent',
      author_email='m.van.lent@zestsoftware.nl',
      url='http://github.com/markvl/Products.enablesettrace',
      license='ZPL 2.1',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
