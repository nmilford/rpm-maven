rpm-maven
=========

An RPM spec file to install the Apache Maven software project management and comprehension tool. 

To Build: 

`sudo yum -y install rpmdevtools && rpmdev-setuptree`

`wget http://apache.petsads.us/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz -O ~/rpmbuild/SOURCES/apache-maven-3.0.5-bin.tar.gz`

`wget https://raw.github.com/nmilford/rpm-maven/master/maven.spec -O ~/rpmbuild/SPECS/maven.spec`

`rpmbuild -bb ~/rpmbuild/SPECS/maven.spec`
