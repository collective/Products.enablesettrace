Introduction
============

To make a long story short: sometimes you need to break into the debugger in the
middle of a Script (Python). To prevent the frustrating ``Unauthorized: import
of 'pdb' is unauthorized`` message, use this enablesettrace package.

This package supports importing the ``pdb`` module. It is a fork of the original
Products.enablesettrace package which still resides in the Zope Subversion
Repository. The only change made was turning the package into an egg.


Installation
============

The installation is as simple as making sure the package is located on the
Python path. For example when you are using zc.buildout list
``Products.enablesettrace`` in the ``eggs`` section::

  [buildout]
  ...
  eggs =
      ...
      Products.enablesettrace


Credits
=======

This code was originally contributed by Zach Bir and `committed by Jim Fulton
<http://svn.zope.org/Products.enablesettrace/trunk/__init__.py?rev=41469&r1=41469&view=log>`_.
Mark van Lent eggified the product.

