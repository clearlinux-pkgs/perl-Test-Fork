#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-Test-Fork
Version  : 0.02
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Test-Fork-0.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Test-Fork-0.02.tar.gz
Summary  : test code which forks
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Fork-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Build)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the perl-Test-Fork package.
Group: Development
Provides: perl-Test-Fork-devel = %{version}-%{release}
Requires: perl-Test-Fork = %{version}-%{release}

%description dev
dev components for the perl-Test-Fork package.


%package perl
Summary: perl components for the perl-Test-Fork package.
Group: Default
Requires: perl-Test-Fork = %{version}-%{release}

%description perl
perl components for the perl-Test-Fork package.


%prep
%setup -q -n Test-Fork-0.02
cd %{_builddir}/Test-Fork-0.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Fork.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
