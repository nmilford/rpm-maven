# To Build: 
#
# sudo yum -y install rpmdevtools && rpmdev-setuptree
#
# wget http://apache.petsads.us/maven/maven-3/3.0.5/binaries/apache-maven-3.0.5-bin.tar.gz -O ~/rpmbuild/SOURCES/apache-maven-3.0.5-bin.tar.gz
# wget https://raw.github.com/nmilford/rpm-maven/master/maven.spec -O ~/rpmbuild/SPECS/maven.spec
# rpmbuild -bb ~/rpmbuild/SPECS/maven.spec

Name:           maven
Version:        3.0.5
Release:        1
Summary:        Apache Maven software project management and comprehension tool.
License:        Apache Software License
URL:            http://ant.apache.org/
Group:          Development/Build Tools
Source0:        apache-maven-%{version}-bin.tar.gz
Requires:       jdk
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Apache Maven is a software project management and comprehension tool. Based on the concept of a project object model (POM), Maven can manage a project's build, reporting and documentation from a central piece of information.

%prep
%setup -q -n apache-maven-%{version}

%build

install -d -m 755 %{buildroot}/opt/%{name}
cp -R %{_builddir}/apache-maven-%{version}/* %{buildroot}/opt/%{name}/

# Make it the default, dawg.
install -d -m 755 %{buildroot}/etc/profile.d/
%{__cat} <<EOF > %{buildroot}/etc/profile.d/%{name}.sh
export MAVEN_HOME_HOME=/opt/%{name}
export PATH=/opt/%{name}/bin:$PATH
EOF

%clean
rm -rf %{buildroot}

%post
echo
echo "You will need to exit your shell to have ant in your default path."
echo "Or run the following"
echo '  export MAVEN_HOME_HOME=/opt/maven'
echo '  export PATH=/opt/maven/bin:$PATH'
echo

%files
/opt/%{name}/
/etc/profile.d/%{name}.sh

%changelog
* Sun Jun 30 2013 Nathan Milford <nathan@milford.io> - 3.0.5-1
- First go at it.