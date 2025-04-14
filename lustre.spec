# TODO:
# - finish kernel part (for 5.15? not ready for 6.x)
# - subpackages for resource-agents, mount_osd modules, snmp agent
#
# Conditional build:
%bcond_with	kernel		# kernel modules (supported: 3.10+patches, 4.12+patches, 4.14+patches, 4.18+patches, 5.3, 5.14)
%bcond_with	kerberos5	# KRB5/GSS support (build fails with heimdal 7.8)
%bcond_with	tests		# build tests
%bcond_without	userspace	# userspace tools

%if %{without userspace}
%undefine	with_tests
%endif
Summary:	Linux kernel modules for Lustre(R) file system
Summary(en.UTF-8):	Linux kernel modules for Lustre® file system
Summary(pl.UTF-8):	Moduły jądra Linuksa dla systemu plików Lustre®
Name:		lustre
Version:	2.15.4
# commit hash taken from tag at https://git.whamcloud.com/?p=fs/lustre-release.git;a=summary
%define	gitref	cac870cf4d2bd9905b1b2bbe563defe6d748ac94
%define	shortref	%(echo %{gitref} | cut -c1-7)
Release:	0.1
License:	GPL v2
Group:		Base/Kernel
Source0:	https://git.whamcloud.com/?p=fs/lustre-release.git;a=snapshot;h=%{gitref};sf=tgz#/%{name}-%{version}.tar.gz
# Source0-md5:	346030ff22e4187a9fdc2ca26424f0ee
Patch0:		%{name}-format.patch
Patch1:		%{name}-snmp.patch
Patch2:		%{name}-32bit.patch
Patch3:		%{name}-tests.patch
Patch4:		%{name}-link.patch
Patch5:		%{name}-configure.patch
Patch6:		%{name}-zfs.patch
Patch7:		%{name}-heimdal.patch
URL:		https://www.lustre.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.10
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libtool >= 2:2
BuildRequires:	rpmbuild(macros) >= 1.379
%if %{with kernel}
BuildRequires:	kernel%{_alt_kernel}-module-build
%endif
%if %{with userspace}
BuildRequires:	keyutils-devel
%{?with_kerberos5:BuildRequires:	krb5-devel}
BuildRequires:	libmount-devel
BuildRequires:	libnl-devel >= 3.1
BuildRequires:	libselinux-devel
BuildRequires:	net-snmp-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.6
BuildRequires:	swig >= 2.0
BuildRequires:	swig-python >= 2.0
BuildRequires:	yaml-devel
BuildRequires:	zlib-devel
%endif
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# conflicts for kernel
%define		filterout_c	-fomit-frame-pointer

%description
Lustre(R) is a high-performance, multi-network, fault-tolerant,
POSIX1-compliant network file system for Linux clusters. Lustre(R) is
a complete, software-only, open-source solution for any hardware that
can run Linux. It has native drivers for many of the fastest
networking fabrics. Lustre(R) can use any storage medium that looks
like a block device.

%description -l en.UTF-8
Lustre® is a high-performance, multi-network, fault-tolerant,
POSIX1-compliant network file system for Linux clusters. Lustre® is a
complete, software-only, open-source solution for any hardware that
can run Linux. It has native drivers for many of the fastest
networking fabrics. Lustre® can use any storage medium that looks like
a block device.

%description -l pl.UTF-8
Lustre® jest wysoko wydajnym, wielosieciowym, odpornym na awarie i
zgodnym z POSIX1 sieciowym systemem plików dla klastrów linuksowych.
Lustre® jest kompletnym, wyłącznie programowym, open-source'owym
rozwiazaniem dla każdego sprzętu, który pracuje pod Linuxem. Posiada
natywne sterowniki dla wielu najszybszych sieci. Lustre® może używać
każdego medium, które zachowuje się jak urządzenie blokowe.

%package iokit
Summary:	Benchmark tools for a cluster with the Lustre file system
Summary(pl.UTF-8):	Narzędzia testujące wydajność klastra z systemem plików Lustre
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description iokit
Benchmark tools for a cluster with the Lustre file system.

%description iokit -l pl.UTF-8
Narzędzia testujące wydajność klastra z systemem plików Lustre.

