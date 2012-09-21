# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

Name:           cabal-rpm
Version:        0.6.2
Release:        1%{?dist}
Summary:        RPM package creator for Haskell Cabal-based packages

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel > 1.10
BuildRequires:  ghc-base-devel < 5
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps

%description
This package generates RPM spec files from Haskell Cabal packages.


%prep
%setup -q


%build
%ghc_bin_build


%install
%ghc_bin_install


%files
%doc COPYING
%doc README.md
%{_bindir}/%{name}


%changelog
* Mon Sep 10 2012 Jens Petersen <petersen@redhat.com> - 0.6.2-1
- shorten description

* Mon Sep 10 2012 Fedora Haskell SIG <haskell@lists.fedoraproject.org>
- spec file generated by cabal-rpm-0.6.2
