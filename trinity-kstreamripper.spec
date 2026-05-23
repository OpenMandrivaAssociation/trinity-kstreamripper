%bcond clang 1

# TDE variables
%define tde_pkg kstreamripper
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Version:	14.1.6
Release:	1
Summary:	TDE frontend for streamripper
Group:		Applications/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/internet/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DPLUGIN_INSTALL_DIR="%{tde_prefix}/%{_lib}/trinity"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_NVCONTROL=OFF
BuildOption:    -DBUILD_ALL=ON -DBUILD_DOC=ON -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	fdupes


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KStreamRipper is a small frontend for the streamripper command
line utility. Streamripper captures internet shoutcast radio streams
on your harddisk and splits them up in mp3 files. KStreamRipper helps
you with managing/ripping your preferred streams.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Missing icon file will make this fail.
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop"

%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/kstreamripper
%{tde_prefix}/share/applications/tde/kstreamripper.desktop
%{tde_prefix}/share/apps/kstreamripper/
%{tde_prefix}/share/icons/hicolor/*/apps/kstreamripper.png
%{tde_prefix}/share/doc/tde/HTML/en/kstreamripper/
%{tde_prefix}/share/man/man*/kstreamripper.*

