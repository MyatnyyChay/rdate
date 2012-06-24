Summary:	Remote clock reader (and local setter)
Summary(de):	Entfernter Uhrenleser (lokaler Einsteller)
Summary(es):	Lector de reloj remoto (y ajuste local)
Summary(fr):	Lecteur d'horloge distante (et configurateur local)
Summary(pl):	Program podaj�cy (i ustawiaj�cy) zdalny czas zegara
Summary(pt_BR):	Leitor de rel�gio remoto (e ajustador local)
Summary(ru):	��������� ��� ������ ��������� ����� � ��������� �� ��� �������
Summary(tr):	A� �zerinden sistem saatini ayarlayan yaz�l�m
Name:		rdate
Version:	1.3
Release:	8
License:	GPL
Group:		Networking/Utilities
Source0:	ftp://people.redhat.com/sopwith/%{name}-%{version}.tar.gz
# Source0-md5: 67da8370335ad0ca7c82cdbe1c82976e
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.cron
Patch0:		%{name}-segfault.patch
Patch1:		%{name}-ipv6.patch
Requires(post,postun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	rdate-bsd

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

%description -l es
Rdate es un programa que puede retornar el tiempo (fecha/hora) de otra
m�quina en tu red. Si le ejecutas como root, tambi�n configurar� el
tiempo local como el de la m�quina solicitada. No es muy riguroso;
coge xntpd, si realmente te preocupa los milisegundos.

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

%description -l pt_BR
Rdate � um programa que pode retornar o tempo (data/hora) de outra
m�quina na sua rede. Se rodar como root, ele tamb�m ir� configurar o
hora local como o da m�quina requisitada. Ele n�o � super preciso;
pegue xntpd se voc� realmente se preocupa com milisegundos.

%description -l ru
������� rdate ��������� ���� � ����� � ������ ������ ����� ����
��������� �������� ��������� � RFC 868. ���� �� ���������� rdate ��
������������ root, ��� ����� ����� ���������� ����� �� ���������
������ � ������������ �� �������� �� ��������� ������. ������ � ����,
��� rdate �� ���������� ��������� ���������; ���� �� ���������� �
�������������, ���������� ����� xntp3, ���������� ������ xntpd.

%description -l tr
rdate ile herhangi ba�ka bir makinadan sistem saatini sorgulanabilir.
Yetkili kullan�c� taraf�ndan �al��t�r�l�rsa sistem saatini ayarlamak
da m�mk�nd�r. Ne var ki bu uygulama �ok hassas de�ildir.

%description -l uk
���̦�� rdate �����դ ���� �� ��� � ���ϧ ������ � ��ۦ� ����֦,
�������������� �������� �������� � RFC 868. ���� �� ���������� rdate
צ� ����������� root, ���� ����� ���� ���������� ��� �� ������Φ�
����Φ � צ���צ����Ԧ �� ����� �� צ�����Φ� ����Φ. ����� �� ���ڦ,
�� rdate �� צ�Ҧ��Ѥ���� ��������� ���Φ���; ���� �� ����դ���� ���
̦ͦ�������, ������צ�� ����� xntp3, ���� ������� ������ xntpd.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} clean
%{__make} CFLAGS="-DINET6 %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,/etc/{cron.daily,rc.d/init.d,sysconfig}}

install rdate $RPM_BUILD_ROOT%{_bindir}
install rdate.1 $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/%{name}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/%{name}
install %{SOURCE3} $RPM_BUILD_ROOT/etc/cron.daily/%{name}

%post
/sbin/chkconfig --add rdate

%preun
if [ "$1" = "0" ]; then
	/sbin/chkconfig --del rdate
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rdate
%attr(755,root,root) /etc/rc.d/init.d/%{name}
%attr(755,root,root) /etc/cron.daily/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%{_mandir}/man1/*
