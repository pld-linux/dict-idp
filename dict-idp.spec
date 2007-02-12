%define		dictname	IDP
%define		dict1		French
%define		dict2		German
%define		dict3		Italian
%define		dict4		Latin
%define		dict5	 	Portuguese
%define		dict6		Spanish
%define		dictionaries	%{dict1} %{dict2} %{dict3} %{dict4} %{dict5} %{dict6}

Summary:	The free dictionaries for dictd made from IDP project
Summary(pl.UTF-8):   Darmowe słowniki dla dictd z projektu IDP
Name:		dict-%{dictname}
Version:	19990219
# Last update on their site
Release:	3
License:	GPL
# is this '#This file is free to use and modify. Thank you for using the IDP.'
# compatible w/ Gnu GPL ???
Group:		Applications/Dictionaries
Source0:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
# Source0-md5:	893caf92b6b0bde075faa610cdcad162
Source1:	http://www.aracnet.com/~tyler/IDP/files/%{dict2}.txt
# Source1-md5:	2228f34eef12289a0aec6892e503fd1f
Source2:	http://www.aracnet.com/~tyler/IDP/files/%{dict3}.txt
# Source2-md5:	39637589eaed62612a97f721c8b42cab
Source3:	http://www.aracnet.com/~tyler/IDP/files/%{dict4}.txt
# Source3-md5:	eca10dc263c32ea0090c49cef70a3a5f
Source4:	http://www.aracnet.com/~tyler/IDP/files/%{dict5}.txt
# Source4-md5:	a90cd624de7c6afb5aea70153af05ad6
Source5:	http://www.aracnet.com/~tyler/IDP/files/%{dict6}.txt
# Source5-md5:	4a9b422b98e957627d3d143ab7f26743
#Source91:	http://www.wh9.tu-dresden.de/~heinrich/dict/dict_idp/idp2dict.sh
# copyright info:
Source98:	http://www.june29.com/IDP/IDPcopyright.html
# Source98-md5:	5128ae048e20870c549807eecd8031ac
Source99:	http://www.june29.com/IDP/IDPdisclaimer.html
# Source99-md5:	d2062ea10b27d0b4c59446600b3bb3b1
URL:		http://www.june29.com/IDP/
BuildRequires:	dictfmt
BuildRequires:	dictzip
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains The Internet Dictionary Project's dictionaries,
formatted for use by the dictionary server in the dictd package. The
Internet Dictionary Project's goal is to create royalty-free
translating dictionaries through the help of the Internet's citizens.
The IDP site allows individuals from all over the world to visit and
assist in the translation of English words into other languages. The
resulting lists of English words and their translated counterparts are
then made available through this site to anyone, with no restrictions
on their use.

%description -l pl.UTF-8
Ten pakiet zawiera darmowe słowniki z Internet Dictionary Project
sformatowane do użytku z serwerem słownika dictd. Celem Internet
Dictionary Project jest stworzenie wolnych od opłat słowników
tłumaczeń w oparciu o pomoc społeczności internetowej. Serwis IDP
pozwala ludziom z całego świata na pomoc przy tłumaczeniu angielskich
słów na inne języki. Powstałe w ten sposób listy angielskich słów i
ich tłumaczeń są udostępniane wszystkim, do nieograniczonego użytku.

%package %{dict1}
Summary:	The %{dict1} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict1} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict1}
This package contains %{dict1} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict1} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict1} do używania z serwerem słownika
dictd.

%package %{dict2}
Summary:	The %{dict2} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict2} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict2}
This package contains %{dict2} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict2} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict2} do używania z serwerem słownika
dictd.

%package %{dict3}
Summary:	The %{dict3} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict3} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict3}
This package contains %{dict3} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict3} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict3} do używania z serwerem słownika
dictd.

%package %{dict4}
Summary:	The %{dict4} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict4} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict4}
This package contains %{dict4} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict4} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict4} do używania z serwerem słownika
dictd.

%package %{dict5}
Summary:	The %{dict5} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict5} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict5}
This package contains %{dict5} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict5} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict5} do używania z serwerem słownika
dictd.

%package %{dict6}
Summary:	The %{dict6} dictionary for dictd
Summary(pl.UTF-8):   Słownik %{dict6} dla dictd
Group:		Applications/Dictionaries
Requires:	%{_sysconfdir}/dictd
Requires:	dictd

%description %{dict6}
This package contains %{dict6} dictionaries for use by the dictionary
server in the dictd package.

%description %{dict6} -l pl.UTF-8
Ten pakiet zawiera słownik %{dict6} do używania z serwerem słownika
dictd.

%prep
%setup -q -c -T
cp -f %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} %{SOURCE5} .

%build
echo "Making %{dictionaries}"
all_targets=""
for x in *.txt; do
	target=%{dictname}_`echo $x | cut -f1 -d.`
	all_targets="$all_targets $target"
	echo '%h 00-database-info' > $target
	echo '%d' >> $target
	grep '^#' $x >> $target
	grep -v '^#' $x | awk 'BEGIN{FS="\t"}{print "%h "$1; print "%d" ; print "\t"$2"\n" }' >> $target
done

for x in $all_targets ; do
	dictfmt -p -u "%url" -s "Internet Dictionary Project" $x < $x
	dictzip $x.dict
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

for i in %{dictionaries}; do
	dictprefix=%{_datadir}/dictd/%{dictname}_$i
	echo "# The Internet Dictionary Project dictionaries
database $i {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
	mv %{dictname}_$i.* $RPM_BUILD_ROOT%{_datadir}/dictd
done

%clean
rm -rf $RPM_BUILD_ROOT

%post %{dict1}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict1}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict2}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict2}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict3}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict3}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict4}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict4}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict5}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict5}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict6}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict6}
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files %{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict1}.*

%files %{dict2}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict2}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict2}.*

%files %{dict3}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict3}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict3}.*

%files %{dict4}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict4}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict4}.*

%files %{dict5}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict5}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict5}.*

%files %{dict6}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict6}.*
