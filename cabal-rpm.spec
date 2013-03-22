# https://fedoraproject.org/wiki/Packaging:Haskell
# https://fedoraproject.org/wiki/PackagingDrafts/Haskell

Name:           cabal-rpm
Version:        0.7.1
Release:        1%{?dist}
Summary:        RPM package creator for Haskell Cabal-based packages

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/packages/archive/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        cabal-rpm.1
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# Begin cabal-rpm deps:
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-old-locale-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
# End cabal-rpm deps
Obsoletes:      cabal2spec < 0.26
Provides:       cblrpm = %{version}

%description
Cabal-rpm generates RPM packages from Haskell Cabal packages.


%prep
%setup -q


%build
%ghc_bin_build


%install
%ghc_bin_install

install -p cblrpm-diff %{buildroot}%{_bindir}
install -p -m 0644 -D man/cblrpm.1 %{buildroot}%{_mandir}/man1/cblrpm.1
install -p -m 0644 %SOURCE1 %{buildroot}%{_mandir}/man1/

ln -s cblrpm %{buildroot}%{_bindir}/%{name}
ln -s cblrpm-diff %{buildroot}%{_bindir}/%{name}-diff


%files
%doc COPYING
%doc NEWS
%doc README.md
%{_bindir}/%{name}
%{_bindir}/cblrpm
%{_bindir}/%{name}-diff
%{_bindir}/cblrpm-diff
%{_mandir}/man1/cabal-rpm.1*
%{_mandir}/man1/cblrpm.1*


%changelog
* Fri Mar 22 2013 Jens Petersen <petersen@redhat.com> - 0.7.1-1
- add final full-stop to description if missing
- add ver-rel to initial changelog entry
- output warning when .spec already exists
- fix handling of package names that end in a digit
- output when trying a path
- map curl C dep to libcurl
- fix use of cblrpm-diff force lib option
- provide cblrpm

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 22 2013 Jens Petersen <petersen@redhat.com> - 0.7.0-1
- cabal-rpm and cabal-rpm-diff are now symlinks to cblrpm and cblrpm-diff
- now uses command args, initially spec, srpm, and build
- tries to sudo yum install dependencies
- https://github.com/juhp/cabal-rpm/blob/master/NEWS

* Wed Nov 21 2012 Jens Petersen <petersen@redhat.com> - 0.6.6-1
- now generates dependencies for C libs, buildtools, and pkgconfig depends
- add short cblrpm and cblrpm-diff alias symlinks
- fix handling of LGPL-2.1 license
- change backup suffix from .cabal-rpm to .cblrpm
- do not mistake non-existent tarballs for package names

* Thu Nov  1 2012 Jens Petersen <petersen@redhat.com> - 0.6.5-1
- drop hscolour BuildRequires
- simplify generated BuildRequires: drop version ranges,
  and exclude base, Cabal, etc
- use ExclusiveArch ghc_arches_with_ghci for template-haskell
- replace --name option with --library to force Lib package

* Tue Sep 25 2012 Jens Petersen <petersen@redhat.com> - 0.6.4-1
- add cabal-rpm-diff wrapper script
- fix generated manpage

* Mon Sep 24 2012 Jens Petersen <petersen@redhat.com> - 0.6.3-1
- can now handle tarball
- new manpage
- obsoletes cabal2spec

* Mon Sep 10 2012 Jens Petersen <petersen@redhat.com> - 0.6.2-1
- shorten description

* Mon Sep 10 2012 Fedora Haskell SIG <haskell@lists.fedoraproject.org>
- spec file generated by cabal-rpm-0.6.2
