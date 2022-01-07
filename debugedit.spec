Name: debugedit
Version: 5.0
Release: 2
Summary: Tools for debuginfo creation
License: GPL-2.0-or-later and LGPL-2.1-only and GPL-3.0-only
Group:   Applications
URL: https://sourceware.org/debugedit/
Source0: https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz
Source1: https://sourceware.org/pub/debugedit/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires: help2man gnupg2 elfutils-devel make gcc autoconf automake
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libdw)

Requires: binutils gawk coreutils xz elfutils findutils
Requires: /usr/bin/gdb-add-index
Suggests: gdb-minimal
Requires: sed dwz grep

Patch0: tests-Handle-zero-directory-entry-in-.debug_line-DWA.patch
Patch1: find-debuginfo.sh-decompress-DWARF-compressed-ELF-se.patch

%description
Debugedit provides programs and scripts for creating debuginfo and
source file distributions, collect build-ids and rewrite source
paths in DWARF data for debugging, tracing and profiling.

%prep
%autosetup -p1

%build
autoreconf -f -v -i
%configure
%make_build

%install
%make_install
cd %{buildroot}%{_bindir}
ln -s find-debuginfo find-debuginfo.sh
cd %{buildroot}
mkdir -p %{buildroot}%{_rpmconfigdir}
ln -s %{_bindir}/find-debuginfo %{buildroot}%{_rpmconfigdir}/find-debuginfo.sh
%check
sed -i 's/^\(C\|LD\)FLAGS=.*/\1FLAGS=""/' tests/atlocal
make check %{?_smp_mflags}

%clean

%files
%license COPYING COPYING3 COPYING.LIB
%doc README
%{_bindir}/debugedit
%{_bindir}/sepdebugcrcfix
%{_bindir}/find-debuginfo
%{_bindir}/find-debuginfo.sh
%{_mandir}/man1/debugedit.1*
%{_mandir}/man1/sepdebugcrcfix.1*
%{_mandir}/man1/find-debuginfo.1*
%{_rpmconfigdir}/find-debuginfo.sh

%changelog
* Fri Jan 07 2022 renhongxun <renhongxun@huawei.com> 5.0-2
- bugfix

* Sat Dec 25 2021 renhongxun <renhongxun@huawei.com>
- init package
