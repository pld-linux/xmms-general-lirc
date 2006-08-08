Summary:	LIRC (Linux Infrared Remote Control) plugin for XMMS
Summary(pl):	Wtyczka LIRC (Zdalne sterowanie Linuksem za pomoc± podczerwieni) dla XMMS-a
Name:		xmms-general-lirc
Version:	1.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/lirc/lirc-xmms-plugin-%{version}.tar.gz
# Source0-md5:	06bf5f4d1f1c1a310ebf04184aba4da1
Patch0:		%{name}-ac.patch
URL:		http://sourceforge.net/projects/lirc/
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
This plugin allows to control XMMS using LIRC (Linux Infrared Remote
Control).

%description -l pl
Ta wtyczka pozwala na zdalne sterowanie XMMS-em za pomoc± LIRC.

%prep
%setup -q -n lirc-xmms-plugin-%{version}
%patch0 -p1

%build
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

rm -f $RPM_BUILD_ROOT%{xmms_general_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog lircrc
%attr(755,root,root) %{xmms_general_plugindir}/*.so
