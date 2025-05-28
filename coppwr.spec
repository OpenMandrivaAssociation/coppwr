%global debug_package %{nil}

Name:		coppwr
Version:	1.6.2
Release:	1
Source0:	https://github.com/dimtpap/coppwr/archive/%{version}/%{name}-%{version}.tar.gz
Source1:    %{name}-%{version}-vendor.tar.gz
Summary:	Low level control GUI for the PipeWire multimedia server
URL:		https://github.com/dimtpap/coppwr
License:	GPL-3.0
Group:		Application/Audio
BuildRequires:	cargo
BuildRequires:	pkgconfig(libpipewire-0.3)

%description
%summary.

%prep
%autosetup -p1
tar -zxf %{S:1}
mkdir -p .cargo
cat >> .cargo/config.toml << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source."git+https://github.com/dimtpap/egui_node_graph.git?rev=6e6f764c5ff98a5b97dbc95e1a9d4b3c85436603"]
git = "https://github.com/dimtpap/egui_node_graph.git"
rev = "6e6f764c5ff98a5b97dbc95e1a9d4b3c85436603"
replace-with = "vendored-sources"

[source."git+https://gitlab.freedesktop.org/dimtpap/pipewire-rs.git?rev=605d15996f3258b3e1cc34e445dfbdf16a366c7e"]
git = "https://gitlab.freedesktop.org/dimtpap/pipewire-rs.git"
rev = "605d15996f3258b3e1cc34e445dfbdf16a366c7e"
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

EOF

%build
cargo build --frozen --release

%install
install -dm0775 %{buildroot}%{_bindir}
install -Dm0775 target/release/%{name} %{buildroot}%{_bindir}/

%files
%license LICENSE
%{_bindir}/%{name}
