Summary: Default GTK+ theme engines
Name: gtk2-engines
Version: 2.20.2
Release: 1
License: GPL
Group: X11/Libraries
Source: gtk-engines-%{version}.tar.gz
URL: ftp://ftp.gnome.org/pub/GNOME/sources/gtk-engines/
BuildRoot:/var/tmp/gtk-engines-%{PACKAGE_VERSION}-root

%description
These are the graphical engines for the various GTK+ toolkit themes.

%prep
%setup -n gtk-engines-%{version}

%build
# Needed for snapshot releases.
if [ ! -f configure ]; then
 ./autogen.sh
fi

%configure

if [ "$SMP" != "" ]; then
  make -j$SMP "MAKE=make -j$SMP"
else
  make
fi

%install

rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT

%makeinstall
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jan 17 2003 Owen Taylor <otaylor@redhat.com>
- Various fixes to good RPM practice

* Thu Oct 22 2002 Christian F.K. Schaller <Uraeus@gnome.org>
- Update SPEC file to include latest stuff 
- work on RH8

* Fri Nov 20 1998 Michael Fulbright <drmike@redhat.com>

- First try at a spec file

%files
%defattr(-, root, root)
%doc COPYING README NEWS ChangeLog
%{_datadir}/themes
%{_libdir}/gtk-2.0/2.10.0/engines/*.so
%{_libdir}/pkgconfig

