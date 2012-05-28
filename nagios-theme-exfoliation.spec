Summary:	Exfoliation Nagios theme
Name:		nagios-theme-exfoliation
Version:	3.4.1
Release:	1
License:	GPL v2+
Group:		Applications/WWW
Source0:	http://downloads.sourceforge.net/nagios/nagios-%{version}.tar.gz
# Source0-md5:	2fa8acfb2a92b1bf8d173a855832de1f
Patch0:		system-jquery.patch
Patch1:		system-magpierss.patch
URL:		http://lancet.mit.edu/mwall/projects/nagios/exfoliation.html
BuildRequires:	sed >= 4.0
Requires:	nagios-cgi >= 3.4.1-0.8
Requires:	webserver(php)
Provides:	nagios-theme
Obsoletes:	nagios-theme
#Obsoletes:	nagios-theme-default < 3.3.1-1.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		htmldir		/usr/share/nagios

%description
Exfoliation is a simple makeover for the Nagios Core web interface.

%prep
%setup -qc
cd nagios
%patch0 -p1
%patch1 -p1
cd ..
mv nagios/contrib/exfoliation/* .
# need some files from nagios tarball the way themes are made
mv nagios/html .

%{__sed} -e '
	s#@cgiurl@#/nagios/cgi-bin#
	s#@localstatedir@#/var/lib/nagios#

	/cgi_config_file/  s#@sysconfdir@#/''etc/webapps/nagios#
	/main_config_file/ s#@sysconfdir@#/''etc/nagios#

' html/config.inc.php.in > html/config.inc.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{htmldir}

# base files, not present in the exfoliation
cp -a html/*.php html/includes $RPM_BUILD_ROOT%{htmldir}

# copy theme files
cp -a images stylesheets $RPM_BUILD_ROOT%{htmldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{htmldir}/*.php
%{htmldir}/includes/*
%{htmldir}/images/*
%exclude %{htmldir}/images/favicon.ico
%{htmldir}/stylesheets/*
