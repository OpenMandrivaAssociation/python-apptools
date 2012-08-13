%define module	apptools
%define name 	python-%{module}
%define version 4.1.0
%define rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary: 	Enthought Tool Suite - Application Tools
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/apptools/
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Obsoletes:	python-enthought-apptools
Requires:  	python-configobj
Requires:  	python-traitsui >= 4.2.0
Requires:  	python-numpy >= 1.1.0
BuildRequires: 	python-setuptools >= 0.6c8
BuildRequires: 	python-sphinx

%description
The apptools project includes a set of packages that Enthought has found
useful in creating a number of applications. They implement functionality
that is commonly needed by many applications.

%prep
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html/
%py_sitedir/%{module}*
