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

#TODO: すべてのPDFファイルをループする

#TODO: 先頭を除く全てのページをループして追加する

#TODO: 統合したPDFをファイルに保存する