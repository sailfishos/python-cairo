# fixme: should be defined in base system side
%define python3_sitearch %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")

Name:       python-cairo
Summary:    Python bindings for the cairo library
Version:    1.17.0
Release:    1
Group:      System/Libraries
License:    MPLv1.1 or LGPLv2
URL:        https://pycairo.readthedocs.io/en/latest/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(cairo)
BuildRequires:  python-devel
BuildRequires:  python3-devel

%description
%{summary}.

%package devel
Summary:    Development components for the pycairo library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%package -n python3-cairo
Summary:    Python 3 bindings for the cairo library

%description -n python3-cairo
%{summary}.

%package -n python3-cairo-devel
Summary:    Development components for the pycairo library
Group:      Development/Libraries
Requires:   python3-cairo = %{version}-%{release}

%description -n python3-cairo-devel
%{summary}.


%prep
%setup -q -n %{name}-%{version}/pycairo

%build
./setup.py build
python3 ./setup.py build

%install
rm -rf %{buildroot}
./setup.py install --skip-build --root %{buildroot}
python3 ./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING*
%{python_sitearch}/cairo
%{python_sitearch}/pycairo*.egg-info

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/pycairo.h
%{_libdir}/pkgconfig/pycairo.pc

%files -n python3-cairo
%defattr(-,root,root,-)
%doc COPYING*
%{python3_sitearch}/cairo
%{python3_sitearch}/pycairo*.egg-info

%files -n python3-cairo-devel
%defattr(-,root,root,-)
%dir %{_includedir}/pycairo
%{_includedir}/pycairo/py3cairo.h
%{_libdir}/pkgconfig/py3cairo.pc
