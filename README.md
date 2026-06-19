# Pyref

A (moderately) simple man-like program to get Python documentation / reference pages.

## USAGE

`pyref [page] [-s/--section section]`

Default sections:
`c-api, deprecations, distributing, extending, faq, howto, installing, library, reference, tutorial, using, whatsnew`

## TODO

- Make pyref_mp parse the .rst files into a more human-readable format, not just plain text. 

## Installation

***WINDOWS/MAC USERS WILL HAVE TO MANUALLY BUILD AND SET ENVIRONMENT VARIABLES, ACCORDING TO THE BUILD SECTION. PYREF WAS MADE ON LINUX, AND ONLY TESTED ON LINUX.***

---

### Linux (64-bit)

---

Use the following command to install pyref:

`curl -sSL https://raw.githubusercontent.com/githuken91/pyref/refs/heads/master/install.sh | sudo sh`

This command automatically installs pyref, pyref_mp (page converter), and the default reference pages (python built-ins).

## Build 

In the source directory, run `make build` to build the pyref & pyref_mp files.

### NOTE:

Currently, there is no way to install the manuals via make. Soon, I will add a makefile command to install the manuals to /opt/pyref/manuals/ and add the environment variables. (Linux/Mac).

The archive with the manuals is located at `http://pyref.alwaysdata.net/refpages.tar.gz`.

Download it, extract it, and set the `PYREF_MANUAL_DIR` environment variable to wherever you extracted the folders to.
