%define major 1
%define dwarvesdevel %mklibname -d dwarves

Summary:	Tool that shows data structure layouts encoded in debugging information
Name:		pahole
Version:	1.24
Release:	6
Group:		Development/C
License:	GPLv2+
# https://git.kernel.org/pub/scm/devel/pahole/pahole.git
Source0:	%{name}-%{version}.tar.gz
# (revision id is from pahole's submodules) https://git.kernel.org/pub/scm/devel/pahole/pahole.git/log/lib
Source1:	https://github.com/libbpf/libbpf/archive/6597330c45d185381900037f0130712cd326ae5.tar.gz
# (tpg) upstream patches
Patch100:	0000-core-Conditionally-define-language-encodings.patch
Patch101:	0001-btf-Fix-building-with-system-libbpf.patch
Patch102:	0002-pahole-Honour-compile-when-C-is-used.patch
Patch103:	0003-emit-Check-if-disambiguated-struct-enum-union-name-w.patch
Patch104:	0004-emit-Don-t-mark-a-enum-with-nr_members-0-as-printed-.patch
Patch105:	0005-dwarves-support-DW_TAG_atomic_type.patch
Patch106:	0006-pahole-Allow-compile-to-work-with-DWARF-in-addition-.patch
Patch107:	0007-dwarf_loader-Support-DW_TAG_label-outside-DW_TAG_lex.patch
Patch108:	0008-pahole-Add-btf-to-the-format-path-option-man-page.patch
Patch109:	0009-pahole-Support-lang-lang_exclude-asm.patch
Patch110:	0010-btf_encoder-Add-extra-debug-info-for-unsupported-DWA.patch
Patch111:	0011-core-Print-more-info-on-tag__assert_search_result.patch
Patch112:	0012-fprintf-Emit-_Atomic-modifiers-for-DW_TAG_atomic_typ.patch
Patch113:	0013-btf_encoder-Store-the-CU-being-processed-to-avoid-ch.patch
Patch114:	0014-core-Add-DW_TAG_unspecified_type-to-tag__is_tag_type.patch
Patch115:	0015-core-Record-if-a-CU-has-a-DW_TAG_unspecified_type.patch
Patch116:	0016-btf_encoder-Encode-DW_TAG_unspecified_type-returning.patch
Patch117:	0017-emit-cu__type-NULL-means-void.patch
Patch118:	0018-emit-Emit-typedefs-for-atomic_-prefixed-base-types.patch
Patch119:	0019-emit-Optionally-pass-a-conf_fprintf-struct-to-type_e.patch
Patch120:	0020-emit-Allow-skip-emitting-the-atomic-typedefs.patch
Patch121:	0021-pahole-Allow-skipping-the-emission-of-atomic-typedef.patch
Patch122:	0022-fprintf-Move-the-typedef-invariant-printf-to-the-sta.patch
Patch123:	0023-fprintf-Support-_Atomic-typedefs.patch
Patch124:	0024-emit-Support-DW_TAG_atomic_type-when-emitting-defini.patch
Patch125:	0025-dwarves-Zero-initialize-struct-cu-in-cu__new-to-prev.patch
Patch126:	0026-core-Use-zalloc-to-make-the-code-more-robust.patch
Patch127:	0027-pahole-Use-zalloc-to-make-the-code-more-robust.patch
Patch128:	0028-pfunct-Use-zalloc-to-make-the-code-more-robust.patch
Patch129:	0029-dwarf_loader-DW_TAG_inlined_subroutine-needs-recodin.patch
Patch130:	0030-core-Introduce-base_type__language_defined.patch
Patch131:	0031-pahole-Use-type__fprintf-directly-for-compile.patch
Patch132:	0032-pahole-Set-libbpf-debug-printer-in-V-mode.patch
Patch133:	0033-dwarf_loader-Sync-with-LINUX_ELFNOTE_LTO_INFO-macro-.patch

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
