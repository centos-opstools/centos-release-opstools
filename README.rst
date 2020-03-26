How to build the package
========================

rpmbuild -D 'dist .el8.centos' -bs centos-release-opstools.spec

cbs build core8-extras-common-el8.centos ~/rpmbuild/SRPMS/centos-release-opstools-1-9.el8.centos.src.rpm
