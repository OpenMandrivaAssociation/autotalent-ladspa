%define _disable_ld_no_undefined 1

Summary:	Singer pitch correction LADSPA Plugin
Name:		autotalent-ladspa
Group:		Sound
Version:	0.2
Release:	2
License:	GPLv2+
Url:		http://tombaran.info/autotalent.html
Source0:	http://tombaran.info/autotalent-%{version}.tar.gz
Patch0:		autotalent-0.2-makefile.patch

%description
Automatic pitch correction module for singers as LADSPA plugin.
You specify the notes that a singer is allowed to hit, and Autotalent 
makes sure that they do. You can also use Autotalent for more exotic 
effects, like the Cher / T-Pain effect, making your voice sound like a 
chiptune, adding artificial vibrato, or messing with your formants. 
Autotalent can also be used as a harmonizer that knows how to sing in 
the scale with you. Or, you can use Autotalent to change the scale of a 
melody between major and minor or to change the musical mode. 

%files
%{_libdir}/ladspa/autotalent.so

#----------------------------------------------------------------------------

%prep
%setup -q -n autotalent-%{version}
%patch0 -p1

%build
%setup_compile_flags
%make

%install
install -d %{buildroot}%{_libdir}/ladspa
install -m 0755 autotalent.so %{buildroot}%{_libdir}/ladspa/autotalent.so


