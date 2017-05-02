#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbformat
Version  : 4.3.0
Release  : 4
URL      : https://pypi.python.org/packages/f9/c5/89df4abf906f766727f976e170caa85b4f1c1d1feb1f45d716016e68e19f/nbformat-4.3.0.tar.gz
Source0  : https://pypi.python.org/packages/f9/c5/89df4abf906f766727f976e170caa85b4f1c1d1feb1f45d716016e68e19f/nbformat-4.3.0.tar.gz
Summary  : The Jupyter Notebook format
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: nbformat-bin
Requires: nbformat-python
BuildRequires : jsonschema
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# The Jupyter Notebook Format
[![codecov.io](https://codecov.io/github/jupyter/nbformat/coverage.svg?branch=master)](https://codecov.io/github/jupyter/nbformat?branch=master)
[![Code Health](https://landscape.io/github/jupyter/nbformat/master/landscape.svg?style=flat)](https://landscape.io/github/jupyter/nbformat/master)

%package bin
Summary: bin components for the nbformat package.
Group: Binaries

%description bin
bin components for the nbformat package.


%package python
Summary: python components for the nbformat package.
Group: Default

%description python
python components for the nbformat package.


%prep
%setup -q -n nbformat-4.3.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1487700821
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1487700821
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jupyter-trust

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
