Name:		texlive-biblist
Version:	17116
Release:	2
Summary:	Print a BibTeX database
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex209/contrib/biblist
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblist.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
