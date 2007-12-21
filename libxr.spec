%define major 0
%define libname %mklibname xr %{major}
%define develname %mklibname xr -d

Summary:	Cross-platform XML-RPC client/server library written in C
Name:		libxr
Version:	0.9.15
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://oss.zonio.net/libxr.htm
Source0:	http://oss.zonio.net/releases/libxr/libxr-%{version}.tar.bz2
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	libglib2-devel	>= 2.12.0
BuildRequires:	libxml2-devel	>= 2.6.20
BuildRequires:	openssl-devel	>= 0.9.8e
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

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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
%doc AUTHORS COPYING NEWS README TODO
%{_includedir}/libxr/*.h
%{_libdir}/libxr.a
%{_libdir}/libxr.la
%{_libdir}/libxr.so
%{_libdir}/pkgconfig/libxr.pc
