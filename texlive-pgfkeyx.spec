Name:		texlive-pgfkeyx
Version:	26093
Release:	2
Summary:	Extended and more robust version of pgfkeys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfkeyx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package extends and improves the robustness of the pgfkeys
package. In particular, it can deal with active comma, equality
sign, and slash in key parsing. The difficulty with active
characters has long been a problem with the pgfkeys package.
The package also introduces handlers beyond those that pgfkeys
can offer.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pgfkeyx/pgfkeyx.sty
%doc %{_texmfdistdir}/doc/latex/pgfkeyx/README
%doc %{_texmfdistdir}/doc/latex/pgfkeyx/pgfkeyx-test1.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
