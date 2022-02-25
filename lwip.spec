%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.3
Release: 2
License: BSD
URL:     http://savannah.nongnu.org/projects/lwip/
Source0: http://download.savannah.nongnu.org/releases/lwip/%{name}-%{version}.tar.gz

Patch9000:  0001-add-makefile.patch
Patch9001:  0002-adapt-lstack.patch
Patch9002:  0003-fix-the-occasional-coredump-when-the-lwip-exits.patch
Patch9003:  0004-fix-error-of-deleting-conn-table-in-connect.patch
Patch9004:  0005-syn-rcvd-state-reg-conn-into-conntable.patch
Patch9005:  0006-fix-coredump-in-etharp.patch
Patch9006:  0007-gazelle-fix-epoll_ctl-EPOLLET-mode-error.patch
Patch9007:  0008-gazelle-fix-lwip_accept-memcpy-sockaddr-large.patch
Patch9008:  0009-fix-stack-buffer-overflow-when-memcpy-addr.patch
Patch9009:  0010-fix-the-incomplete-release-of-the-conntable.patch
Patch9010:  0011-remove-gazelle-tcp-conn-func.patch
Patch9011:  0012-fix-incomplete-resource-release-in-lwip-close.patch
Patch9012:  0013-remove-gazelle-syscall-thread.patch
Patch9013:  0014-fix-some-compile-errors.patch
Patch9014:  0015-fix-tcp-port-alloc-issue.patch

BuildRequires: gcc-c++ dos2unix dpdk-devel

#Requires: 

ExclusiveArch: x86_64 aarch64

%description
lwip is a small independent implementation of the TCP/IP protocol suite.

%prep
%setup -n %{name}-%{version} -q
find %{_builddir}/%{name}-%{version} -type f -exec dos2unix -q {} \;

%patch9000 -p1
%patch9001 -p1
%patch9002 -p1
%patch9003 -p1
%patch9004 -p1
%patch9005 -p1
%patch9006 -p1
%patch9007 -p1
%patch9008 -p1
%patch9009 -p1
%patch9010 -p1
%patch9011 -p1
%patch9012 -p1
%patch9013 -p1
%patch9014 -p1

%build
cd %{_builddir}/%{name}-%{version}/src
%make_build

%install
cd %{_builddir}/%{name}-%{version}/src
%make_install

%files
%defattr(0644,root,root)
%{_includedir}/lwip
%{_libdir}/liblwip.a

%changelog
* Fri Dec 31 2021 jiangheng<jiangheng12@huawei.com> - 2.1.3-2
- adapt to lstack

* Fri Nov 26 2021 jiangheng<jiangheng12@huawei.com> - 2.1.3-1
- update to 2.1.3

* Mon Sep 06 2021 jiangheng<jiangheng12@huawei.com> - 2.1.2-2
- backport some patches from community

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-1
- remove README

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-0
- Init package
