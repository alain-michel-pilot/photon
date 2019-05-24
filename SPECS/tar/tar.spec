Summary:	Archiving program
Name:		tar
Version:	1.29
Release:	3%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/tar
Group:		Applications/System
Vendor:		VMware, Inc.
Distribution: 	Photon
Source0:	tar/%{name}-%{version}.tar.xz
%define sha1 tar=03851c34c90f0656177f2dd375cd61bd1204c51d
Patch0:		tar-CVE-2019-9923.patch
Patch1:		tar-CVE-2018-20482.patch
%description
Contains GNU archiving program
%prep
%setup -q
%patch0 -p1
%patch1 -p1
%build
autoreconf -i --force
FORCE_UNSAFE_CONFIGURE=1  ./configure \
	--prefix=%{_prefix} \
	--bindir=/bin \
	--disable-silent-rules
make %{?_smp_mflags}
%install
install -vdm 755 %{buildroot}%{_sbindir}
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} -C doc install-html docdir=%{_defaultdocdir}/%{name}-%{version}
install -vdm 755 %{buildroot}/usr/share/man/man1 
rm -rf %{buildroot}%{_infodir}
%find_lang %{name}
%check
make  %{?_smp_mflags} check
%files -f %{name}.lang
%defattr(-,root,root)
/bin/tar
%{_libexecdir}/rmt
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/*/*
%changelog
*       Thu May 23 2019 Keerthana K <keerthanak@vmware.com> 1.29-3
-       Fix CVE-2018-20482
*	Tue Apr 23 2019 Siju Maliakkal <smaliakkal@vmware.com> 1.29-2
-	Fix for CVE-2019-9923
*       Tue Apr 11 2017 Vinay Kulkarni <kulkarniv@vmware.com> 1.29-1
-       Update to version 1.29.
*       Mon Oct 10 2016 ChangLee <changlee@vmware.com> 1.28-3
-       Modified %check
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.28-2
-	GA - Bump release of all rpms
*	Wed Jan 20 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.28-1
-	Update to 1.28-1.
*	Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 1.27.1-1
-	Initial build.	First version
