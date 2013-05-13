Name: xclock
Version: 1.0.6
Release: 2
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


%changelog
* Mon Feb 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.6-1
+ Revision: 781030
- version update 1.0.6

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.5-2
+ Revision: 671283
- mass rebuild

* Fri Sep 24 2010 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 580823
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2010.1
+ Revision: 524383
- rebuilt for 2010.1

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2010.0
+ Revision: 448651
- new release

* Sat Mar 07 2009 Michael Scherer <misc@mandriva.org> 1.0.3-5mdv2009.1
+ Revision: 351548
- do not regerenate the configure script for no reason

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.3-4mdv2009.0
+ Revision: 226020
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 166452
- Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 155953
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 07 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.3-1mdv2008.0
+ Revision: 59574
- new upstream release: 1.0.3

