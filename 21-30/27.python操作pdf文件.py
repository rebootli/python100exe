#pip install PyPDF2

import PyPDF2

reader = PyPDF2.PdfReader('test.pdf')
for page in reader.pages:
    print(page.extract_text())