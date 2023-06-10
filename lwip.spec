%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.2
Release: 40
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
Patch9030:  0030-refactor-add-event-limit-send-pkts-num.patch
Patch9031:  0031-fix-free-pbuf-miss-data.patch
Patch9032:  0032-alloc-socket-fail-clean-sock.patch
Patch9033:  0034-add-accept4-and-epoll_create1.patch
Patch9034:  0035-add-writev-and-readv.patch
Patch9035:  0036-enable-ARP-QUEUE-to-avoid-sync-packet-dropped.patch
Patch9036:  0037-add-tso.patch
Patch9037:  0038-optimize-app-thread-write-buff-block.patch
Patch9038:  0039-add-huge-snd_buf.patch
Patch9039:  0040-optimite-pcb-list-limit-send-size-and-ack-now.patch
Patch9040:  0041-expand-recv-win.patch
Patch9041:  0042-add-prefetch.patch
Patch9042:  0043-skip-unnecessary-tcp_route.patch
Patch9043:  0044-add-variable-in-struct-sock.patch
Patch9044:  0045-add-dataack-when-recv-too-many-acks-with-data.patch
Patch9045:  0046-reduce-struct-pbuf-size.patch
Patch9046:  0047-listen-pcb-also-use-pcb_if.patch
Patch9047:  0048-expand-recv-mbox-size.patch
Patch9048:  0049-lwip-reuse-ip-port.patch
Patch9049:  0050-lwip-add-need_tso_send.patch
Patch9050:  0051-lwip_fnctl-only-support-F_SETFL-F_GETFL.patch
Patch9051:  0052-cleancode-improve-lwipopts.h-readability.patch
Patch9052:  0053-reduce-cpu-usage-when-send.patch
Patch9053:  0054-add-pbuf-lock-when-aggregate-pbuf.patch
Patch9054:  0055-fix-tso-small-packet-drop-in-kernel-server.patch
Patch9055:  0056-same-node-gazellectl-a.patch
Patch9056:  0057-lwip-send-recv-thread-bind-numa.patch
Patch9057:  0058-fix-last_unsent-last_unacked.patch
Patch9058:  0059-lwip-add-udp-multicast.patch
Patch9059:  0060-optimize-avoid-too-many-empty-acks-in-tcp_input.patch

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
%patch9051 -p1
%patch9052 -p1
%patch9053 -p1
%patch9054 -p1
%patch9055 -p1
%patch9056 -p1
%patch9057 -p1
%patch9058 -p1
%patch9059 -p1

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
* Sat Jun 10 2023 Lemmy Huang <huangliming5@huawei.com> - 2.1.2-40
- optimize: avoid too many empty acks in tcp_input

* Sat May 13 2023 kircher <majun65@huawei.com> - 2.1.2-39
- add udp multicast support in lwip

* Sat Apr 01 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-38
- fix last_unsent/last_unacked error
- fix send failed due to pcb->nrtx > TCP_MAXRTX

* Tue Mar 21 2023 kircher <majun65@huawei.com> - 2.1.2-37
- lwip send/recv thread bind numa

* Mon Mar 13 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-36
- add same node ring & gazellectl -a

* Mon Mar 13 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-35
- fix tso small packet drop in kernel server

* Mon Mar 13 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-34
- add pbuf lock when aggregate pbuf

* Fri Mar 10 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-33
- reduce cpu usage when send

* Thu Mar 9 2023 Lemmy Huang <huangliming5@huawei.com> - 2.1.2-32
- cleancode: improve lwipopts.h readability

* Tue Wed 22 2023 jiangheng <jiangheng14@huawei.com> - 2.1.2-31
- lwip_fnctl only suport F_SETFL,F_GETFL, other opt return 0 for compitable

* Tue Feb 21 2023 majun<majun65@huawei.com> - 2.1.2-30
- add lwip need_tso_send

* Tue Feb 14 2023 majun<majun65@huawei.com> - 2.1.2-29
- add lwip reuse ip port

* Sat Feb 11 2023 majun<majun65@huawei.com> - 2.1.2-28
- fix TSO snd_nxt incorrectly update

* Fri Dec 30 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-27
- expand recv mbox size

* Wed Dec 21 2022 jiangheng<jiangheng14@huawei.com> - 2.1.2-26
- move pcb_if to ip_pcb to let listen pcb use it

* Wed Dec 21 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-25
- reduce struct pbuf size

* Wed Dec 21 2022 kircher<majun65@huawei.com> - 2.1.2-24
- do not update cwnd when send dataack

* Tue Dec 20 2022 kircher<majun65@huawei.com> - 2.1.2-23
- fix dataack is always lower than 256

* Tue Dec 20 2022 kircher<majun65@huawei.com> - 2.1.2-22
- add dataack when recv too many acks with data

* Tue Dec 20 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-21
- add variable in struct sock

* Mon Dec 19 2022 kircher<majun65@huawei.com> - 2.1.2-20
- skip unnecessary tcp_route

* Sun Dec 18 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-19
- expand rcv wnd size and prefetch

* Tue Dec 13 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-18
- optimite pcb unsent and unacked list
  fast rexmit all pkts

* Wed Dec 7 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.2-17
- add huge snd buf

* Sat Dec 3 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-16
- add tso define

* Wed Nov 23 2022 jiangheng<jiangheng14@huawei.com> - 2.1.2-15
- enable ARP QUEUE to avoid packet dropped

* Wed Oct 19 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.2-14
- add writev and readv

* Sat Oct 15 2022 zhujunhao<zhujunhao11@huawei.com> - 2.1.2-13
- add epoll_create1 and accetp4

* Tue Oct 11 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-12
- alloc socket fail clean sock

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-11
- fix miss data due to free pbuf
  close debug

* Thu Oct 6 2022 wuchangsheng<wuchangsheng2@huawei.com> - 2.1.2-10
- refactor add event
  limit send pkts num max 10

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
