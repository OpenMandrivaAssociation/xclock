Name: xclock
Version: 1.0.3
Release: %mkrel 2
Summary: analog / digital clock for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libxaw-devel	>= 1.0.4
BuildRequires: libxrender-devel >= 0.9.4
BuildRequires: xft2-devel	>= 2.1.12
BuildRequires: libxkbfile-devel	>= 1.0.4

%description
The xclock program displays the time in analog or digital form. The time is
continuously updated at a frequency which may be specified by the user.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock-color
%{_datadir}/X11/app-defaults/XClock
%{_mandir}/man1/xclock.1*
