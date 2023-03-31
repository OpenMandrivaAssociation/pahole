%define major 1
%define dwarvesdevel %mklibname -d dwarves

Summary:	Tool that shows data structure layouts encoded in debugging information
Name:		pahole
Version:	1.24
Release:	4
Group:		Development/C
# https://git.kernel.org/pub/scm/devel/pahole/pahole.git
Source0:	%{name}-%{version}.tar.gz
# (revision id is from pahole's submodules) https://git.kernel.org/pub/scm/devel/pahole/pahole.git/log/lib
Source1:	https://github.com/libbpf/libbpf/archive/6597330c45d185381900037f0130712cd326ae5.tar.gz
# Needed to make kernels compile with binutils >= 2.40
# https://lore.kernel.org/all/YzwkazNc6wNCpQTN@kernel.org/t/
Patch0:		pahole-fix-kernel-builds-with-binutils-2.40.patch
License:	GPLv2+
Provides:	dwarves = %{EVRD}
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libelf)

%description
pahole shows data structure layouts encoded in debugging information formats,
DWARF, CTF and BTF being supported.

This is useful for, among other things: optimizing important data structures by
reducing its size, figuring out what is the field sitting at an offset from the
start of a data structure, investigating ABI changes and more generally
understanding a new codebase you have to work with.

%package -n %{dwarvesdevel}
Summary:	Development files for the dwarves library, a part of pahole
Group:		Development/C

%description -n %{dwarvesdevel}
Development files for the dwarves library, a part of pahole

%libpackage dwarves %{major}
%libpackage dwarves_emit %{major}
%libpackage dwarves_reorganize %{major}

%prep
%autosetup -p1 -a 1
rmdir lib/bpf
mv libbpf-* lib/bpf
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{dwarvesdevel}
%{_includedir}/dwarves
%{_libdir}/*.so

%files
%{_bindir}/btfdiff
%{_bindir}/codiff
%{_bindir}/ctracer
%{_bindir}/dtagnames
%{_bindir}/fullcircle
%{_bindir}/ostra-cg
%{_bindir}/pahole
%{_bindir}/pdwtags
%{_bindir}/pfunct
%{_bindir}/pglobal
%{_bindir}/prefcnt
%{_bindir}/scncopy
%{_bindir}/syscse
%{_datadir}/dwarves
%doc %{_mandir}/man1/pahole.1*
