%global debug_package %{nil}
%global __os_install_post %{nil}

Summary: lwip is a small independent implementation of the TCP/IP protocol suite
Name:    lwip
Version: 2.1.2
Release: 2
License: BSD
URL:     http://savannah.nongnu.org/projects/lwip/
Source0: http://download.savannah.nongnu.org/releases/lwip/%{name}-%{version}.zip

Patch0:  0001-add-makefile.patch
Patch1:  backport-bug-54700-Unexpected-expiry-of-pending-ARP-table-ent.patch 
Patch2:  backport-tcp-Fix-double-free-in-tcp_split_unsent_seg.patch  
Patch3:  backport-tcp-fix-sequence-number-comparison.patch 
Patch4:  backport-tcp-tighten-up-checks-for-received-SYN.patch 

BuildRequires: gcc-c++ dos2unix

#Requires: 

ExclusiveArch: x86_64 aarch64

%description
lwip is a small independent implementation of the TCP/IP protocol suite.

%prep
%setup -n %{name}-%{version} -q
find %{_builddir}/%{name}-%{version} -type f -exec dos2unix -q {} \;

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
* Mon Sep 06 2020 jiangheng<jiangheng12@huawei.com> - 2.1.2-2
- backport some patches from community

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-1
- remove README

* Mon Nov 30 2020 peanut_huang<huangliming5@huawei.com> - 2.1.2-0
- Init package
