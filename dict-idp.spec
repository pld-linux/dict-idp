%define	dictname    IDP
%define	dict1	French
%define	dict2	German
%define	dict3	Italian
%define	dict4	Latin
%define	dict5 	Portuguese
%define	dict6 	Spanish
%define   dictionaries %{dict1} %{dict2} %{dict3} %{dict4} %{dict5} %{dict6}

Summary:	The Free dictionaries for dictd made from IDP project
Summary(pl):	Darmowe S這wniki dla dictd z projektu IDP
Name:		dict-%{dictname}
Version:	19990219
# Last update on their site
Release:	1
License:	GPL
# is this '#This file is free to use and modify.  Thank you for using the IDP.'
# compatible w/ Gnu GPL ???
Group:		Applications/Dictionaries
Source1:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
Source2:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
Source3:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
Source4:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
Source5:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
Source6:	http://www.aracnet.com/~tyler/IDP/files/%{dict1}.txt
#Source91:   www.wh9.tu-dresden.de/%7Eheinrich/dict/dict_idp/idp2dict.sh
# copyright info:
Source98:	http://www.june29.com/IDP/IDPcopyright.html
Source99:	http://www.june29.com/IDP/IDPdisclaimer.html
URL:		http://www.june29.com/IDP/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	dictzip
BuildRequires:	autoconf
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description
This package contains The Internet Dictionary Project's dictionaries,
version %version formatted for use by the dictionary server in the
dictd package. The Internet Dictionary Project's goal is to create
royalty-free translating dictionaries through the help of the
Internet's citizens. This site allows individuals from all over the
world to visit and assist in the translation of English words into
other languages. The resulting lists of English words and their
translated counterparts are then made available through this site to
anyone, with no restrictions on their use. Please enjoy your visit,
and thank you for donating your time to this project.

%description -l pl
Ten pakiet zawiera darmowe s這wniki z Internet Dictionary Project w
wersji %version sformatowane do u篡tku z serwerem s這wnika dictd.

%package %{dict1}
Summary:	The %{dict1} Dictionary for dictd
Summary(pl):	S這wnik %{dict1} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict1}
This package contains %{dict1} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict1} -l pl
Ten pakiet zawiera s這wnik %{dict1} do u篡wania z serwerem s這wnika
dictd.

%package %{dict2}
Summary:	The %{dict2} Dictionary for dictd
Summary(pl):	S這wnik %{dict2} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict2}
This package contains %{dict2} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict2} -l pl
Ten pakiet zawiera s這wnik %{dict2} do u篡wania z serwerem s這wnika
dictd.

%package %{dict3}
Summary:	The %{dict3} Dictionary for dictd
Summary(pl):	S這wnik %{dict3} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict3}
This package contains %{dict3} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict3} -l pl
Ten pakiet zawiera s這wnik %{dict3} do u篡wania z serwerem s這wnika
dictd.

%package %{dict4}
Summary:	The %{dict4} Dictionary for dictd
Summary(pl):	S這wnik %{dict4} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict4}
This package contains %{dict4} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict4} -l pl
Ten pakiet zawiera s這wnik %{dict4} do u篡wania z serwerem s這wnika
dictd.

%package %{dict5}
Summary:	The %{dict5} Dictionary for dictd
Summary(pl):	S這wnik %{dict5} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict5}
This package contains %{dict5} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict5} -l pl
Ten pakiet zawiera s這wnik %{dict5} do u篡wania z serwerem s這wnika
dictd.

%package %{dict6}
Summary:	The %{dict6} Dictionary for dictd
Summary(pl):	S這wnik %{dict6} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict6}
This package contains %{dict6} dictionaries for use by the dicitonary
server in the dictd package.

%description %{dict6} -l pl
Ten pakiet zawiera s這wnik %{dict6} do u篡wania z serwerem s這wnika
dictd.

%package %{dict7}
Summary:	The %{dict7} Dictionary for dictd
Summary(pl):	S這wnik %{dict7} dla dictd
Group:		Applications/Dictionaries
Requires:	dictd
Requires:	%{_sysconfdir}/dictd

%description %{dict7}
This package contains %{dict7} dictionaries for use by the dicitonary
server in the dictd package.

%setup
mkdir idp
cp %{Source1} idp/
cp %{Source2} idp/
cp %{Source3} idp/
cp %{Source4} idp/
cp %{Source5} idp/
cp %{Source6} idp/

%build
echo "Making %{dictionaries}"
all_targets=""
for x in *.txt ; do
    target=idp_`echo $x | cut -f1 -d.`
    all_targets=$all_targets" "$target
    echo '%h 00-database-info' > $target
    echo '%d' >> $target
    grep '^#' $x >> $target
    grep -v '^#' $x | awk 'BEGIN{FS="\t"}{print "%h "$1; print "%d" ; print "\t"$2"\n" }' >> $target
done

for x in $all_targets ; do
    dictfmt -p -u "%{URL}" -s "Internet Dictionary Project"  $x < $x
    dictzip  $x'.dict'
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}

for i in %{dictionaries}; do
  dictprefix=%{_datadir}/dictd/%{dictname}_$i
  echo "# The Internet Dictionary Project dictionaries
  database $i {
    data \"$dictprefix.dict.dz\"
    index \"$dictprefix.index\"
  }
  " > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}-$i.dictconf
  install %{dictname}_$i* $RPM_BUILD_ROOT%{_datadir}/dictd/
done

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict1}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict1}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi

%postun %{dict2}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict2}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun %{dict3}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict3}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun %{dict4}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict4}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun %{dict5}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict5}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun %{dict6}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict6}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi
%postun %{dict7}
if [ -f /var/lock/subsys/dictd ]; then
/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post %{dict7}
  if [ -f /var/lock/subsys/dictd ]; then
  /etc/rc.d/init.d/dictd restart 1>&2
fi

%files %{dict1}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict1}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict1}*

%files %{dict2}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict2}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict2}*

%files %{dict3}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict3}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict3}*

%files %{dict4}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict4}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict4}*

%files %{dict5}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict5}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict5}*

%files %{dict6}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict6}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict6}*

%files %{dict7}
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}-%{dict7}.dictconf
%{_datadir}/dictd/%{dictname}_%{dict7}*
