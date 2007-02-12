Summary:	Interactive spelling corrector with GNU xslt-process
Summary(pl.UTF-8):   Interaktywny korektor pisowni używający GNU xslt-process-a
Name:		xemacs-xslt-process-pkg
%define		srcname	xslt-process
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	30273cbe2e90ae703ea410879412e68b
URL:		http://www.xemacs.org/
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xslt-process
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Interactive spelling corrector with GNU xslt-process.

%description -l pl.UTF-8
Interaktywny korektor pisowni używający GNU xslt-process-a.

%prep
%setup -q -c

#%build
#xemacs -batch -q -no-site-file -f batch-byte-compile lisp/xslt-process/xslt-process.el

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/xslt-process/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
