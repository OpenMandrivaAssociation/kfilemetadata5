%define libname %{mklibname KF5FileMetaData 5}
%define devname %{mklibname KF5FileMetaData -d}

Summary:	File metadata parsing library
Name:		kfilemetadata5
Version:	5.29.0
Release:	1
License:	LGPL
Group:		Graphical desktop/KDE
Url:		http://kde.org/
Source0:	http://download.kde.org/stable/frameworks/%(echo %{version} |cut -d. -f1-2)/kfilemetadata-%{version}.tar.xz
Source1000:	%{name}.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	ebook-tools-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(Gettext)
BuildRequires:	ffmpeg-devel
BuildRequires:	attr-devel
Requires: %{libname} = %{EVRD}

%dependinglibpackage KF5FileMetaData 5
%{_libdir}/libKF5FileMetaData.so.3

%description
File metadata parsing library.

%files -f kfilemetadata.lang
# FIXME may want to split some not so commonly used plugins into subpackages
%dir %{_libdir}/qt5/plugins/kf5/kfilemetadata
%dir %{_libdir}/qt5/plugins/kf5/kfilemetadata/writers
%{_libdir}/qt5/plugins/kf5/kfilemetadata/kfilemetadata_*.so
%{_libdir}/qt5/plugins/kf5/kfilemetadata/writers/kfilemetadata_*.so

%package -n %{devname}
Summary:	Development files for KFileMetaData
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 5.13.0-2

%description -n %{devname}
Development files for KFileMetaData.

%files -n %{devname}
%{_libdir}/cmake/KF5FileMetaData
%{_includedir}/KF5/KFileMetaData
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n kfilemetadata-%{version}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kfilemetadata
