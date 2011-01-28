
%define         _name kdmicons

Summary:	kdm user pictures - %{_name}
Summary(pl.UTF-8):	Obrazki użytkowników dla kdm-a - %{_name}
Name:		kdm-user-pictures-%{_name}
Version:	02
Release:	1
License:	GPL
Group:		Themes
Source0:	http://kde-look.org/content/files/21231-%{_name}.tar.gz
# Source0-md5:	b7fe87ac0ef049a6118e8c9eafab6586
URL:		http://www.kde-look.org/content/show.php?content=21231
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is icons of user avantars for kdm.

%description -l pl.UTF-8
%{_name} to ikony obrazków użytkowników dla kdm-a.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}
install %{_name}/*.png $RPM_BUILD_ROOT%{_datadir}/apps/kdm/pics/users/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/pics/users/%{_name}
