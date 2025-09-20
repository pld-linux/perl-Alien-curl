#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	Alien
%define		pnam	curl
Summary:	Alien::curl - Discover or download and install curl + libcurl
Summary(pl.UTF-8):	Alien::curl - wykrywanie lub pobieranie i instalowanie biblioteki curl
Name:		perl-Alien-curl
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Alien/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fcedb90c1523876b76a1241ca63bc2b8
URL:		https://metacpan.org/dist/Alien-curl
BuildRequires:	curl-devel
BuildRequires:	perl-Alien-Build >= 0.40
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.52
BuildRequires:	perl-Env-ShellWords
BuildRequires:	perl-FFI-CheckLib
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Alien-Base >= 0.038
BuildRequires:	perl-Test-Alien >= 0.11
BuildRequires:	perl-Test-Simple >= 0.98
BuildRequires:	perl-Test2-Suite >= 0.000121
%endif
Requires:	curl-devel
Requires:	perl-Alien-Base >= 0.038
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# no binary code, but platform dependent paths inside
%define		_enable_debug_packages	0

%description
This distribution provides curl so that it can be used by other Perl
distributions that are on CPAN. It does this by first trying to detect
an existing install of curl on your system. If found it will use that.
If it cannot be found, the source code will be downloaded from the
Internet and it will be installed in a private share location for the
use of other modules.

%description -l pl.UTF-8
Ten pakiet dostarcza bibliotekę curl tak, że może być używana przez
inne pakiety Perla z CPAN. W pierwszej kolejności próbuje wykryć
istniejącą instalację biblioteki curl w systemie; jeśli nie istnieje,
zostanie pobrana i zainstalowana w prywatnej lokalizacji dla innych
modułów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Alien/curl.pm
%{perl_vendorarch}/Alien/curl
%{perl_vendorarch}/auto/Alien/curl
%{perl_vendorarch}/auto/share/dist/Alien-curl
%{_mandir}/man3/Alien::curl.3pm*
