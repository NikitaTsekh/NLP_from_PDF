# import PyPDF2
# from langdetect import detect
#
# def text():
#     pdf_file = open('Documents/1_EN.pdf', 'rb')
#     pdf_file = open('Documents/2_RU.pdf', 'rb')
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     page_obj = pdf_reader.pages[0] # 0-based index
#
#     text = page_obj.extract_text()
#     pdf_file.close()
#     detected_lang = detect(text)
#     print(detected_lang)
#     return text
#
# print(text())


import PyPDF2
from langdetect import detect

def text():
    pdf_file = open('Documents/1_EN.pdf', 'rb')
    pdf_file = open('Documents/2_RU.pdf', 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]
        text += page_obj.extract_text()
    pdf_file.close()
    detected_lang = detect(text)
    print(detected_lang)
    return text

print(text())