#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Summary:	Tool for adjusting KDE debug settings
Name:		kdebugsettings
Version:	25.04.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kdebugsettings/-/archive/%{gitbranch}/kdebugsettings-%{gitbranchd}.tar.bz2#/kdebugsettings-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdebugsettings-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Designer)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6NewStuff)
BuildRequires:	cmake(KF6Parts)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	pkgconfig(shared-mime-info)

%description
Tool for adjusting KDE debug settings

%files -f kdebugsettings.lang
%{_datadir}/qlogging-categories6/kdebugsettings.categories
%{_datadir}/qlogging-categories6/kde.renamecategories
%{_bindir}/kdebugsettings
%{_datadir}/applications/org.kde.kdebugsettings.desktop
%{_datadir}/metainfo/org.kde.kdebugsettings.appdata.xml
%{_datadir}/kdebugsettings
# No need to build a separate lib package because this is internal.
# No headers shipped, so it won't be used by anything else.
%{_libdir}/libkdebugsettings.so*
%{_libdir}/libkdebugsettingscore.so*

%prep
%autosetup -p1 -n kdebugsettings-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kdebugsettings
