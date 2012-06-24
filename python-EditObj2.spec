%define		pname	EditObj
Summary:	Usefull tool for writing editors of all kinds
Summary(pl):	Narz�dzie s�u��ce do tworzenia r�nych edytor�w
Name:		python-EditObj
Version:	0.5.3
Release:	1
License:	GPL
Group:		Applications
Source0:	http://oomadness.tuxfamily.org/downloads/%{pname}-%{version}.tar.gz
# Source0-md5:	b933eac5959e2e269a806bd7c2ff0bee
URL:		http://oomadness.tuxfamily.org/en/editobj/
Requires:	python-tkinter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a usefull tool for writing (text or
non-text) editors of all kinds, including GUI editor and 3D editor.

%description -l pl
EditObj tworzy i wy�wietla okno dialogowe Tkinter do edycji objekt�w
Pythona (podobnie do edytora Java Bean, tylko dla objekt�w Pythona).
EditObj jest u�ytecznym narz�dziem s�u��cym do tworzenia r�nych
edytor�w (tekstowych lub nie), w��cznie z edytorami GUI i 3D.

%prep
%setup -q -n %{pname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/editobj
%{py_sitedir}/editobj/*.py[co]
%{py_sitedir}/editobj/icons
