Summary:	Exfoliation Nagios theme
Name:		nagios-theme-exfoliation
Version:	4.5.9
Release:	1
License:	GPL v2+
Group:		Applications/WWW
# https://www.nagios.org/downloads/nagios-core/thanks/?product_download=nagioscore-source
Source0:	https://assets.nagios.com/downloads/nagioscore/releases/nagios-%{version}.tar.gz
# Source0-md5:	dea21ad245e301fb05d3e8408499e001
Patch0:		system-jquery.patch
Patch1:		remove-information-leak.patch
URL:		http://lancet.mit.edu/mwall/projects/nagios/exfoliation.html
BuildRequires:	sed >= 4.0
Requires:	jquery >= 3.7.1
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
cd nagios-%{version}
%patch -P0 -p1
%patch -P1 -p1
cd ..
mv nagios-%{version}/contrib/exfoliation/* .
# need some files from nagios tarball the way themes are made
mv nagios-%{version}/html .

%{__sed} -e '
	s#@cgiurl@#/nagios/cgi-bin#
	s#@localstatedir@#/var/lib/nagios#

	/cgi_config_file/  s#@sysconfdir@#/''etc/webapps/nagios#
	/main_config_file/ s#@sysconfdir@#/''etc/nagios#

' html/config.inc.php.in > html/config.inc.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{htmldir}

# keep synced with install-exfoliation Makefile.in target

# base files, not present in the exfoliation
cp -a html/*.php html/includes html/images html/stylesheets $RPM_BUILD_ROOT%{htmldir}

# @COREWINDOW@ doesn't need to be expanded here for us
cp -a html/index.php.in $RPM_BUILD_ROOT%{htmldir}/index.php

# overwrite changed theme files since some files from base are still needed (ex nag_funcs.css)
cp -a images/* $RPM_BUILD_ROOT%{htmldir}/images/
cp -a stylesheets/* $RPM_BUILD_ROOT%{htmldir}/stylesheets/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{htmldir}/*.php
%{htmldir}/includes/*
%{htmldir}/images/*
%exclude %{htmldir}/images/favicon.ico
%{htmldir}/stylesheets/*
