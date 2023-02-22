%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.3
Release: 42
License: BSD
URL:     http://savannah.nongnu.org/projects/lwip/
Source0: http://download.savannah.nongnu.org/releases/lwip/%{name}-%{version}.zip

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
Patch9028:  0029-fix-EISCONN-err-and-remove-same-customized-modificat.patch
Patch9029:  0030-refactor-tcp-new-port.patch
Patch9030:  0031-refactor-add-event-limit-send-pkts-num.patch
Patch9031:  0032-fix-free-pbuf-miss-data.patch
Patch9032:  0033-alloc-socket-fail-clean-sock.patch
Patch9033:  0034-add-accept4-and-epoll_create1.patch
Patch9034:  0035-add-writev-and-readv.patch 
Patch9035:  0036-add-fs-secure-compilation-option.patch
Patch9036:  0037-enable-ARP-QUEUE-to-avoid-sync-packet-dropped.patch
Patch9037:  0038-add-tso.patch
Patch9038:  0039-optimize-app-thread-write-buff-block.patch
Patch9039:  0040-add-huge-snd_buf.patch
Patch9040:  0041-optimite-pcb-list-limit-send-size-and-ack-now.patch
Patch9041:  0042-expand-recv-win.patch
Patch9042:  0043-add-prefetch.patch
Patch9043:  0044-skip-unnecessary-tcp_route.patch
Patch9044:  0045-add-variable-in-struct-sock.patch
Patch9045:  0046-add-dataack-when-recv-too-many-acks-with-data.patch
Patch9046:  0047-reduce-struct-pbuf-size.patch
Patch9047:  0048-listen-pcb-also-use-pcb_if.patch
Patch9048:  0049-expand-recv-mbox-size.patch
Patch9049:  0050-lwip-reuse-ip-port.patch
Patch9050:  0051-lwip-add-need_tso_send.patch

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
%patch9030 -p1
%patch9031 -p1
%patch9032 -p1
%patch9033 -p1
%patch9034 -p1
%patch9035 -p1
%patch9036 -p1
%patch9037 -p1
%patch9038 -p1
%patch9039 -p1
%patch9040 -p1
%patch9041 -p1
%patch9042 -p1
%patch9043 -p1
%patch9044 -p1
%patch9045 -p1
%patch9046 -p1
%patch9047 -p1
%patch9048 -p1
%patch9049 -p1
%patch9050 -p1

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
* Tue Feb 21 2023 majun<majun65@huawei.com> - 2.1.3-42
- add lwip need_tso_send

* Tue Feb 14 2023 majun<majun65@huawei.com> - 2.1.3-41
- add lwip reuse ip port

* Sat Feb 11 2023 majun<majun65@huawei.com> - 2.1.3-40
- fix TSO snd_nxt incorrectly update

* Fri Dec 30 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-39
- expand recv mbox size

* Wed Dec 21 2022 jiangheng <jiangheng14@huawei.com> - 2.1.3-38
- move pcb_if to ip_pcb to let listen pcb can use it

* Wed Dec 21 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-37
- reduce struct pbuf size

* Wed Dec 21 2022 kircher<majun65@huawei.com> - 2.1.3-36
- do not update cwnd when send dataack

* Tue Dec 20 2022 kircher<majun65@huawei.com> - 2.1.3-35
- fix the dataack is always lower than 256

* Tue Dec 20 2022 kircher<majun65@huawei.com> - 2.1.3-34
- add dataack when recv too many acks with data

* Tue Dec 20 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-33
- add variable in struct sock

* Mon Dec 19 2022 kircher<majun65@huawei.com> - 2.1.3-32
- skip unnecessary tcp_route

* Sun Dec 18 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-31
- expand rcv wnd size and add prefetch

* Tue Dec 13 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-30
- optimite pcb unsent and unacked list
  fast rexmit all pkts

* Tue Dec 6 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.3-29
- add huge snd_buf

* Sat Dec 3 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-28
- add tso define

* Thu Dec 01 2022 jiangheng<jiangheng14@huawei.com> - 2.1.3-27
- remove lwip-2.1.3.tar.gz

* Sat Nov 26 2022 jiangheng<jiangheng14@huawei.com> - 2.1.3-26
- replace lwip-2.1.3.tar.gz to lwip-2.1.3.zip

* Wed Nov 23 2022 jiangheng<jiangheng14@huawei.com> - 2.1.3-25
- enable ARP QUEUE to avoid packet dropped

* Sat Oct 22 2022 jiangheng<jiangheng14@huawei.com> - 2.1.3-24
- add fs secure compilation option

* Wed Oct 19 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.3-23
- add writev and readv

* Sat Oct 15 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.3-22
- add epoll_create1 and accetp4

* Tue Oct 11 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-21
- alloc socket fail clean sock

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-20
- fix miss data due to free pbuf
  close debug

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-19
- refactor add event
  limit send pkts num max 10

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-18
- fix multithread duplicate port num
  support select appropriate port num to rss same as nic

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.3-17
- fix EISCONN conditon err
  remove same customized modification

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
