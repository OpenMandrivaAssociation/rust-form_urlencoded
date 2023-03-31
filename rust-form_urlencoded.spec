%bcond_without check
%global debug_package %{nil}

%global crate form_urlencoded

Name:           rust-%{crate}
Version:        1.0.1
Release:        2
Summary:        Parser and serializer for the application/x-www-form-urlencoded syntax, as used by HTML forms

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/form_urlencoded
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(matches/default) >= 0.1.0 with crate(matches/default) < 0.2.0)
BuildRequires:  (crate(percent-encoding/default) >= 2.1.0 with crate(percent-encoding/default) < 3.0.0)
%endif

%global _description %{expand:
Parser and serializer for the application/x-www-form-urlencoded syntax, as used
by HTML forms.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(form_urlencoded) = 1.0.1
Requires:       cargo
Requires:       (crate(matches/default) >= 0.1.0 with crate(matches/default) < 0.2.0)
Requires:       (crate(percent-encoding/default) >= 2.1.0 with crate(percent-encoding/default) < 3.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(form_urlencoded/default) = 1.0.1
Requires:       cargo
Requires:       crate(form_urlencoded) = 1.0.1

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
