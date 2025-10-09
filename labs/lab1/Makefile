RMD_FILE = lab1-slides.Rmd
OUT_FILE = lab1-slides.pdf

all: render

render:
	Rscript -e "rmarkdown::render('$(RMD_FILE)', output_file='$(OUT_FILE)')"

clean:
	rm -f $(OUT_FILE)
