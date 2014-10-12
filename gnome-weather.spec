Summary:	GNOME weather
Name:		gnome-weather
Version:	3.14.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-weather/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	4d9abb509f64a9aa41e3a1cc6cef701a
URL:		https://live.gnome.org/Design/Apps/Weather
BuildRequires:	gobject-introspection-devel >= 1.42.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires:	gjs >= 1.42.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%find_lang org.gnome.Weather

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f org.gnome.Weather.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%{_datadir}/dbus-1/services/org.gnome.Weather.Application.service
%{_datadir}/dbus-1/services/org.gnome.Weather.BackgroundService.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.Application.search-provider.ini
%dir %{_datadir}/org.gnome.Weather
%attr(755,root,root) %{_datadir}/org.gnome.Weather/org.gnome.Weather.Application
%attr(755,root,root) %{_datadir}/org.gnome.Weather/org.gnome.Weather.BackgroundService
%{_datadir}/org.gnome.Weather/*.gresource

%{_desktopdir}/org.gnome.Weather.Application.desktop
%{_iconsdir}/hicolor/*/apps/org.gnome.Weather.Application.png

