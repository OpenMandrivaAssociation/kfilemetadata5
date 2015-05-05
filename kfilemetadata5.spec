%define libname %{mklibname KF5FileMetaData 5}
%define devname %{mklibname KF5FileMetaData -d}
%define major %(echo %{version} |cut -d. -f1-3)
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define kdeversion %(echo %{version} |cut -d. -f1).%(expr $(echo %{version} |cut -d. -f2) - 4).%(echo %{version} |cut -d. -f3-)

Summary:	File metadata parsing library
Name:		kfilemetadata5
Version:	5.9.0
Release:	1
License:	LGPL
Group:		Graphical desktop/KDE
Url:		http://kde.org/
%if "%{stable}" == "stable"
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{kdeversion}/kfilemetadata-%{version}.tar.xz
%else
Source0:	ftp://ftp.kde.org/pub/kde/%{stable}/plasma/%{kdeversion}/kfilemetadata-%{version}.tar.xz
%endif
Source1000:	%{name}.rpmlintrc

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(FFmpeg)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	ebook-tools-devel
BuildRequires:	qmobipocket-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(Gettext)
BuildRequires:	ffmpeg-devel
Requires: %{libname} = %{EVRD}

%dependinglibpackage KF5FileMetaData 5
%{_libdir}/libKF5FileMetaData.so.3

%description
File metadata parsing library.

%files -f kfilemetadata.lang
%{_libdir}/cmake/KF5FileMetaData
# FIXME may want to split some not so commonly used plugins into subpackages
%dir %{_libdir}/qt5/plugins/kf5/kfilemetadata
%{_libdir}/qt5/plugins/kf5/kfilemetadata/kfilemetadata_*.so

%package -n %{devname}
Summary:	Development files for KFileMetaData
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for KFileMetaData.

%files -n %{devname}
%{_includedir}/KF5/KFileMetaData
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n kfilemetadata-%{major}
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kfilemetadata
