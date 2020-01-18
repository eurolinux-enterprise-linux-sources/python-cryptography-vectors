%global modname cryptography-vectors
%global pymodname cryptography_vectors

Name:               python-%{modname}
Version:            1.3.1
Release:            3%{?dist}
Summary:            Test vectors for the cryptography package

Group:              Development/Libraries
License:            ASL 2.0 or BSD
URL:                http://pypi.python.org/pypi/cryptography-vectors
Source0:            https://pypi.python.org/packages/source/c/%{modname}/cryptography_vectors-%{version}.tar.gz

BuildArch:          noarch
BuildRequires:      python2-devel python-setuptools
%if 0%{?fedora}
BuildRequires:      python3-devel python3-setuptools
%endif

%description
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.

%package -n  python2-%{modname}
Group:          Development/Libraries
Summary:        Test vectors for the cryptography package
Obsoletes:      python-cryptography-vectors <= %{version}-%{release}

%if 0%{?fedora}
%{?python_provide:%python_provide python2-%{modname}}
%else
Provides:       python-%{modname}
%endif

%description -n python2-%{modname}
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.

%if 0%{?fedora}
%package -n  python3-%{modname}
Group:          Development/Libraries
Summary:        Test vectors for the cryptography package

%{?python_provide:%python_provide python3-%{modname}}

%description -n python3-%{modname}
Test vectors for the cryptography package.

The only purpose of this package is to be a building requirement for
python-cryptography, otherwise it has no use. Don’t install it unless
you really know what you are doing.
%endif

%prep
%setup -q -n %{pymodname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build
%if 0%{?fedora}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
%if 0%{?fedora}
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}
%endif

%check
%{__python2} setup.py test
%if 0%{?fedora}
%{__python3} setup.py test
%endif

%files -n python2-%{modname}
%doc LICENSE
%{python2_sitelib}/%{pymodname}/
%{python2_sitelib}/%{pymodname}-%{version}*

%if 0%{?fedora}
%files -n python3-%{modname}
%doc LICENSE
%{python3_sitelib}/%{pymodname}/
%{python3_sitelib}/%{pymodname}-%{version}*
%endif


%changelog
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue May 10 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.3.1-2
- Clean up distro macros

* Tue May 03 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.3.1-1
- Update to v1.3.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-2
- Migrate python-cryptography-vectors => python2-cryptography-vectors

* Sat Jan 09 2016 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-1
- Update to v1.2.1

* Wed Nov 11 2015 Robert Kuska <rkuska@redhat.com> - 1.1-1
- Update to v1.1

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 1.0.2-2
- Rebuilt for Python3.5 rebuild

* Wed Sep 30 2015 Matěj Cepl <mcepl@redhat.com> - 1.0.2-1
- New upstream release (fix #1267548)

* Wed Aug 12 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.0-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 14 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.9-1
- New upstream release

* Fri Apr 17 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.8.2-1
- New upstream release

* Fri Mar 13 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.8-1
- New upstream release

* Wed Mar 04 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.7.2-2
- Add python3 subpackage

* Wed Mar 04 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.7.2-1
- New upstream release
- Now licensed under Apache 2.0 or BSD

* Thu Oct 16 2014 Matej Cepl <mcepl@redhat.com> - 0.6.1-1
- New upstream release (fixes among others #1153501)

* Wed Oct 01 2014 Matej Cepl <mcepl@redhat.com> - 0.5.4-3
- Add LICENSE file from the upstream repo.

* Mon Sep 29 2014 Matej Cepl <mcepl@redhat.com> - 0.5.4-2
- initial package for Fedora
