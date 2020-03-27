How to build the package
========================

    $ rpmbuild -bs \
               --define "_sourcedir $PWD/SOURCES" \
               --define "_srcrpmdir $PWD" \
               --define "dist .el8.centos" \
               SPECS/centos-release-opstools.spec

    $ cbs build core8-extras-common-el8.centos \
           centos-release-opstools-1-9.el8.centos.src.rpm
