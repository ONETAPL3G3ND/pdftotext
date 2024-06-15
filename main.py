#https://github.com/ONETAPL3G3ND
import pdftotext
with open("doc.pdf", "rb") as file:
  pdf = pdftotext.PDF(file)

for page in pdf:
  print(page)
