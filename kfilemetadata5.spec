%define libname %{mklibname KF5FileMetaData 5}
%define devname %{mklibname KF5FileMetaData -d}

Summary:	File metadata parsing library
Name:		kfilemetadata5
Version:	5.0.0
Release:	1
License:	LGPL
Group:		Graphical desktop/KDE
Url:		http://kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{version}/kfilemetadata-%{version}.tar.xz
Source1000:	%{name}.rpmlintrc

BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(Taglib)
BuildRequires:	cmake(Exiv2)
BuildRequires:	cmake(FFmpeg)
BuildRequires:	ebook-tools-devel
BuildRequires:	qmobipocket-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake

Requires: %{libname} = %{EVRD}

%libpackage KF5FileMetaData 5
%{_libdir}/libKF5FileMetaData.so.1

%description
File metadata parsing library

%files
%{_datadir}/kservicetypes5/*.desktop
%{_datadir}/kservices5/*.desktop
%{_libdir}/cmake/KF5FileMetaData
# FIXME may want to split some not so commonly used plugins into subpackages
%{_libdir}/plugins/kfilemetadata_*.so

%package -n %{devname}
Summary:	Development files for KFileMetaData
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Development files for KFileMetaData

%files -n %{devname}
%{_includedir}/KF5/KFileMetaData
%{_libdir}/*.so

#----------------------------------------------------------------------------

%prep
%setup -q -n kfilemetadata-%{version}

%build
%cmake
%make

%install
%makeinstall_std -C build

