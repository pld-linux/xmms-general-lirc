Summary:	LIRC (Linux Infrared  Remote Control) plugin for XMMS
Summary(pl):	Wtyczka LIRC (Zdalna kontrola Linuksa za pomoc± podczerwieni) dla XMMS
Name:		xmms-general-lirc
Version:	1.2
Release:	5
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	ftp://ftp.xmms.org/xmms/plugins/lirc-xmms/lirc-xmms-plugin-%{version}.tar.gz
# Source0-md5:	d268886f9b26aba7e29e04569322668c
Patch0:		%{name}-ac.patch
URL:		http://www.xmms.org/plugins.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libtool
BuildRequires:	lirc-devel >= 0.6.0
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows to control xmms using LIRC (Linux Infrared Remote
Control).

%description -l pl
Ta wtyczka pozwala na zdaln± kontrolê xmms-a za pomoc± LIRC.

%prep
%setup -q -n lirc-xmms-plugin-%{version}
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog lircrc
%attr(755,root,root) %{xmms_general_plugindir}/*.so
%{xmms_general_plugindir}/*.la
