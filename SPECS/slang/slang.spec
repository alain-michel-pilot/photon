Summary:	An interpreted language that may be embedded into an application to make the application extensible.
Name:		slang
Version:	2.3.1a
Release:	2%{?dist}
License:	GNU General Public License
URL:		http://www.jedsoft.org/slang/index.html
Group:		Development/Languages
Source0:	http://www.jedsoft.org/releases/%{name}/old/%{name}-%{version}.tar.bz2
%define sha1 slang=a8ea7f1b5736160a94efb67b137a0f5b9916bdf2
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	readline-devel

%description
S-Lang is a multi-platform programmer's library designed to allow a developer to create robust multi-platform software. It provides facilities required by interactive applications such as display/screen management, keyboard input, keymaps, and so on. The most exciting feature of the library is the slang interpreter that may be easily embedded into a program to make it extensible. While the emphasis has always been on the embedded nature of the interpreter, it may also be used in a stand-alone fashion through the use of slsh, which is part of the S-Lang distribution.

Unlike many interpreters, the S-Lang interpreter supports all of the native C integer types (signed and unsigned versions of char, short, int, long, and long long), and both single and double precision types, as well as a double precision complex type. Other data types supported by the interpreter include strings, lists, associative arrays (hashes), user-defined structures, and multi-dimensional arrays of any data-type.

The S-Lang interpreter has very strong support for array-based operations making it ideal for numerical applications.

%package	devel
Summary:	Header and development files for ncurses
Requires:	%{name} = %{version}

%description	devel
It contains the libraries and header files to create applications 

%prep
%setup -q -n %{name}-%{version}

%build
./configure --prefix=%{_prefix} \
            --sysconfdir=%{_sysconfdir} \
            --with-readline=gnu
make -j1

%install
make DESTDIR=%{buildroot} install_doc_dir=%{_docdir}/slang-%{version}   \
     SLSH_DOC_DIR=%{_docdir}/slang-%{version}/slsh \
     install-all

chmod -v 755 %{buildroot}%{_libdir}/libslang.so.2.3.1 \
             %{buildroot}%{_libdir}/slang/v2/modules/*.so

%check
sed -i "s|test_misc ();|%test_misc ();|g" src/test/posixio.sl
make  check

%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_libdir}/slang/*
%{_libdir}/libslang.so.2*
%{_bindir}/*
%{_datadir}/*

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/libslang.so
%{_libdir}/pkgconfig/*.pc

%changelog
*       Wed Aug 02 2017 Chang Lee <changlee@vmware.com> 2.3.1a-2
-       Skipped %check test cases for pseudo terminal-/dev/pts/*
*       Thu Apr 13 2017 Vinay Kulkarni <kulkarniv@vmware.com> 2.3.1a-1
-       Update to version 2.3.1a
*       Tue Oct 04 2016 ChangLee <changlee@vmware.com> 2.3.0-3
-       Modified %check
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.3.0-2
-	GA - Bump release of all rpms
*   	Wed Jan 20 2016 Anish Swaminathan <anishs@vmware.com> 2.3.0-1
-   	Upgrade version.
*	Tue Oct 27 2015 Mahmoud Bassiouny <mbassiouny@vmware.com> 2.2.4-1
-	Initial build.	First version