%package libs
Summary:	Lustre shared libraries
Summary(pl.UTF-8):	Biblioteki współdzielone Lustre
Group:		Libraries

%description libs
Lustre shared libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone Lustre.

%package devel
Summary:	Header files for Lustre libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Lustre
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	yaml-devel

%description devel
Header files for Lustre libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Lustre.

%package static
Summary:	Lustre static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Lustre
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Lustre static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Lustre.

%package -n kernel%{_alt_kernel}-lustre
Summary:	Linux kernel modules for Lustre(R) file system
Summary(en.UTF-8):	Linux kernel modules for Lustre® file system
Summary(pl.UTF-8):	Moduły jądra Linuksa dla systemu plików Lustre®
Group:		Base/Kernel

%description -n kernel%{_alt_kernel}-lustre
Linux kernel modules for Lustre(R). Lustre(R) is a high-performance,
multi-network, fault-tolerant, POSIX1-compliant network file system
for Linux clusters. Lustre(R) is a complete, software-only,
open-source solution for any hardware that can run Linux. It has
native drivers for many of the fastest networking fabrics. Lustre(R)
can use any storage medium that looks like a block device.

%description -n kernel%{_alt_kernel}-lustre -l en.UTF-8
Linux kernel modules for Lustre®. Lustre® is a high-performance,
multi-network, fault-tolerant, POSIX1-compliant network file system
for Linux clusters. Lustre® is a complete, software-only, open-source
solution for any hardware that can run Linux. It has native drivers
for many of the fastest networking fabrics. Lustre® can use any
storage medium that looks like a block device.

%description -n kernel%{_alt_kernel}-lustre -l en.UTF-8 -l pl.UTF-8
Moduły jądra Linuksa dla Lustre®. Lustre® jest wysoko wydajnym,
wielosieciowym, odpornym na awarie i zgodnym z POSIX1 sieciowym
systemem plików dla klastrów linuksowych. Lustre® jest kompletnym,
wyłącznie programowym, open-source'owym rozwiazaniem dla każdego
sprzętu, który pracuje pod Linuxem. Posiada natywne sterowniki dla
wielu najszybszych sieci. Lustre® może używać każdego medium,
które zachowuje się jak urządzenie blokowe.

%prep
%setup -q -n %{name}-release-%{shortref}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1

%{__sed} -i -e '1s,/usr/bin/env python3$,%{__python3},' lustre/scripts/zfsobj2fid

