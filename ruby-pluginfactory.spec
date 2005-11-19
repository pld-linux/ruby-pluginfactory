Summary:	Ruby PluginFactory pattern
Summary(pl):	Wzorzec PluginFactory w Rubym
Name:		ruby-pluginfactory
Version:	1.0.1
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://www.deveiate.org/code/PluginFactory-%{version}.tar.gz
# Source0-md5:	fece540e184cdbabc395ef52e70833ff
Source1:	setup.rb
URL:		http://www.deveiate.org/code/PluginFactory.html
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
#BuildArch: noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby implementation of the PluginFactory pattern.

%description -l pl
Implementacja wzorca PluginFactory w j�zyku Ruby.

%prep
%setup -q -n PluginFactory-%{version}
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc lib --inline-source
rdoc --ri lib -o ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%{ruby_rubylibdir}/pluginfactory.rb
%{ruby_ridir}/*
