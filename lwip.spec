%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.3
Release: 16
License: BSD
URL:     http://savannah.nongnu.org/projects/lwip/
Source0: http://download.savannah.nongnu.org/releases/lwip/%{name}-%{version}.tar.gz

Patch6001:  backport-tcp-fix-sequence-number-comparison.patch
Patch6002:  backport-tcp-tighten-up-checks-for-received-SYN.patch

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
Patch9015:  0016-lstack-support-mysql-mode.patch
Patch9016:  0017-support-REUSEPOR-option.patch
Patch9017:  0018-exec-gazelle_init_sock-before-read-event.patch
Patch9018:  0019-gazelle-reduce-copy-in-send.patch
Patch9019:  0020-remove-chose_dlsym_handle-function-set-handle-to-RTL.patch
Patch9020:  0021-refactor-event-if-ring-is-full-the-node-is-added-to-.patch
Patch9021:  0022-notify-app-that-sock-state-changes-to-CLOSE_WAIT.patch
Patch9022:  0023-refactor-event-and-checksum-offload-support.patch
Patch9023:  0024-refactor-pkt-read-send-performance.patch
Patch9024:  0025-Replace-gettid-with-syscall-SYS_gettid.patch
Patch9025:  0026-del-redundant-wait_close-and-move-epoll_events-pos.patch
Patch9026:  0027-modify-EISCONN-condition.patch
Patch9027:  0028-per-thread-reassdata-variables.patch

BuildRequires: gcc-c++ dos2unix dpdk-devel

#Requires: 

ExclusiveArch: x86_64 aarch64

%description
lwip is a small independent implementation of the TCP/IP protocol suite.

%prep
%autosetup -n %{name}-%{version} -p1
find %{_builddir}/%{name}-%{version} -type f -exec dos2unix -q {} \;

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
* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-16
- per thread reassdata variables

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-15
- modify EISCONN path condition
  add in_send and send_flag value in sock

* Tue Jul 26 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-14
- del redundant wait_close in lwip_sock
  move epoll_events into cache aligned area

* Tue Jul 12 2022 Honggang Li <honggangli@163.com> - 2.1.3-13
- Replace gettid() with syscall()

* Fri Jul 8 2022 xiusailong<xiusailong@huawei.com> - 2.1.3-12
- sync two patches from 20.03-LTS-SP1

* Thu Jul 7 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-11
- refactor refactor pkt read send performance

* Tue Mar 29 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-10
- refactor event
- add HW checksum offload support

* Tue Mar 15 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-9
- notify app that sock state changes to CLOSE_WAIT

* Tue Mar 15 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-8
- refactor event,if ring is full, node is added to list

* Mon Mar 07 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-7
- remove chose_dlsym_handle function as it is redundant

* Mon Mar 07 2022 wu-changsheng<wuchangsheng2@huawei.com> - 2.1.3-6
- gazelle reduce copy in send

* Mon Mar 07 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-5
- exec gazelle_sock_init before read event

* Thu Mar 03 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-4
- support REUSEPOR option
- fix rpc msg too much
- fix recrruing events

* Thu Feb 24 2022 jiangheng<jiangheng12@huawei.com> - 2.1.3-3
- remove kernel socket interface
- support the mode that listen and accept thread be separaten

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
