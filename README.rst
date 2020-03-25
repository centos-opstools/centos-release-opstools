How to build the package
========================

rpmbuild -D 'dist .el7.centos' -bs centos-release-opstools.spec

cbs build core7-extras-common-el7.centos ~/rpmbuild/SRPMS/centos-release-opstools-1-7.el7.centos.src.rpm
