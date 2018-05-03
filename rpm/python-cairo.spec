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

%description
%{summary}.

%package devel
Summary:    Development components for the pycairo library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{name}-%{version}/pycairo

%build
./setup.py build

%install
rm -rf %{buildroot}
./setup.py install --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING*
%{python_sitearch}/cairo
%{python_sitearch}/pycairo*.egg-info

%files devel
%defattr(-,root,root,-)
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc
