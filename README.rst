`pyfod`
=======

|docs| |build| |coverage| |license| |zenodo|

The `pyfod <https://github.com/prmiles/pyfod/wiki>`_ package is a Python
repository for performing fractional-order derivative operations.  Several different definitions of fractional derivative are available within the package:

- Riemann-Liouville
- Caputo (development)
- Grünwald-Letnikov

For now, the package is designed specifically for problems where the fractional order is between 0 and 1.  Accommodating a broader range of fractional order values will be a feature added as time permits.

Installation
============

This code can be found on the `Github project page <https://github.com/prmiles/pyfod>`_.  To install the master branch directly from Github,

::

    pip install git+https://github.com/prmiles/pyfod.git

You can also clone the repository and run ``python  setup.py install``.

Getting Started
===============

- `Tutorial notebooks <https://nbviewer.jupyter.org/github/prmiles/pyfod/tree/master/tutorials/index.ipynb>`_
- `Release history <https://github.com/prmiles/pyfod/blob/master/CHANGELOG.rst>`_

Feedback
========

- `Feature request <https://github.com/prmiles/pyfod/issues/new?template=feature_request.md>`_
- `Bug report <https://github.com/prmiles/pyfod/issues/new?template=bug_report.md>`_

.. |docs| image:: https://readthedocs.org/projects/pyfod/badge/?version=latest
    :target: https://pyfod.readthedocs.io/en/latest/?badge=latest

.. |build| image:: https://travis-ci.org/prmiles/pyfod.svg?branch=master
    :target: https://travis-ci.org/prmiles/pyfod

.. |coverage| image:: https://coveralls.io/repos/github/prmiles/pyfod/badge.svg?branch=master
    :target: https://coveralls.io/github/prmiles/pyfod?branch=master

.. |zenodo| image:: https://zenodo.org/badge/175037345.svg
    :target: https://zenodo.org/badge/latestdoi/175037345

.. |license| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :target: https://github.com/prmiles/pyfod/blob/master/LICENSE
