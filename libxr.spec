%define major 1
%define libname %mklibname xr %{major}
%define develname %mklibname xr -d

Summary:	Cross-platform XML-RPC client/server library written in C
Name:		libxr
Version:	1.0
Release:	%mkrel 3
License:	LGPLv2+
Group:		System/Libraries
Url:		http://oss.zonio.net/libxr.htm
Source0:	http://oss.zonio.net/releases/libxr/libxr-%{version}.tar.bz2
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libglib2-devel	>= 2.12.0
BuildRequires:	pkgconfig(libxml-2.0)	>= 2.6.20
BuildRequires:	openssl-devel	>= 0.9.8e
BuildRequires:	re2c
Requires:	%{libname} = %{version}-%{release}
Requires:	%{develname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Cross-platform XML-RPC client/server library written in C that supports 
persistent HTTP/1.1 conenctions over SSL and comes with XML-RPC interface 
description language and client/server code compiler.

Features:

- Persistent connections over HTTP/1.1
- SSLv3/TLSv1 using OpenSSL.
- XML-RPC interface description language (XDL).
- XML-RPC client stubs/servlet skels compiler.
- Multiple servlets per server.
- Servlet lifetime (init -- call -- call -- fini).
- Multiplatform (linux, mingw32 on windows).
- IPV6 as soon as OpenSSL 0.9.9 is released.

%package -n %{libname}
Summary:	Main library for libxr
Group:		System/Libraries
Obsoletes:	%mklibname xr 0

%description -n %{libname}
Main library for libxr.

%package -n %{develname}
Summary:	Development files for libxr
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%mklibname %{name} 0 -d

%description -n %{develname}
Development files for libxr.

%prep
%setup -q

%build
%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xdl-compiler
%{_mandir}/man1/xdl-compiler.*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxr.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS NEWS README TODO
%{_includedir}/libxr/*.h
%{_libdir}/libxr.a
%{_libdir}/libxr.so
%{_libdir}/pkgconfig/libxr.pc


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-3mdv2011.0
+ Revision: 609790
- rebuild

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 1.0-2mdv2010.1
+ Revision: 536656
- rebuild

* Sun Jan 24 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0-1mdv2010.1
+ Revision: 495552
- update to new version 1.0

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.9.97-2mdv2010.0
+ Revision: 439515
- rebuild

* Fri Oct 17 2008 Funda Wang <fwang@mandriva.org> 0.9.97-1mdv2009.1
+ Revision: 294572
- New version 0.9.97

* Sat Oct 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.96-1mdv2009.1
+ Revision: 292490
- update to new version 0.9.96

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.9.94-2mdv2009.0
+ Revision: 268080
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.94-1mdv2009.0
+ Revision: 194454
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.9.15-2mdv2008.1
+ Revision: 109221
- rebuild for new lzma

* Wed Oct 31 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.15-1mdv2008.1
+ Revision: 104043
- new version

* Tue Oct 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.14-1mdv2008.1
+ Revision: 96164
- new version
- new license policy

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

* Fri Jun 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.10-3mdv2008.0
+ Revision: 43166
- fix requires

* Tue Jun 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.10-2mdv2008.0
+ Revision: 41623
- new devel library policy

* Sat May 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.10-1mdv2008.0
+ Revision: 28410
- new version

* Mon Apr 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.8-2mdv2008.0
+ Revision: 17558
- set requires on subpackages

* Mon Apr 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.8-1mdv2008.0
+ Revision: 17318
- add missing buildrequires
- Import libxr

