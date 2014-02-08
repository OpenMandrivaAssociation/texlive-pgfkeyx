# revision 26093
# category Package
# catalog-ctan /macros/latex/contrib/pgfkeyx
# catalog-date 2012-04-21 23:54:26 +0200
# catalog-license lppl1.3
# catalog-version 0.0.1
Name:		texlive-pgfkeyx
Version:	0.0.1
Release:	3
Summary:	Extended and more robust version of pgfkeys
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pgfkeyx
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pgfkeyx.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.0.1-2
+ Revision: 813701
- Update to latest release.
- Import texlive-pgfkeyx
- Import texlive-pgfkeyx

