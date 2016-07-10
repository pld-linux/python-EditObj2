%define		module	EditObj2
Summary:	Useful tool for writing editors of all kinds
Summary(pl.UTF-8):	Narzędzie służące do tworzenia różnych edytorów
Name:		python-%{module}
Version:	0.5.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	https://pypi.python.org/packages/source/E/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	fd7c0c16bb70cdf5eaa30f0e47b16e4f
Patch0:		install.patch
URL:		http://www.lesfleursdunormal.fr/static/informatique/editobj/index_en.html
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-tkinter
Obsoletes:	python-EditObj
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a useful tool for writing (text or
non-text) editors of all kinds, including GUI editor and 3D editor.

%description -l pl.UTF-8
EditObj tworzy i wyświetla okno dialogowe Tkinter do edycji obiektów
Pythona (podobnie do edytora Java Bean, tylko dla objektów Pythona).
EditObj jest użytecznym narzędziem służącym do tworzenia różnych
edytorów (tekstowych lub nie), włącznie z edytorami GUI i 3D.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/editobj2
%{py_sitescriptdir}/editobj2/*.py[co]
%{py_sitescriptdir}/editobj2/icons
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/EditObj2-*.egg-info
%endif
