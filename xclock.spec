Name: xclock
Version: 1.0.6
Release: 1
Summary: analog / digital clock for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxrender-devel >= 0.9.0
BuildRequires: pkgconfig(xft) >= 2.1.8.2
BuildRequires: libxkbfile-devel >= 1.0.1

%description
The xclock program displays the time in analog or digital form. The time is
continuously updated at a frequency which may be specified by the user.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock-color
%{_datadir}/X11/app-defaults/XClock
%{_mandir}/man1/xclock.1*
