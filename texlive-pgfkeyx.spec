%global tl_name pgfkeyx
%global tl_revision 26093

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.1
Release:	%{tl_revision}.1
Summary:	Extended and more robust version of pgfkeys
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/pgfkeyx
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package extends and improves the robustness of the pgfkeys package.
In particular, it can deal with active comma, equality sign, and slash
in key parsing. The difficulty with active characters has long been a
problem with the pgfkeys package. The package also introduces handlers
beyond those that pgfkeys can offer.

