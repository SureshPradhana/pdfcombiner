import PyPDF2
import sys
 
inputs =sys.argv[1:]
merger=PyPDF2.PdfFileMerger()
def pdf_combiner(pdflist):
	for pdf in pdflist:
		merger.append(pdf)
	merger.write("super.pdf")
pdf_combiner(inputs)
