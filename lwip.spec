%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.2
Release: 9
License: BSD
URL:     http://savannah.nongnu.org/projects/lwip/
Source0: http://download.savannah.nongnu.org/releases/lwip/%{name}-%{version}.zip

Patch6001:  backport-bug-54700-Unexpected-expiry-of-pending-ARP-table-ent.patch 
Patch6002:  backport-tcp-Fix-double-free-in-tcp_split_unsent_seg.patch  
Patch6003:  backport-tcp-fix-sequence-number-comparison.patch 
Patch6004:  backport-tcp-tighten-up-checks-for-received-SYN.patch 

Patch9001:  0001-add-makefile.patch
Patch9002:  0002-adapt-lstack.patch
Patch9003:  0003-fix-the-occasional-coredump-when-the-lwip-exits.patch
Patch9004:  0004-fix-error-of-deleting-conn-table-in-connect.patch
Patch9005:  0005-syn-rcvd-state-reg-conn-into-conntable.patch
Patch9006:  0006-fix-coredump-in-etharp.patch
Patch9007:  0007-gazelle-fix-epoll_ctl-EPOLLET-mode-error.patch
Patch9008:  0008-gazelle-fix-lwip_accept-memcpy-sockaddr-large.patch
Patch9009:  0009-fix-stack-buffer-overflow-when-memcpy-addr.patch
Patch9010:  0010-fix-the-incomplete-release-of-the-conntable.patch
Patch9011:  0011-remove-gazelle-tcp-conn-func.patch
Patch9012:  0012-fix-incomplete-resource-release-in-lwip-close.patch
Patch9013:  0013-remove-gazelle-syscall-thread.patch
Patch9014:  0014-fix-some-compile-errors.patch
Patch9015:  0015-fix-tcp-port-alloc-issue.patch
Patch9016:  0016-lstack-support-mysql-mode.patch
Patch9017:  0017-support-REUSEPOR-option.patch
Patch9018:  0018-exec-gazelle_init_sock-before-read-event.patch
Patch9019:  0019-gazelle-reduce-copy-in-send.patch
Patch9020:  0020-remove-chose_dlsym_handle-function-set-handle-to-RTL.patch
Patch9021:  0021-refactor-event-if-ring-is-full-the-node-is-added-to-.patch
Patch9022:  0022-notify-app-that-sock-state-changes-to-CLOSE_WAIT.patch
Patch9023:  0023-refactor-event-and-checksum-offload-support.patch
Patch9024:  0024-refactor-pkt-read-send-performance.patch
Patch9025:  0025-del-redundant-wait_close-and-move-epoll_events-pos.patch
Patch9026:  0026-modify-EISCONN-condition.patch
Patch9027:  0027-per-thread-reassdata-variables.patch
Patch9028:  0028-fix-EISCONN-err-and-remove-same-customized-modificat.patch
Patch9029:  0029-refactor-tcp-new-port.patch

BuildRequires: gcc-c++ dos2unix dpdk-devel

#Requires: 

ExclusiveArch: x86_64 aarch64

%description
lwip is a small independent implementation of the TCP/IP protocol suite.

%prep
%setup -n %{name}-%{version} -q
find %{_builddir}/%{name}-%{version} -type f -exec dos2unix -q {} \;

%patch6001 -p1
%patch6002 -p1
%patch6003 -p1
%patch6004 -p1
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
%patch9015 -p1
%patch9016 -p1
%patch9017 -p1
%patch9018 -p1
%patch9019 -p1
%patch9020 -p1
%patch9021 -p1
%patch9022 -p1
%patch9023 -p1
%patch9024 -p1
%patch9025 -p1
%patch9026 -p1
%patch9027 -p1
%patch9028 -p1
%patch9029 -p1

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
* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-9
- fix multithread duplicate port num
  support select appropriate port num to rss same as nic

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-8
- fix EISCONN conditon err
  remove same customized modification

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-7
- per thread reassdata variables

* Thu Sep 22 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.2-6
- modify EISCONN path condition
  add in_send and send_flag value for gazelle

* Tue Jul 26 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-5
- del redundant wait_close in lwip_sock
  move epoll_events into cache aligned area

* Fri Jul 8 2022 xiusailong<xiusailong@huawei.com> - 2.1.2-4
- refactor pkt read send performance

* Tue Jun 07 2022 xiusailong<xiusailong@huawei.com> - 2.1.2-3
- support gazelle feature

* Mon Sep 06 2021 jiangheng<jiangheng12@huawei.com> - 2.1.2-2
- backport some patches from community

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-1
- remove README

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-0
- Init package
