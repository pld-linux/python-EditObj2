%define		module	EditObj
Summary:	Useful tool for writing editors of all kinds
Summary(pl):	Narzêdzie s³u¿±ce do tworzenia ró¿nych edytorów
Name:		python-EditObj
Version:	0.5.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://download.gna.org/songwrite/%{module}-%{version}.tar.gz
# Source0-md5:	a8e999353957cd9fa9f5a6d6fcd0e889
URL:		http://oomadness.tuxfamily.org/en/editobj/
Requires:	python-tkinter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EditObj can create and display a Tkinter dialog box for editing any
Python object (similarly to what Java call a Bean editor, but for
Python object). EditObj is a useful tool for writing (text or
non-text) editors of all kinds, including GUI editor and 3D editor.

%description -l pl
EditObj tworzy i wy¶wietla okno dialogowe Tkinter do edycji obiektów
Pythona (podobnie do edytora Java Bean, tylko dla objektów Pythona).
EditObj jest u¿ytecznym narzêdziem s³u¿±cym do tworzenia ró¿nych
edytorów (tekstowych lub nie), w³±cznie z edytorami GUI i 3D.

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
%dir %{py_sitedir}/editobj
%{py_sitedir}/editobj/*.py[co]
%{py_sitescriptdir}/editobj/icons
