%global tl_name showcharinbox
%global tl_revision 29803

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Show characters inside a box
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/showcharinbox
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/showcharinbox.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package typesets a character inside a box, showing where reference
point is, and displaying width, height, and depth information of the
character. The output is like that on page 63 of "The TeXBook" or page
101 of "The METAFONTbook". The package itself is motivated by Knuth's
macros in the file manmac.tex. Users should note that using a small size
for the character inside the box does not make any sense: use a large
size.

