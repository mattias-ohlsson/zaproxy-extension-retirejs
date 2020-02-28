%global commit ba5fac0d22a30381bb79c3900e9bff35a9c01726
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global extension_id retirejs
%global extension_name Retire.js
%global extension_info Identify vulnerable JavaScript libraries.
%global extension_status alpha
%global addon_folder %{extension_id}

Name:           zaproxy-extension-%{extension_id}
Version:        3.0.0
Release:        1%{?dist}
Summary:        %{extension_name} extension

License:        ASL 2.0
URL:            https://github.com/h3xstream/burp-retire-js
Source0:        https://github.com/h3xstream/burp-retire-js/archive/%{commit}/burp-retire-js-%{shortcommit}.tar.gz
BuildArch:      noarch

BuildRequires:  maven
Requires:       zaproxy

%description
%{extension_info}

%prep
%autosetup -n burp-retire-js-%{commit}

%build
mvn package

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/zaproxy/plugin

install -m 644 -D retirejs-zap-plugin/target/retirejs-alpha-3.jar \
 %{buildroot}%{_datadir}/zaproxy/plugin/%{extension_id}-%{extension_status}-%{version}.zap

%files
%license LICENSE
%doc README.md
%{_datadir}/zaproxy/plugin/*-%{version}.zap

%changelog
* Fri Feb 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.0.0-1
- Initial build
