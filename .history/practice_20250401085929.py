f=open('/icons/list.pdf','rb')
pdf_reader=PyPDF2.PdfReader(f)

page_number=0
page_one=pdf_reader.pages[0]

pdf_writer=PyPDF2.PdfWriter()