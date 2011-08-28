Summary:	An Etherpad based on node.js
Name:		etherpad-lite
Version:	1.0
Release:	0.1
License:	Apache v2.0
Group:		Applications/WWW
URL:		https://github.com/Pita/etherpad-lite
Source0:	https://github.com/Pita/etherpad-lite/tarball/1.0#/%{name}-%{version}.tar.gz
# Source0-md5:	-
Requires:	nodejs >= 0.5.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An Etherpad based on node.js

%prep
%setup -qc
# for githug urls:
mv *-%{name}-*/* .

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
