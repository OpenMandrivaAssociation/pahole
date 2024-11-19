%define major 1
%define dwarvesdevel %mklibname -d dwarves

Summary:	Tool that shows data structure layouts encoded in debugging information
Name:		pahole
Version:	1.27
Release:	2
Group:		Development/C
License:	GPLv2+
# https://git.kernel.org/pub/scm/devel/pahole/pahole.git
Source0:	https://git.kernel.org/pub/scm/devel/pahole/pahole.git/snapshot/%{name}-%{version}.tar.gz

Provides:	dwarves = %{EVRD}
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(libbpf)

%patchlist
# Patches from upstream's upstream, needed for building kernels with clang+LTO
https://github.com/acmel/dwarves/commit/6a2b27c0f512619b0e7a769a18a0fb05bb3789a5.patch
https://github.com/acmel/dwarves/commit/94a01bde592c555b3eb526aeb4c2ad695c5660d8.patch

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
%autosetup -p1
%cmake \
		-DLIBBPF_EMBEDDED=OFF \
		-G Ninja

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
