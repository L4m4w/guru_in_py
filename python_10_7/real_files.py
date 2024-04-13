"""
- Запаковать в zip архив несколько разных файлов: pdf, xlsx, csv;

– Положить его в ресурсы;

– Реализовать тесты на чтение и проверку содержимого каждого файла из архива
"""

import os
from zipfile import ZipFile, ZIP_DEFLATED

path = os.getcwd() + '/attachments/'

attachments = os.listdir(path)

# print(attachments)

with ZipFile('small_zip.zip', mode='w', compression=ZIP_DEFLATED) as zf:
    for attach in attachments:
        add_attach = os.path.join(path, attach)
        zf.write(add_attach)

with ZipFile('small_zip.zip', mode='a') as zf:
    for file in zf.infolist():
        print(os.path.basename(file.filename))

os.remove(os.getcwd() + '/small_zip.zip')