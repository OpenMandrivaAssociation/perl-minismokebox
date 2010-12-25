%define upstream_name    minismokebox
%define upstream_version 0.40

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    A backend to App::SmokeBox::Mini
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::SmokeBox::PerlVersion)
BuildRequires: perl(Config::Tiny)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Spec)
BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Net::IP)
BuildRequires: perl(POE)
BuildRequires: perl(POE::Component::SmokeBox)
BuildRequires: perl(POE::Component::SmokeBox::Dists)
BuildRequires: perl(POE::Component::SmokeBox::Recent)
BuildRequires: perl(POE::Filter::HTTP::Parser)
BuildRequires: perl(Pod::Usage)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::POE::Server::TCP)
BuildRequires: perl(Time::Duration)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_bindir}/minismokebox
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*


