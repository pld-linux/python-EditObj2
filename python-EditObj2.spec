%define		module	EditObj2
Summary:	Useful tool for writing editors of all kinds
Summary(pl.UTF-8):	Narzędzie służące do tworzenia różnych edytorów
Name:		python-%{module}
Version:	0.1
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://download.gna.org/songwrite/%{module}-%{version}.tar.gz
# Source0-md5:	2ecf7ddc6ebf4e14c40f932513defeee
URL:		http://home.gna.org/oomadness/en/editobj/
Requires:	python-tkinter
Obsoletes:	python-EditObj
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a useful tool for writing (text or
non-text) editors of all kinds, including GUI editor and 3D editor.

%description -l pl.UTF-8
EditObj tworzy i wyświetla okno dialogowe Tkinter do edycji obiektów
Pythona (podobnie do edytora Java Bean, tylko dla objektów Pythona).
EditObj jest użytecznym narzędziem służącym do tworzenia
różnych edytorów (tekstowych lub nie), włącznie z edytorami GUI i
3D.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--install-purelib=%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/editobj2
%dir %{py_sitescriptdir}/editobj2
%{py_sitedir}/editobj2/*.py[co]
%{py_sitescriptdir}/editobj2/icons
