%define dwarvesdevel %mklibname -d dwarves
%define major 1
%define dwarveslib %mklibname dwarves %{major}
%define dwarves_emitlib %mklibname dwarves_emit %{major}
%define dwarves_reorganizelib %mklibname dwarves_reorganize %{major}

Summary:	Tool that shows data structure layouts encoded in debugging information
Name:		pahole
Version:	1.20
Release:	1
Group:		Development/C
# https://git.kernel.org/pub/scm/devel/pahole/pahole.git
Source0:	%{name}-%{version}.tar.gz
# https://github.com/libbpf/libbpf
# git archive -o ../libbpf-986962fade5dfa89c2890f3854eb040d2a64ab3.tar --prefix=lib/bpf/ 986962fade5dfa89c2890f3854eb040d2a64ab3
# (revision id is from pahole's submodules)
Source1:	libbpf-986962fade5dfa89c2890f3854eb040d2a64ab3.tar.xz
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

%prep
%autosetup -p1 -a 1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%libpackage dwarves %{major}
%libpackage dwarves_emit %{major}
%libpackage dwarves_reorganize %{major}

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
%{_mandir}/man1/pahole.1*
