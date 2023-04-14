import PyPDF2

pdf = open('exemplo.pdf', 'rb')

# lendo pdf
pdflendo = PyPDF2.PdfFileReader(pdf)

page = pdflendo.getPage(0)
# extraindo o texto
text = page.extractText()

# exibindo pdf
print(text)
