Name:		texlive-showcharinbox
Version:	29803
Release:	2
Summary:	Show characters inside a box
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showcharinbox
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package typesets a character inside a box, showing where
reference point is, and displaying width, height, and depth
information of the character. The output is like that on page
63 of "The TeXBook" or page 101 of "The METAFONTbook". The
package itself is motivated by Knuth's macros in the file
manmac.tex. Users should note that using a small size for the
character inside the box does not make any sense: use a large
size.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/showcharinbox/showcharinbox.sty
%doc %{_texmfdistdir}/doc/latex/showcharinbox/README
%doc %{_texmfdistdir}/doc/latex/showcharinbox/showcharinbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/showcharinbox/showcharinbox.dtx
%doc %{_texmfdistdir}/source/latex/showcharinbox/showcharinbox.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
