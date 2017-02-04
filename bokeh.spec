#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bokeh
Version  : 0.12.4
Release  : 1
URL      : https://pypi.python.org/packages/6c/f5/6a4b75f5f7c35771b172994c5b5642dd0f923d781b8eb7a9167339eb63b4/bokeh-0.12.4.tar.gz
Source0  : https://pypi.python.org/packages/6c/f5/6a4b75f5f7c35771b172994c5b5642dd0f923d781b8eb7a9167339eb63b4/bokeh-0.12.4.tar.gz
Summary  : Statistical and novel interactive HTML plots for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: bokeh-bin
Requires: bokeh-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
# Bokeh Examples
## Examples in this repository
This directory contains many examples of different ways to use Bokeh. As Bokeh has been evolving
fast, it is important that you **ensure that the version of an example you're looking at matches
the version of Bokeh you are running**.

%package bin
Summary: bin components for the bokeh package.
Group: Binaries

%description bin
bin components for the bokeh package.


%package python
Summary: python components for the bokeh package.
Group: Default

%description python
python components for the bokeh package.


%prep
%setup -q -n bokeh-0.12.4

%build
export LANG=C
export SOURCE_DATE_EPOCH=1486236001
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1486236001
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
