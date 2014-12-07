# revision 17116
# category Package
# catalog-ctan /macros/latex209/contrib/biblist
# catalog-date 2010-02-21 11:42:27 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-biblist
Version:	20100221
Release:	9
Summary:	Print a BibTeX database
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/biblist
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblist.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of listing an entire BibTeX
database, avoiding the potentially large (macro) impact
associated with \nocite{*}.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblist/biblist.sty
%doc %{_texmfdistdir}/doc/latex/biblist/README
%doc %{_texmfdistdir}/doc/latex/biblist/biblist.bst-dist
%doc %{_texmfdistdir}/doc/latex/biblist/biblist.gde
%doc %{_texmfdistdir}/doc/latex/biblist/biblist.pdf
%doc %{_texmfdistdir}/doc/latex/biblist/biblist.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100221-2
+ Revision: 749692
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100221-1
+ Revision: 717938
- texlive-biblist
- texlive-biblist
- texlive-biblist
- texlive-biblist
- texlive-biblist

