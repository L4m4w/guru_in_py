"""
- Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;

– Положить его в ресурсы;

– Реализовать тесты на чтение и проверку содержимого каждого файла из архива
"""

import os
from zipfile import ZipFile, ZIP_DEFLATED

path = os.getcwd() + '/resources/'

attachments = os.listdir(path)

with ZipFile(path + 'small_zip.zip','w', ZIP_DEFLATED) as zf:
    for attach in attachments:
        add_attach = os.path.join(path, attach)
        zf.write(add_attach, arcname=attach)


def archive_open():
    with ZipFile(path + 'small_zip.zip', 'r') as zf:
        for file in zf.infolist():
            print(os.path.basename(file.filename))


def test_csv_in_archive():
    test_object = 'small_csv.csv'
    with ZipFile(path + 'small_zip.zip', "r") as zf:

        assert b"Hello, darling. How are you?" in zf.read(test_object)


def test_pdf_in_archive():
    with ZipFile(path + 'small_zip.zip', "r") as zf:

        assert b"thahks" in zf.read('small_pdf.pdf')


def test_xlsx_in_archive():
    test_object = 'small_xlsx.xlsx'
    with ZipFile(path + 'small_zip.zip', "r") as zf:

        assert b"Me too" in zf.read(test_object)[:6]

