%define _disable_lto 1

Name: xclock
Version: 1.0.8
Release: 1
Summary: analog / digital clock for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: pkgconfig(xaw7) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: pkgconfig(xrender) >= 0.9.0
BuildRequires: pkgconfig(xft) >= 2.1.8.2
BuildRequires: pkgconfig(xkbfile) >= 1.0.1
BuildRequires: gettext-devel


%description
The xclock program displays the time in analog or digital form. The time is
continuously updated at a frequency which may be specified by the user.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/xclock
%{_datadir}/X11/app-defaults/XClock-color
%{_datadir}/X11/app-defaults/XClock
%{_mandir}/man1/xclock.1*
