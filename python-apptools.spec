%define module	apptools
%define name 	python-%{module}
%define version 4.0.0
%define release %mkrel 1

Summary: 	Enthought Tool Suite - apptools project
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://code.enthought.com/projects/app_tools.php
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Obsoletes:	python-enthought-apptools
Requires:  	python-configobj
Requires:  	python-traitsui >= 4.0.0
Requires:	python-envisage >= 4.0.0
Requires:  	python-numpy >= 1.1.0
BuildRequires: 	python-setuptools >= 0.6c8
BuildRequires: 	python-sphinx

%description
The apptools project includes a set of packages that Enthought has found
useful in creating a number of applications. They implement functionality
that is commonly needed by many applications.

* apptools.appscripting: Framework for scripting applications.
* apptools.help: Provides a plugin for displaying documents and examples
  and running demos in Evisage Workbench applications.
* apptools.io: Provides an abstraction for files and folders in a
  file system.
* apptools.naming: Manages naming contexts, supporting
  non-string data types and scoped preferences.
* apptools.permissions: Supports limiting access to parts of an application 
  unless the user is appropriately authorized (not full-blown security).
* apptools.persistence: Supports pickling the state of a Python
  object to a dictionary, which can then be flexibly applied in
  restoring the state of the object.
* apptools.preferences: Manages application preferences.
* apptools.resource: Manages application resources such as images and sounds.
* apptools.scripting: A framework for automatic recording of Python scripts.
* apptools.sweet_pickle: Handles class-level versioning, to support
  loading of saved data that exist over several generations of
  internal class structures.
* apptools.template: Supports creating templatizable object hierarchies.
* apptools.type_manager: Manages type extensions, including factories to 
  generate adapters, and hooks for methods and functions.
* apptools.undo: Supports undoing and scripting application commands.

%prep
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html/
