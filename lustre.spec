#TODO Some kernel specialists has to make it build
Summary:	Kernel modules for Lustre®
Summary(pl.UTF-8):	Moduły kernela dla Lustre®
Name:		lustre
Version:	1.6.4.1
Release:	0.1
License:	GPL v2
Group:		Base/Kernel
Source0:	http://www.clusterfs.com/downloads/public/Lustre/v1.6/Production/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e9d383eb48f6d41ff1a2dce4ae474415
##Requires:	-kernel with lustre compiled in
URL:		http://www.clusterfs.com/scalable-storage.html
BuildRequires:	kernel%{_alt_kernel}-module-build
BuildRequires:	rpmbuild(macros) >= 1.379
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kernel modules for Lustre® Lustre® is a high-performance,
multi-network, fault-tolerant, POSIX1-compliant network file system
for Linux clusters. Lustre® is a complete, software-only, open-source
solution for any hardware that can run Linux. It has native drivers
for many of the fastest networking fabrics. Lustre® can use any
storage medium that looks like a block device.

%description -l pl.UTF-8
Moduły kernela dla Lustre®. Lustre® jest wysoko wydajnym,
wielosieciowym, odpornym na awarie zgodnym z POSIX1 sieciowym systemem
plików dla klastrów Linuxowych. Lustre® jest kompletnym,
wyłącznie programowym, open-source'owym rozwiazaniem dla każdego
sprzętu który pracuje pod Linuxem. Posiada natywne sterowniki dla
wielu najszybszych sieci. Lustre® może używać każdego madium
które zachowuje się jak urządzenie blokowe.

%prep
%setup -q

%build
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
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
