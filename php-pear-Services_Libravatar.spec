%define		status		alpha
%define		pearname	Services_Libravatar
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - API interfacing class for libravatar.org
Name:		php-pear-Services_Libravatar
Version:	0.2.2
Release:	1
License:	MIT License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	34ed27cdfcac0421dcd069ecb369358a
URL:		http://pear.php.net/package/Services_Libravatar/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
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
