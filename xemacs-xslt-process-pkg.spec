Summary:	Interactive spelling corrector with GNU xslt-process
Summary(pl):	Interakcyiny korektor pisowni u¿ywaj±cy GNU xslt-process-a
Name:		xemacs-xslt-process-pkg
%define		srcname	xslt-process
Version:	1.05
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xslt-process
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with GNU xslt-process.

%description -l pl
Interakcyiny korektor pisowni u¿ywaj±cy GNU xslt-process-a.

%prep
%setup -q -c

#%build
#xemacs -batch -q -no-site-file -f batch-byte-compile lisp/xslt-process/xslt-process.el

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/xslt-process/ChangeLog

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/xslt-process/ChangeLog.gz
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
