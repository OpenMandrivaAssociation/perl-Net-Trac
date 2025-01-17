%define upstream_name    Net-Trac
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Simple client library for a remote Trac instance
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Lingua::EN::Inflect)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Text::CSV)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(WWW::Mechanize)
BuildArch:	noarch

%description
Net::Trac is simple client library for a remote Trac instance. Because Trac
doesn't provide a web services API, this module currently "fakes" an RPC
interface around Trac's webforms and the feeds it exports. Because of this,
it's somewhat more brittle than a true RPC client would be.

As of now, this module has been tested against Trac 10.4 and Trac 11.0.

The author's needs for this module are somewhat modest and its current
featureset reflects this. Right now, only basic read/write functionality
for Trac's tickets is provided. Patches would be gratefully appreciated.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# (misc, 30/04/2010) 
# tests do not work
# https://rt.cpan.org/Ticket/Display.html?id=57063 
#make test

%install
%makeinstall_std

%files
%doc META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/Net


%changelog
* Wed Apr 06 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 651042
- new version 0.16

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 541156
- import perl-Net-Trac


* Fri Apr 30 2010 cpan2dist 0.15-1mdv
- initial mdv release, generated with cpan2dist
