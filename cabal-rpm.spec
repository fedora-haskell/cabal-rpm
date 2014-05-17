# https://fedoraproject.org/wiki/Packaging:Haskell

# no useful debuginfo for Haskell packages without C sources
%global debug_package %{nil}

Name:           cabal-rpm
Version:        0.8.11
Release:        1%{?dist}
Summary:        RPM packaging tool for Haskell Cabal-based packages

License:        GPLv3+
URL:            http://hackage.haskell.org/package/%{name}
Source0:        http://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        cabal-rpm.1
Source2:        cblrpm-diff

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
Provides:       cblrpm = %{version}-%{release}
Requires:       cabal-install
Requires:       rpm-build
# for repoquery
Requires:       yum-utils

%description
Cabal-rpm is a tool for RPM packaging of Haskell Cabal-based packages.
It interacts with yum to install build dependencies and can also act as
a cabal-install wrapper installing dependencies packaged in Fedora before
running "cabal install".


%prep
%setup -q


%build
%ghc_bin_build


%install
%ghc_bin_install

install -p %SOURCE2 %{buildroot}%{_bindir}
install -p -m 0644 -D man/cblrpm.1 %{buildroot}%{_mandir}/man1/cblrpm.1
install -p -m 0644 %SOURCE1 %{buildroot}%{_mandir}/man1/

ln -s cblrpm %{buildroot}%{_bindir}/%{name}
ln -s cblrpm-diff %{buildroot}%{_bindir}/%{name}-diff


%files
%doc ChangeLog
%doc COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/cblrpm
%{_bindir}/%{name}-diff
%{_bindir}/cblrpm-diff
%{_mandir}/man1/cabal-rpm.1*
%{_mandir}/man1/cblrpm.1*


%changelog
* Sat May 17 2014 Jens Petersen <petersen@redhat.com> - 0.8.11-1
- use .spec file to determine pkg-ver when no .cabal file around
- build command renamed again from "rpm" to "local" (like fedpkg)
- automatically generate bcond for %check and add testsuite BRs
  when testsuites available
- disable debuginfo explicitly when no c-sources in preparation for
  ghc-rpm-macros no longer disabling debuginfo
- reset filemode of downloaded hackage tarballs to 0644:
  workaround for cabal-install setting 0600
- include release again in initial changelog

* Mon Mar  3 2014 Jens Petersen <petersen@redhat.com> - 0.8.10-1
- new diff command replaces cblrpm-diff script
- new missingdeps command
- should now work on RHEL 5 and 6: dropped use use of rpmspec
- add a temporary cblrpm-diff compat script
- refresh description

* Mon Feb 10 2014 Jens Petersen <petersen@redhat.com> - 0.8.9-1
- bugfix for error handling dir with spec file
- cblrpm-diff arg is now optional

* Sun Feb  9 2014 Jens Petersen <petersen@redhat.com> - 0.8.8-1
- use .spec file to determine package if no .cabal file (with or without arg)
- bugfix: install command now works if some dependencies not packaged
- bugfix: do not re-copy cached tarball each time
- use new shorter hackage2 URL for packages
- filter @ and \ quotes in descriptions
- capitalize start of summary and description
- new prep command (like "rpmbuild -bp" or "fedpkg prep")
- new depends and requires commands list package depends or buildrequires
- new builddep command (like yum-buildep, but allows missing packages)

* Tue Dec 31 2013 Jens Petersen <petersen@redhat.com> - 0.8.7-1
- new "install" command wrapping "cabal install"
- "build" command renamed to "rpm"
- sort devel Requires
- cblrpm-diff: allow package arg
- support copying tarball fetched from another remote-repo (codeblock)
- support AGPL license in Cabal-1.18
- update package description

* Tue Oct  8 2013 Jens Petersen <petersen@redhat.com> - 0.8.6-1
- check for _darcs or .git dir in package topdir not pwd

* Sun Sep 29 2013 Jens Petersen <petersen@redhat.com> - 0.8.5-1
- fix repoquery when a package update exists for C lib
- make cblrpm-diff quieter

* Sat Sep 28 2013 Jens Petersen <petersen@redhat.com> - 0.8.4-1
- use repoquery to determine extra C library dependencies
- quote "pkgconfig(foo)" for rpm query and yum install
- show sudo command before sudo password prompt appears
- exclude hsc2hs from build tool deps
- devel now provides ghc-<pkg>-static
- drop release from initial changelog entry for packager to add an entry
- do not try to fetch tarball for a darcs or git source dir

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Jens Petersen <petersen@redhat.com> - 0.8.3-1
- only try to install missing dependencies
- word-wrap generic descriptions
- now handles ghc_fix_dynamic_rpath for executables depending on own lib
- map ffi to libffi
- source module rearrangements

* Tue Jul  2 2013 Jens Petersen <petersen@redhat.com> - 0.8.2-1
- handle pkg-ver arg, and check cabal list is non-empty
- sort all generated deps
- use yum-builddep again to install deps
- copy tarball into cwd for rpmbuild
- wrap after end of sentence near end of line
- use _isa in requires ghc-<pkg>
- require rpm-build

* Fri Jun 21 2013 Jens Petersen <petersen@redhat.com> - 0.8.1-2
- rebuild

* Fri Jun 14 2013 Jens Petersen <petersen@redhat.com> - 0.8.1-1
- word wrapping of descriptions
- use generic description for shared subpackage
- simplify logic for summary and description processing

* Fri May 31 2013 Jens Petersen <petersen@redhat.com> - 0.8.0-1
- use simplified Fedora Haskell Packaging macros approved by
  Fedora Packaging Committee (https://fedorahosted.org/fpc/ticket/194)

* Wed Apr  3 2013 Jens Petersen <petersen@redhat.com> - 0.7.1-2
- better require cabal-install

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
