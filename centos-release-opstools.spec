Summary: Config to enable the repository for OpsTools SIG
Name:    centos-release-opstools
Version: 1
Release: 7%{?dist}
License: GPL
URL: http://wiki.centos.org/SpecialInterestGroup/OpsTools
Source0: CentOS-OpsTools.repo
Source1: RPM-GPG-KEY-CentOS-SIG-OpsTools

BuildArch: noarch

Requires: centos-release

%description
yum configs for CentOS OpsTools SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-OpsTools.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-CentOS-SIG-OpsTools

%changelog
* Thu Mar 23 2017 Matthias Runge <mrunge@redhat.com> - 1.7
- drop dependency on centos-openstack repos

* Fri Feb 24 2017 Matthias Runge <mrunge@redhat.com> - 1.6
- add gpg key for CentOS SIG OpsTools

* Wed Jan 25 2017 Matthias Runge <mrunge@redhat.com> - 1.5
- add opstools-release repo

* Fri Jan 13 2017 Matthias Runge <mrunge@redhat.com> - 1.4
- depend on newton release

* Fri Aug 26 2016 Matthias Runge <mrunge@redhat.com> - 1.3
- temporarily enable pulling logging packages from cbs

* Wed Aug 17 2016 Matthias Runge <mrunge@redhat.com> - 1.2
- fix repository location

* Tue Aug 02 2016 Matthias Runge <mrunge@redhat.com> - 1.1
- initial version
