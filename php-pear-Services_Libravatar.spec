%define		status		alpha
%define		pearname	Services_Libravatar
%define		php_min_version 5.2.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - API interfacing class for libravatar.org
Name:		php-pear-Services_Libravatar
Version:	0.2.3
Release:	1
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	510ea180536e3c0bec1be7ca0ead32b9
URL:		http://pear.php.net/package/Services_Libravatar/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(filter)
Requires:	php(hash)
Requires:	php(pcre)
Requires:	php(spl)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows PHP applications to implement libravatar.org

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Services_Libravatar/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Libravatar.php
%{php_pear_dir}/data/Services_Libravatar
