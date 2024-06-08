import pdftotext
with open("doc.pdf", "rb") as file:
  pdf = pdftotext.PDF(file)

for page in pdf:
  print(page)
