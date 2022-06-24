# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python3-cairo
Summary:    Python bindings for the cairo library
Version:    1.19.0
Release:    1
License:    MPLv1.1 or LGPLv2
URL:        https://github.com/sailfishos/python-cairo
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  python3-devel
Obsoletes:      python-cairo < %{version}

%description
%{summary}.

%package devel
Summary:    Development components for the pycairo library
Requires:   %{name} = %{version}-%{release}
Obsoletes:  python-cairo-devel < %{version}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}/pycairo

%build
python3 ./setup.py build

%install
rm -rf %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%license COPYING*
%{python3_sitearch}/cairo
%{python3_sitearch}/pycairo*.egg-info

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc
