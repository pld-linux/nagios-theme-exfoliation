Summary:	Exfoliation Nagios theme
Name:		nagios-theme-exfoliation
Version:	0.7
Release:	0.10
License:	GPL v2+
Group:		Applications/WWW
Source0:	http://lancet.mit.edu/mwall/projects/nagios/exfoliation-%{version}.tgz
# Source0-md5:	0398a7c560450906ba85c0638c17651b
URL:		http://lancet.mit.edu/mwall/projects/nagios/exfoliation.html
BuildRequires:	sed >= 4.0
Requires:	nagios-cgi >= 2.0-0.b3.31
Provides:	nagios-theme
Obsoletes:	nagios-theme
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/webapps/nagios
%define		htmldir		/usr/share/nagios

%description
Exfoliation is a simple makeover for the Nagios Core web interface.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{htmldir}

# copy theme files
cp -a images stylesheets $RPM_BUILD_ROOT%{htmldir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{htmldir}/images/*
%exclude %{htmldir}/images/favicon.ico
%{htmldir}/stylesheets/*
