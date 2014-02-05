%define module	apptools
%define rel		1
%if %mdkversion < 201100
%else
%endif

Summary: 	Enthought Tool Suite - Application Tools
Name: 	 	python-%{module}
Version: 	4.2.1
Release: 	1
Source0: 	http://www.enthought.com/repo/ets/apptools-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	https://github.com/enthought/apptools/
BuildArch: 	noarch
Obsoletes:	python-enthought-apptools
Requires:  	python-configobj
Requires:  	python-traitsui >= 4.2.0
Requires:  	python-numpy >= 1.1.0
BuildRequires: 	python-setuptools >= 0.6c8
BuildRequires: 	python-setupdocs >= 1.0.5 
BuildRequires:	python-sphinx

%description
The apptools project includes a set of packages that Enthought has found
useful in creating a number of applications. They implement functionality
that is commonly needed by many applications.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
%__python setup.py build_docs

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files 
%doc *.txt *.rst examples/ build/docs/html/
%{py_puresitedir}/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 814658
- Update to 4.1.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.0.1-1
+ Revision: 745664
- Update to 4.0.1.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-2
+ Revision: 689267
- Rebuild.
- Remove envisage dependency.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689177
- import python-apptools




