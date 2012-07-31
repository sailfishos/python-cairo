# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       python-cairo

# >> macros
# << macros

Summary:    Python bindings for the cairo library
Version:    1.10.0
Release:    1
Group:      System/Libraries
License:    MPLv1.1 or LGPLv2
URL:        http://cairographics.org/pycairo
Source0:    http://cairographics.org/releases/py2cairo-%{version}.tar.bz2
Source100:  python-cairo.yaml
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
%setup -q -n py2cairo-%{version}

# >> setup
# << setup

%build
# >> build pre
./waf configure --prefix=%{_prefix}
./waf build
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
./waf install --destdir=%{buildroot}
# << install pre

# >> install post
# << install post


%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING* INSTALL NEWS README
%{python_sitearch}/cairo/
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/pycairo/
%{_libdir}/pkgconfig/pycairo.pc
# << files devel