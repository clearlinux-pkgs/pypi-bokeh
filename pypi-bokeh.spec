#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : pypi-bokeh
Version  : 3.6.3
Release  : 89
URL      : https://files.pythonhosted.org/packages/2f/a1/32d07573bce3afb3339e165c08ea0c6fc41da7ccdac28488a56403cf2dc7/bokeh-3.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/2f/a1/32d07573bce3afb3339e165c08ea0c6fc41da7ccdac28488a56403cf2dc7/bokeh-3.6.3.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-bokeh-bin = %{version}-%{release}
Requires: pypi-bokeh-license = %{version}-%{release}
Requires: pypi-bokeh-python = %{version}-%{release}
Requires: pypi-bokeh-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(colorama)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_git_versioning)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/bokeh/pm/main/assets/logos/SVG/bokeh-logo-white-text-no-padding.svg">
<img src="https://raw.githubusercontent.com/bokeh/pm/main/assets/logos/SVG/bokeh-logo-black-text-no-padding.svg" alt="Bokeh logo -- text is white in dark theme and black in light theme" height=60/>
</picture>

%package bin
Summary: bin components for the pypi-bokeh package.
Group: Binaries
Requires: pypi-bokeh-license = %{version}-%{release}

%description bin
bin components for the pypi-bokeh package.


%package license
Summary: license components for the pypi-bokeh package.
Group: Default

%description license
license components for the pypi-bokeh package.


%package python
Summary: python components for the pypi-bokeh package.
Group: Default
Requires: pypi-bokeh-python3 = %{version}-%{release}

%description python
python components for the pypi-bokeh package.


%package python3
Summary: python3 components for the pypi-bokeh package.
Group: Default
Requires: python3-core
Provides: pypi(bokeh)
Requires: pypi(contourpy)
Requires: pypi(jinja2)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pandas)
Requires: pypi(pillow)
Requires: pypi(pyyaml)
Requires: pypi(tornado)
Requires: pypi(xyzservices)

%description python3
python3 components for the pypi-bokeh package.


%prep
%setup -q -n bokeh-3.6.3
cd %{_builddir}/bokeh-3.6.3
pushd ..
cp -a bokeh-3.6.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738795246
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bokeh
cp %{_builddir}/bokeh-%{version}/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-bokeh/4a51b5ef3e1f0fefa55249fc75c4939ad21a618e || :
cp %{_builddir}/bokeh-%{version}/src/bokeh/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-bokeh/4a51b5ef3e1f0fefa55249fc75c4939ad21a618e || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bokeh/4a51b5ef3e1f0fefa55249fc75c4939ad21a618e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
