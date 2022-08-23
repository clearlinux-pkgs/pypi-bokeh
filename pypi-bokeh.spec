#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-bokeh
Version  : 2.4.3
Release  : 56
URL      : https://files.pythonhosted.org/packages/ac/01/c7622f3f8c6440f4a66ed58bfe5a2a499c2cc8551e00a298ceb94ccc3c70/bokeh-2.4.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/01/c7622f3f8c6440f4a66ed58bfe5a2a499c2cc8551e00a298ceb94ccc3c70/bokeh-2.4.3.tar.gz
Summary  : Interactive plots and applications in the browser from Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-bokeh-bin = %{version}-%{release}
Requires: pypi-bokeh-license = %{version}-%{release}
Requires: pypi-bokeh-python = %{version}-%{release}
Requires: pypi-bokeh-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(jinja2)
BuildRequires : pypi(numpy)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pillow)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(tornado)
BuildRequires : pypi(typing_extensions)

%description
<a href="https://bokeh.org">
<img src="https://static.bokeh.org/logos/logotype.svg" height="60" alt="Bokeh logotype" />
</a>

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
Requires: pypi(jinja2)
Requires: pypi(numpy)
Requires: pypi(packaging)
Requires: pypi(pillow)
Requires: pypi(pyyaml)
Requires: pypi(tornado)
Requires: pypi(typing_extensions)

%description python3
python3 components for the pypi-bokeh package.


%prep
%setup -q -n bokeh-2.4.3
cd %{_builddir}/bokeh-2.4.3
pushd ..
cp -a bokeh-2.4.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656361925
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bokeh
cp %{_builddir}/bokeh-2.4.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-bokeh/6f7c0f2c85b999dcbd5abee2d3a9c9e7881e322b
cp %{_builddir}/bokeh-2.4.3/bokeh/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-bokeh/6f7c0f2c85b999dcbd5abee2d3a9c9e7881e322b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bokeh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bokeh/6f7c0f2c85b999dcbd5abee2d3a9c9e7881e322b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
