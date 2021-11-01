#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nbformat
Version  : 5.1.3
Release  : 50
URL      : https://files.pythonhosted.org/packages/e5/bd/847367dcc514b198936a3de8bfaeda1935e67ce369bf0b3e7f3ed4616ae8/nbformat-5.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/e5/bd/847367dcc514b198936a3de8bfaeda1935e67ce369bf0b3e7f3ed4616ae8/nbformat-5.1.3.tar.gz
Summary  : The Jupyter Notebook format
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: nbformat-license = %{version}-%{release}
Requires: nbformat-python = %{version}-%{release}
Requires: nbformat-python3 = %{version}-%{release}
Requires: ipython_genutils
Requires: jsonschema
Requires: jupyter_core
Requires: traitlets
BuildRequires : buildreq-distutils3
BuildRequires : jsonschema
BuildRequires : traitlets

%description
This package contains the base implementation of the Jupyter Notebook format,
            and Python APIs for working with notebooks.

%package license
Summary: license components for the nbformat package.
Group: Default

%description license
license components for the nbformat package.


%package python
Summary: python components for the nbformat package.
Group: Default
Requires: nbformat-python3 = %{version}-%{release}

%description python
python components for the nbformat package.


%package python3
Summary: python3 components for the nbformat package.
Group: Default
Requires: python3-core
Provides: pypi(nbformat)
Requires: pypi(ipython_genutils)
Requires: pypi(jsonschema)
Requires: pypi(jupyter_core)
Requires: pypi(traitlets)

%description python3
python3 components for the nbformat package.


%prep
%setup -q -n nbformat-5.1.3
cd %{_builddir}/nbformat-5.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635757429
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nbformat
cp %{_builddir}/nbformat-5.1.3/COPYING.md %{buildroot}/usr/share/package-licenses/nbformat/4864371bd27fe802d84990e2a5ee0d60bb29e944
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nbformat/4864371bd27fe802d84990e2a5ee0d60bb29e944

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
