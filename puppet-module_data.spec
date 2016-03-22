Name:			puppet-module_data
Version:		XXX
Release:		XXX
Summary:		A hiera backend to allow the use of data while writing sharable modules
License:		ASL 2.0

URL:			https://github.com/ripienaar/puppet-module-data

Source0:		https://github.com/ripienaar/puppet-module-data/archive/%{version}.tar.gz

BuildArch:		noarch

Requires:		puppet >= 2.7.0

%description
A hiera backend to allow the use of data while writing sharable modules

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/module-data/



%files
%{_datadir}/openstack-puppet/modules/module-data/


%changelog

