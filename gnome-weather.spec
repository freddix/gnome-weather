Summary:	GNOME weather
Name:		gnome-weather
Version:	3.8.0
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-weather/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	f4e34d19aed2d780840cb7af02698482
URL:		https://live.gnome.org/Design/Apps/Weather
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-weather

%description
GNOME weather.

%prep
%setup -q

%build
%configure \
	GJS="%{_bindir}/gjs"		\
	--disable-schemas-compile	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/libgd.so
%{_libexecdir}/girepository-1.0
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%{_datadir}/gnome-weather
%{_desktopdir}/gnome-weather.desktop