%build
%{__libtoolize}
%{__aclocal} -I config -I libcfs/autoconf -I lnet/autoconf -I lustre/autoconf -I snmp/autoconf
%{__autoconf}
%{__autoheader}
%{__automake}
%if %{with userspace}
CPPFLAGS="%{rpmcppflags} -I$(pwd)/lnet/include/uapi -I$(pwd)/lustre/include/uapi -DHAVE_HEIMDAL"
%endif
%configure \
	%{!?with_userspace:--disable-doc} \
	%{!?with_kernel:--disable-modules} \
	%{!?with_userspace:--disable-manpages} \
	%{!?with_tests:--disable-tests} \
	%{!?with_userspace:--disable-utils} \
	--with-bash-completion-dir=%{bash_compdir} \
	--with-linux-obj=%{_kernelsrcdir} \
	--with-systemdsystemunitdir=%{systemdunitdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	agentdir=%{_libdir}/snmp \
	mibdir=%{_datadir}/mibs

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.la

%{__rm} $RPM_BUILD_ROOT%{_libdir}/snmp/liblustresnmp.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MAINTAINERS README lustre/{BUGS,ChangeLog}
%attr(755,root,root) /sbin/mount.lustre
%attr(755,root,root) /sbin/mount.lustre_tgt
%attr(755,root,root) %{_bindir}/lfs
%attr(755,root,root) %{_bindir}/lfs_migrate
%attr(755,root,root) %{_bindir}/llobdstat
%attr(755,root,root) %{_bindir}/llstat
%attr(755,root,root) %{_bindir}/lustre_req_history
%attr(755,root,root) %{_bindir}/plot-llstat
%attr(755,root,root) %{_sbindir}/ko2iblnd-probe
%attr(755,root,root) %{_sbindir}/ksocklnd-config
%attr(755,root,root) %{_sbindir}/mkfs.lustre
%attr(755,root,root) %{_sbindir}/l_foreign_symlink
%attr(755,root,root) %{_sbindir}/l_getidentity
%attr(755,root,root) %{_sbindir}/l_getsepol
%attr(755,root,root) %{_sbindir}/l_tunedisk
%attr(755,root,root) %{_sbindir}/lc_cluman
%attr(755,root,root) %{_sbindir}/lc_hb
%attr(755,root,root) %{_sbindir}/lc_lvm
%attr(755,root,root) %{_sbindir}/lc_md
%attr(755,root,root) %{_sbindir}/lc_modprobe
%attr(755,root,root) %{_sbindir}/lc_mon
%attr(755,root,root) %{_sbindir}/lc_net
%attr(755,root,root) %{_sbindir}/lc_servip
%attr(755,root,root) %{_sbindir}/lctl
%attr(755,root,root) %{_sbindir}/ldev
%attr(755,root,root) %{_sbindir}/ldlm_debug_upcall
%attr(755,root,root) %{_sbindir}/lhbadm
%attr(755,root,root) %{_sbindir}/lhsmtool_posix
%attr(755,root,root) %{_sbindir}/ll_decode_filter_fid
%attr(755,root,root) %{_sbindir}/ll_decode_linkea
%attr(755,root,root) %{_sbindir}/llog_reader
%attr(755,root,root) %{_sbindir}/llsom_sync
%attr(755,root,root) %{_sbindir}/llverdev
%attr(755,root,root) %{_sbindir}/llverfs
%attr(755,root,root) %{_sbindir}/lnet
%attr(755,root,root) %{_sbindir}/lnetctl
%attr(755,root,root) %{_sbindir}/lr_reader
%attr(755,root,root) %{_sbindir}/lshowmount
%attr(755,root,root) %{_sbindir}/lst
%attr(755,root,root) %{_sbindir}/lustre_rmmod
%attr(755,root,root) %{_sbindir}/lustre_routes_config
%attr(755,root,root) %{_sbindir}/lustre_routes_conversion
%attr(755,root,root) %{_sbindir}/lustre_rsync
%attr(755,root,root) %{_sbindir}/lustre_start
%attr(755,root,root) %{_sbindir}/ofd_access_log_reader
%attr(755,root,root) %{_sbindir}/routerstat
%attr(755,root,root) %{_sbindir}/tunefs.lustre
%dir %{_libdir}/lustre
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ldev.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lnet.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lnet_routes.conf
%config(noreplace) %verify(not md5 mtime size) /etc/modprobe.d/ko2iblnd.conf
%config(noreplace) %verify(not md5 mtime size) /etc/udev/rules.d/99-lustre.rules
%config(noreplace) %verify(not md5 mtime size) /etc/udev/rules.d/99-lustre-server.rules
%{systemdunitdir}/lnet.service
%{bash_compdir}/lctl
%{bash_compdir}/lfs
%{bash_compdir}/lustre
%{_mandir}/man1/lfs.1*
%{_mandir}/man1/lfs-*.1*
%{_mandir}/man1/lfs_migrate.1*
%{_mandir}/man5/ldev.conf.5*
%{_mandir}/man5/nids.5*
%{_mandir}/man7/lustre.7*
%{_mandir}/man8/l_getidentity.8*
%{_mandir}/man8/l_getsepol.8*
%{_mandir}/man8/lctl.8*
%{_mandir}/man8/lctl-*.8*
%{_mandir}/man8/ldev.8*
%{_mandir}/man8/lhbadm.8*
%{_mandir}/man8/ll_decode_filter_fid.8*
%{_mandir}/man8/ll_decode_linkea.8*
%{_mandir}/man8/llobdstat.8*
%{_mandir}/man8/llog_reader.8*
%{_mandir}/man8/llsom_sync.8*
%{_mandir}/man8/llstat.8*
%{_mandir}/man8/llverdev.8*
%{_mandir}/man8/lnetctl.8*
%{_mandir}/man8/lshowmount.8*
%{_mandir}/man8/lst.8*
%{_mandir}/man8/lustre_routes_config.8*
%{_mandir}/man8/lustre_routes_conversion.8*
%{_mandir}/man8/lustre_rsync.8*
%{_mandir}/man8/mkfs.lustre.8*
%{_mandir}/man8/mount.lustre.8*
%{_mandir}/man8/mount.lustre_tgt.8*
%{_mandir}/man8/plot-llstat.8*
%{_mandir}/man8/routerstat.8*
%{_mandir}/man8/tunefs.lustre.8*
%if %{with kerberos5}
%attr(755,root,root) %{_sbindir}/l_idmap
%attr(755,root,root) %{_sbindir}/lgss_keyring
%attr(755,root,root) %{_sbindir}/lgss_sk
%attr(755,root,root) %{_sbindir}/lgssd
%attr(755,root,root) %{_sbindir}/lsvcgssd
%{_mandir}/man8/lgss_sk.8*
%endif

# resource-agents
%attr(755,root,root) /etc/ha.d/resource.d/Lustre.ha_v2
%dir %{_prefix}/lib/ocf/resource.d/lustre
%{_prefix}/lib/ocf/resource.d/lustre/Lustre
%{_prefix}/lib/ocf/resource.d/lustre/healthLNET
%{_prefix}/lib/ocf/resource.d/lustre/healthLUSTRE
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/lustre
%endif
%attr(755,root,root) %{_libexecdir}/lustre/haconfig
%{_libexecdir}/lustre/lc_common

# osd-ldiskfs-mount
%attr(755,root,root) %{_libdir}/lustre/mount_osd_ldiskfs.so

# osd-zfs-mount
%attr(755,root,root) %{_sbindir}/zfsobj2fid
%attr(755,root,root) %{_libdir}/lustre/mount_osd_zfs.so
%attr(755,root,root) /etc/zfs/zed.d/statechange-lustre.sh
%attr(755,root,root) /etc/zfs/zed.d/vdev_attach-lustre.sh
%attr(755,root,root) /etc/zfs/zed.d/vdev_clear-lustre.sh
%attr(755,root,root) /etc/zfs/zed.d/vdev_remove-lustre.sh

# snmp
%attr(755,root,root) %{_libdir}/snmp/liblustresnmp.so*
%{_datadir}/mibs/Lustre-MIB.txt

%files iokit
%defattr(644,root,root,755)
%doc lustre-iokit/{AUTHORS,README} lustre-iokit/ior-survey/README.ior-survey lustre-iokit/mds-survey/README.mds-survey lustre-iokit/obdfilter-survey/README.obdfilter-survey lustre-iokit/ost-survey/README.ost-survey lustre-iokit/sgpdd-survey/README.sgpdd-survey lustre-iokit/stats-collect/README.iokit-lstats
%attr(755,root,root) %{_bindir}/iokit-config
%attr(755,root,root) %{_bindir}/iokit-gather-stats
%attr(755,root,root) %{_bindir}/iokit-libecho
%attr(755,root,root) %{_bindir}/iokit-lstats
%attr(755,root,root) %{_bindir}/iokit-parse-ior
%attr(755,root,root) %{_bindir}/iokit-plot-obdfilter
%attr(755,root,root) %{_bindir}/iokit-plot-ost
%attr(755,root,root) %{_bindir}/iokit-plot-sgpdd
%attr(755,root,root) %{_bindir}/ior-survey
%attr(755,root,root) %{_bindir}/mds-survey
%attr(755,root,root) %{_bindir}/obdfilter-survey
%attr(755,root,root) %{_bindir}/ost-survey
%attr(755,root,root) %{_bindir}/sgpdd-survey

%if %{with tests}
%files tests
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/wirecheck
%attr(755,root,root) %{_sbindir}/wiretest
# TODO: permissions
%{_libdir}/lustre/tests
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblnetconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblnetconfig.so.4
%attr(755,root,root) %{_libdir}/liblustreapi.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblustreapi.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblnetconfig.so
%attr(755,root,root) %{_libdir}/liblustreapi.so
%{_libdir}/libiam.a
%{_includedir}/linux/lnet
%{_includedir}/linux/lustre
%{_includedir}/lustre
%{_pkgconfigdir}/lustre.pc
%{_mandir}/man3/llapi_*.3*
%{_mandir}/man7/llapi_layout.7*
%{_mandir}/man7/lustreapi.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/liblnetconfig.a
%{_libdir}/liblustreapi.a
