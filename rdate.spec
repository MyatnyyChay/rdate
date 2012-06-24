Summary:	Remote clock reader (and local setter)
Summary(fr):	Lecteur d'horloge distante (et configurateur local)
Summary(de):	Entfernter Uhrenleser (lokaler Einsteller)
Summary(pl):	Program podaj�cy (i ustawiaj�cy) zdalny czas zegara
Summary(tr):	A� �zerinden sistem saatini ayarlayan yaz�l�m
Name:		rdate
%define		versionmajor 0
%define		versionminor 990821
Version:	%{versionmajor}.%{versionminor}
Release:	2
License:	none
Group:		Networking/Utilities
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/misc/%{name}-%{versionminor}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdate is a program that can retrieve the time from another machine on
your network. If run as root, it will also set your local time to that
of the machine you queried. It is not super accurate; get ntpd if you
are really worried about milliseconds.

%description -l de
rdate ist ein Programm, das die Uhrzeit von einem anderen
Netzwerkrechner lesen kann. Wenn Sie es als root ausf�hren, stellt es
Ihre Ortszeit auf die des abgefragten Rechners ein. Es ist nicht sehr
genau. Wenn Sie auf die Millisekunde genau sein wollen, besorgen Sie
sich ntpd.

%description -l fr
rdate permet de r�cup�rer l'heure d'une autre machine du r�seau. s'il
est lanc� par root, il configurera aussi votre heure locale avec celle
de la machine que vous avez interrog�. Il n'est pas tr�s pr�cis ; si
vous vous souciez des millisecondes, r�cup�rez ntpd.

%description -l pl
rdate jest programem kt�ry odczytuje dat� i godzin� z innej maszyny w
sieci. Je�eli jest uruchamiany jako root mo�e tak�e s�u�y� do
synchronizacji lokalnego czasu wzgl�dem innego komputera w sieci. Nie
jest zbyt dok�adny i je�eli milisekundy maj� dla nas znaczenie nale�y
u�y� ntpd.

%description -l tr
rdate ile herhangi ba�ka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullan�c� taraf�ndan �al��t�r�l�rsa sistem saatini ayarlamak
da m�mk�nd�r. Ne var ki bu uygulama �ok hassas de�ildir.

%prep
%setup -q -n %{name}-%{versionminor}

%build
%{__make} clean
%{__make} CFLAGS="-DINET6 %{rpmcflags}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install rdate $RPM_BUILD_ROOT%{_bindir}
install rdate.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdate
%{_mandir}/man1/*
