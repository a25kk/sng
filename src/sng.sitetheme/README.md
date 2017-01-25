# sng.sitetheme

## Introduction

This package provides an installable python package that can be used to setup
a Plone site theme.

* `Source code @ GitHub <https://github.com/kreativkombinat/sng>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/sng.sitetheme>`_
* `Continuous Integration @ Travis-CI <http://travis-ci.org/kreativkombinat/sng>`_

## How it works

This package provides a Diazo Plone theme as an installable Python egg package.
The generated Python package hold the necessary scaffold to kickstart theme
development.

In order to get productive you still need to generate a theme

```bash
$ cd ${buildout:directory}/src/sng.sitethem/sng/sitetheme/resources
$ yo generator-diazotheme

```


## Installation

To install `sng.sitetheme` you simply add ``sng.sitetheme``
to the list of eggs in your buildout, run buildout and restart Plone.
Then, install `sng.sitetheme` using the Add-ons control panel.


## Configuration

The configuration is done by the package generic setup profile but can be changed by accessing the plone theming control panel
