%define upstream_name    minismokebox
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A backend to App::SmokeBox::Mini
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(App::SmokeBox::PerlVersion)
BuildRequires:	perl(Config::Tiny)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Module::Load)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Net::IP)
BuildRequires:	perl(POE)
BuildRequires:	perl(POE::Component::SmokeBox)
BuildRequires:	perl(POE::Component::SmokeBox::Dists)
BuildRequires:	perl(POE::Component::SmokeBox::Recent)
BuildRequires:	perl(POE::Filter::HTTP::Parser)
BuildRequires:	perl(POE::Quickie)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(String::Perl::Warnings)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::POE::Server::TCP)
BuildRequires:	perl(Time::Duration)
BuildArch:	noarch

%description
This document describes the App::SmokeBox::Mini::Plugin system for the
App::SmokeBox::Mini manpage and the minismokebox manpage.

Plugins are a mechanism for providing additional functionality to the
App::SmokeBox::Mini manpage and the minismokebox manpage.

It is assumed that plugins will be the POE manpage based and consist of at
least one the POE::Session manpage.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL="--skipdeps --alldeps"
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_bindir}/minismokebox
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.440.0-2mdv2011.0
+ Revision: 657477
- rebuild for updated spec-helper

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.440.0-1
+ Revision: 644767
- update to new version 0.44

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.400.0-3mdv2011.0
+ Revision: 625110
- Add Net::IP as an explicit dep
- Set the CPAN distro Just-f-do-it (JFDI) environment vars
- Upgraded to 0.40
- import perl-minismokebox

