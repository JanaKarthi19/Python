from heapq import merge

import PyPDF2
import sys



#     --PDF Merger--
def pdf_merger():
    merger = PyPDF2.PdfWriter()

    ar = open(sys.argv[1],'rb')
    br = open(sys.argv[2],'rb')

    for pdf in [ar, br]:
        merger.append(pdf)

    merger.write(sys.argv[3])
    merger.close()

pdf_merger()


#      --Water Mark--
#
template = PyPDF2.PdfReader(open('Orginal.pdf','rb'))
watermark = PyPDF2.PdfReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfWriter()



for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

file = open('Watermarked.pdf','wb')
output.write(file)
