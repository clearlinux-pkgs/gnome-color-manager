#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-color-manager
Version  : 3.32.0
Release  : 12
URL      : https://download.gnome.org/sources/gnome-color-manager/3.32/gnome-color-manager-3.32.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-color-manager/3.32/gnome-color-manager-3.32.0.tar.xz
Summary  : GNOME Color Profile Tools
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-color-manager-bin = %{version}-%{release}
Requires: gnome-color-manager-data = %{version}-%{release}
Requires: gnome-color-manager-libexec = %{version}-%{release}
Requires: gnome-color-manager-license = %{version}-%{release}
Requires: gnome-color-manager-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : exiv2-dev
BuildRequires : itstool
BuildRequires : pkgconfig(colord)
BuildRequires : pkgconfig(colord-gtk)
BuildRequires : pkgconfig(exiv2)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(lcms2)
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libexif)
BuildRequires : pkgconfig(libtiff-4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : vte-dev

%description
GNOME Color Manager
Color profile manager for the GNOME desktop
GNOME Color Manager is a session framework that makes it easy to manage, install
and generate color profiles in the GNOME desktop.

%package bin
Summary: bin components for the gnome-color-manager package.
Group: Binaries
Requires: gnome-color-manager-data = %{version}-%{release}
Requires: gnome-color-manager-libexec = %{version}-%{release}
Requires: gnome-color-manager-license = %{version}-%{release}

%description bin
bin components for the gnome-color-manager package.


%package data
Summary: data components for the gnome-color-manager package.
Group: Data

%description data
data components for the gnome-color-manager package.


%package doc
Summary: doc components for the gnome-color-manager package.
Group: Documentation

%description doc
doc components for the gnome-color-manager package.


%package libexec
Summary: libexec components for the gnome-color-manager package.
Group: Default
Requires: gnome-color-manager-license = %{version}-%{release}

%description libexec
libexec components for the gnome-color-manager package.


%package license
Summary: license components for the gnome-color-manager package.
Group: Default

%description license
license components for the gnome-color-manager package.


%package locales
Summary: locales components for the gnome-color-manager package.
Group: Default

%description locales
locales components for the gnome-color-manager package.


%prep
%setup -q -n gnome-color-manager-3.32.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557002130
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Denable-packagekit=false -Denable-exiv=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-color-manager
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-color-manager/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-color-manager

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gcm-calibrate
/usr/bin/gcm-import
/usr/bin/gcm-inspect
/usr/bin/gcm-picker
/usr/bin/gcm-viewer

%files data
%defattr(-,root,root,-)
/usr/share/applications/gcm-calibrate.desktop
/usr/share/applications/gcm-import.desktop
/usr/share/applications/gcm-picker.desktop
/usr/share/applications/org.gnome.ColorProfileViewer.desktop
/usr/share/gnome-color-manager/figures/viewer-example-00.png
/usr/share/gnome-color-manager/figures/viewer-example-01.png
/usr/share/gnome-color-manager/figures/viewer-example-02.png
/usr/share/gnome-color-manager/figures/viewer-example-03.png
/usr/share/gnome-color-manager/icons/calibration-long.svg
/usr/share/gnome-color-manager/icons/calibration-normal.svg
/usr/share/gnome-color-manager/icons/calibration-short.svg
/usr/share/gnome-color-manager/icons/clock.svg
/usr/share/gnome-color-manager/icons/icons/crt.svg
/usr/share/gnome-color-manager/icons/icons/lcd.svg
/usr/share/gnome-color-manager/icons/icons/projector.svg
/usr/share/gnome-color-manager/icons/scan-target-bad.svg
/usr/share/gnome-color-manager/icons/scan-target-good.svg
/usr/share/gnome-color-manager/icons/scan-target.svg
/usr/share/gnome-color-manager/targets/CMP-DigitalTarget3.png
/usr/share/gnome-color-manager/targets/CMP_DT_003.png
/usr/share/gnome-color-manager/targets/ColorChecker24.png
/usr/share/gnome-color-manager/targets/ColorCheckerDC.png
/usr/share/gnome-color-manager/targets/ColorCheckerSG.png
/usr/share/gnome-color-manager/targets/IT872.png
/usr/share/gnome-color-manager/targets/LaserSoftDCPro.png
/usr/share/gnome-color-manager/targets/QPcard_201.png
/usr/share/gnome-color-manager/targets/QPcard_202.png
/usr/share/gnome-color-manager/targets/i1_RGB_Scan_14.png
/usr/share/gnome-color-manager/targets/unknown.png
/usr/share/gnome-color-manager/ti1/display-long.ti1
/usr/share/gnome-color-manager/ti1/display-normal.ti1
/usr/share/gnome-color-manager/ti1/display-short.ti1
/usr/share/gnome-color-manager/ti1/printer-long.ti1
/usr/share/gnome-color-manager/ti1/printer-normal.ti1
/usr/share/gnome-color-manager/ti1/printer-short.ti1
/usr/share/icons/hicolor/16x16/apps/gnome-color-manager.png
/usr/share/icons/hicolor/22x22/apps/gnome-color-manager.png
/usr/share/icons/hicolor/24x24/apps/gnome-color-manager.png
/usr/share/icons/hicolor/256x256/apps/gnome-color-manager.png
/usr/share/icons/hicolor/32x32/apps/gnome-color-manager.png
/usr/share/icons/hicolor/48x48/apps/gnome-color-manager.png
/usr/share/icons/hicolor/64x64/apps/gnome-color-manager.png
/usr/share/icons/hicolor/scalable/apps/gnome-color-manager.svg
/usr/share/metainfo/org.gnome.ColorProfileViewer.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-color-manager/color-import-linux.page
/usr/share/help/C/gnome-color-manager/color-import-osx.page
/usr/share/help/C/gnome-color-manager/color-import-windows.page
/usr/share/help/C/gnome-color-manager/legal.xml
/usr/share/help/ca/gnome-color-manager/color-import-linux.page
/usr/share/help/ca/gnome-color-manager/color-import-osx.page
/usr/share/help/ca/gnome-color-manager/color-import-windows.page
/usr/share/help/ca/gnome-color-manager/legal.xml
/usr/share/help/cs/gnome-color-manager/color-import-linux.page
/usr/share/help/cs/gnome-color-manager/color-import-osx.page
/usr/share/help/cs/gnome-color-manager/color-import-windows.page
/usr/share/help/cs/gnome-color-manager/legal.xml
/usr/share/help/da/gnome-color-manager/color-import-linux.page
/usr/share/help/da/gnome-color-manager/color-import-osx.page
/usr/share/help/da/gnome-color-manager/color-import-windows.page
/usr/share/help/da/gnome-color-manager/legal.xml
/usr/share/help/de/gnome-color-manager/color-import-linux.page
/usr/share/help/de/gnome-color-manager/color-import-osx.page
/usr/share/help/de/gnome-color-manager/color-import-windows.page
/usr/share/help/de/gnome-color-manager/legal.xml
/usr/share/help/el/gnome-color-manager/color-import-linux.page
/usr/share/help/el/gnome-color-manager/color-import-osx.page
/usr/share/help/el/gnome-color-manager/color-import-windows.page
/usr/share/help/el/gnome-color-manager/legal.xml
/usr/share/help/es/gnome-color-manager/color-import-linux.page
/usr/share/help/es/gnome-color-manager/color-import-osx.page
/usr/share/help/es/gnome-color-manager/color-import-windows.page
/usr/share/help/es/gnome-color-manager/legal.xml
/usr/share/help/fi/gnome-color-manager/color-import-linux.page
/usr/share/help/fi/gnome-color-manager/color-import-osx.page
/usr/share/help/fi/gnome-color-manager/color-import-windows.page
/usr/share/help/fi/gnome-color-manager/legal.xml
/usr/share/help/fr/gnome-color-manager/color-import-linux.page
/usr/share/help/fr/gnome-color-manager/color-import-osx.page
/usr/share/help/fr/gnome-color-manager/color-import-windows.page
/usr/share/help/fr/gnome-color-manager/legal.xml
/usr/share/help/gl/gnome-color-manager/color-import-linux.page
/usr/share/help/gl/gnome-color-manager/color-import-osx.page
/usr/share/help/gl/gnome-color-manager/color-import-windows.page
/usr/share/help/gl/gnome-color-manager/legal.xml
/usr/share/help/hr/gnome-color-manager/color-import-linux.page
/usr/share/help/hr/gnome-color-manager/color-import-osx.page
/usr/share/help/hr/gnome-color-manager/color-import-windows.page
/usr/share/help/hr/gnome-color-manager/legal.xml
/usr/share/help/hu/gnome-color-manager/color-import-linux.page
/usr/share/help/hu/gnome-color-manager/color-import-osx.page
/usr/share/help/hu/gnome-color-manager/color-import-windows.page
/usr/share/help/hu/gnome-color-manager/legal.xml
/usr/share/help/it/gnome-color-manager/color-import-linux.page
/usr/share/help/it/gnome-color-manager/color-import-osx.page
/usr/share/help/it/gnome-color-manager/color-import-windows.page
/usr/share/help/it/gnome-color-manager/legal.xml
/usr/share/help/ko/gnome-color-manager/color-import-linux.page
/usr/share/help/ko/gnome-color-manager/color-import-osx.page
/usr/share/help/ko/gnome-color-manager/color-import-windows.page
/usr/share/help/ko/gnome-color-manager/legal.xml
/usr/share/help/ml/gnome-color-manager/color-import-linux.page
/usr/share/help/ml/gnome-color-manager/color-import-osx.page
/usr/share/help/ml/gnome-color-manager/color-import-windows.page
/usr/share/help/ml/gnome-color-manager/legal.xml
/usr/share/help/pl/gnome-color-manager/color-import-linux.page
/usr/share/help/pl/gnome-color-manager/color-import-osx.page
/usr/share/help/pl/gnome-color-manager/color-import-windows.page
/usr/share/help/pl/gnome-color-manager/legal.xml
/usr/share/help/pt_BR/gnome-color-manager/color-import-linux.page
/usr/share/help/pt_BR/gnome-color-manager/color-import-osx.page
/usr/share/help/pt_BR/gnome-color-manager/color-import-windows.page
/usr/share/help/pt_BR/gnome-color-manager/legal.xml
/usr/share/help/sv/gnome-color-manager/color-import-linux.page
/usr/share/help/sv/gnome-color-manager/color-import-osx.page
/usr/share/help/sv/gnome-color-manager/color-import-windows.page
/usr/share/help/sv/gnome-color-manager/legal.xml
/usr/share/help/zh_CN/gnome-color-manager/color-import-linux.page
/usr/share/help/zh_CN/gnome-color-manager/color-import-osx.page
/usr/share/help/zh_CN/gnome-color-manager/color-import-windows.page
/usr/share/help/zh_CN/gnome-color-manager/legal.xml
/usr/share/help/zh_HK/gnome-color-manager/color-import-linux.page
/usr/share/help/zh_HK/gnome-color-manager/color-import-osx.page
/usr/share/help/zh_HK/gnome-color-manager/color-import-windows.page
/usr/share/help/zh_HK/gnome-color-manager/legal.xml
/usr/share/help/zh_TW/gnome-color-manager/color-import-linux.page
/usr/share/help/zh_TW/gnome-color-manager/color-import-osx.page
/usr/share/help/zh_TW/gnome-color-manager/color-import-windows.page
/usr/share/help/zh_TW/gnome-color-manager/legal.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gcm-helper-exiv

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-color-manager/COPYING

%files locales -f gnome-color-manager.lang
%defattr(-,root,root,-)

