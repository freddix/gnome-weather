Summary:	GNOME weather
Name:		gnome-weather
Version:	3.12.0
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-weather/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	fa4121882f2cc8d94e7fa8e3a79bce03
URL:		https://live.gnome.org/Design/Apps/Weather
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	pkg-config
Requires(post,postun):	glib-gio-gsettings
Requires:	gjs >= 1.40.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/org.gnome.Weather.Application

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

%{__rm} $RPM_BUILD_ROOT%{_libexecdir}/libgd.la

%find_lang org.gnome.Weather.Application

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_gsettings_cache

%postun
%update_gsettings_cache

%files -f org.gnome.Weather.Application.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-weather
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/libgd.so
%{_libexecdir}/girepository-1.0
%{_datadir}/dbus-1/services/org.gnome.Weather.Application.service
%{_datadir}/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml
%{_datadir}/gnome-shell/search-providers/org.gnome.Weather.Application.search-provider.ini
%dir %{_datadir}/org.gnome.Weather.Application
%attr(755,root,root) %{_datadir}/org.gnome.Weather.Application/org.gnome.Weather.Application
%dir %{_datadir}/org.gnome.Weather.Application/gir-1.0
%{_datadir}/org.gnome.Weather.Application/gir-1.0/Gd-1.0.gir
%{_datadir}/org.gnome.Weather.Application/org.gnome.Weather.Application.data.gresource
%{_datadir}/org.gnome.Weather.Application/org.gnome.Weather.Application.src.gresource
%{_datadir}/org.gnome.Weather.Application/package.js

%{_desktopdir}/org.gnome.Weather.Application.desktop
%{_iconsdir}/hicolor/*/apps/org.gnome.Weather.Application.png

