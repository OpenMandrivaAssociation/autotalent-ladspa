Name: autotalent-ladspa
Summary: Singer pitch correction LADSPA Plugin
Group: Sound
Version: 0.2
Release: %mkrel 1
License: GPLv2
Source: http://web.mit.edu/tbaran/www/autotalent-%{version}.tar.gz
URL: http://web.mit.edu/tbaran/www/autotalent.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Automatic pitch correction module for singers as LADSPA plugin.
You specify the notes that a singer is allowed to hit, and Autotalent 
makes sure that they do. You can also use Autotalent for more exotic 
effects, like the Cher / T-Pain effect, making your voice sound like a 
chiptune, adding artificial vibrato, or messing with your formants. 
Autotalent can also be used as a harmonizer that knows how to sing in 
the scale with you. Or, you can use Autotalent to change the scale of a 
melody between major and minor or to change the musical mode. 

%prep
%setup -q -n autotalent-%{version}

%build
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_libdir}/ladspa
install -m644 autotalent.so %{buildroot}%{_libdir}/ladspa/autotalent.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%{_libdir}/ladspa/autotalent.so
