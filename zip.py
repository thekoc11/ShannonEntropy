# import shutil
#
# shutil.make_archive('zip', 'gztar', 'files')
#
import zipfile
import struct




my_zip  =  zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED)

my_zip.write('files/allText.txt')
my_zip.close()

with open('files.zip', 'rb') as f:
    f.seek(-8, 2)
    print(struct.unpack('I', f.read(4))[0])