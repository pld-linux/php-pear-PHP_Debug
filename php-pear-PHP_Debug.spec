%include	/usr/lib/rpm/macros.php
%define		_status		stable
%define		_pearname	PHP_Debug
Summary:	%{_pearname} - provides assistance in debugging PHP code
Summary(pl.UTF-8):	%{_pearname} - pomoc przy odpluskiwaniu kodu PHP
Name:		php-pear-%{_pearname}
Version:	1.0.3
Release:	2
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	2176e37a1b7d5b2c459593863cadcaeb
URL:		http://pear.php.net/package/PHP_Debug/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Suggests:	php-pear-Text_Highlighter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Text/Highlighter.*)'  'pear(Services/W3C/HTMLValidator.*)'

%description
The basic purpose of PHP_Debug is to provide assistance in debugging
PHP code, by "debug" i don't mean "step by step debug" but program
trace, variables display, process time, included files, queries
executed, watch variables... These informations are gathered through
the script execution and therefore are displayed at the end of the
script (in a nice floating div or a html table) so that it can be read
and used at any moment. (especially usefull during the development
phase of a project or in production with a secure key/ip)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Podstawowym zadaniem PHP_Debug jest pomoc przy odpluskiwaniu kodu PHP.
Nie chodzi tu o śledzenieu krok po kroku działania programu, ale
wyświetlaniu wywołań programu, zmiennych, czasu działania, dołączonych
plików, wykonanych zapytań, śledzonych zmiennych... Informacje te
zbierane są w trakcie wywoływania skryptu, wobec czego wyświetlane sa
po zakończeniu jego działania (w postaci warstwy div lub tabeli HTML)
i mogą być wykorzystane w dowolnym momencie, co może być szczególnie
przydatne na etapie projektowania lub produkcyjnym.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%if 2
%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi
%endif

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/PHP_Debug/docs docs/PHP_Debug/*.php
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/PHP/Debug
%{php_pear_dir}/PHP/Debug.php
%{php_pear_dir}/PHP/DebugLine.php
%{php_pear_dir}/data/PHP_Debug
