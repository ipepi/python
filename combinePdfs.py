#! python3
# combinePdf.py - カレントディレクトリの全PDFを一つのPDFをに統合する

import PyPDF2, os

#すべてのPDFファイル名を取得する

pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)

pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

#すべてのPDFファイルをループする
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    #先頭を除く全てのページをループして追加する
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

#TODO: 統合したPDFをファイルに保存する