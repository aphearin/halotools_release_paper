tex :
	pdflatex halotools

all :
	pdflatex halotools
	bibtex halotools
	pdflatex halotools
	pdflatex halotools
	pdflatex halotools
	open halotools.pdf


clean :
	-rm *.aux *.bbl *.log *.synctex.gz *.blg
