Summary:	LIRC (Linux Infrared  Remote Control) plugin for XMMS
Summary(pl):	Wtyczka LIRC (Zdalna kontrola Linuksa za pomoc± podczerwieni) dla XMMS
Name:		xmms-general-lirc
Version:	1.2
Release:	4
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.xmms.org/xmms/plugins/lirc-xmms/lirc-xmms-plugin-%{version}.tar.gz
Patch0:		%{name}-ac.patch
URL:		http://www.xmms.org/plugins.html
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	lirc-devel >= 0.6.0
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
This plugin allows to control xmms using LIRC (Linux Infrared Remote
Control).

%description -l pl
Ta wtyczka pozwala na zdaln± kontrolê xmms'a za pomoc± LIRC.

%prep
%setup -q -n lirc-xmms-plugin-%{version}
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
autoheader
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog lircrc
%attr(755,root,root) %{_libdir}/xmms/General/*.so
%attr(755,root,root) %{_libdir}/xmms/General/*.la
