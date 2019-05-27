FILE=cv
LANG = $(lang)

all: $(FILE).pdf

$(FILE).pdf: link
	lualatex $(FILE).tex

link:
	ln -s ../yaac-another-awesome-cv.cls yaac-another-awesome-cv.cls || echo "yaac-another-awesome-cv exist"
	ln -s ../fonts fonts || echo "Symlink font exist"
	ln -s ../moi.png moi.png || echo "Symlink photo exist"

clean:
	rm -f ${FILE}.{lof,lol,lot,toc,ps,pdf,log,aux,out,dvi,bbl,blg,fdb_latexmk,fls,aux,out} *.log *.pdf
	find . -type l -delete
