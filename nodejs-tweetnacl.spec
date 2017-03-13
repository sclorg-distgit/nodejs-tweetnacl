%{?scl:%scl_package nodejs-tweetnacl}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name tweetnacl

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    0.14.3
Release:    2%{?dist}
Summary:    Port of TweetNaCl cryptographic library to JavaScript
License:    Public Domain
URL:        https://tweetnacl.js.org
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Port of TweetNaCl cryptographic library to JavaScript

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr nacl-fast.js nacl-fast.min.js nacl.js nacl.min.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

#Public Domain doesn't need license, but is specified in COPYING file
%doc COPYING.txt
%doc README.md

%changelog
* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.14.3-2
- Initial build

