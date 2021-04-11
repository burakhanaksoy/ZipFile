import zipfile
import os
from functions.functions import *
import time

file_path = 'large_files'
print(f'Before compression -> {folder_size(file_path)}')
t1 = time.time()
# Creating a zip file
# Context manager
with zipfile.ZipFile('after_compression.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as demo_zip:
    demo_zip.write('large_files/100MB.txt')
    demo_zip.write(
        'large_files/Very_Large_Telescope_Ready_for_Action_(ESO).jpeg')
t2 = time.time()
file_path = 'after_compression.zip'
print(f'After compression -> {file_size(file_path)}')
print(f'Elapsed time -> {t2-t1} s')

# Extracting a zip file
# with zipfile.ZipFile('after_compression.zip', 'r') as demo_zip:
#     # print(demo_zip.namelist())
#     # demo_zip.extractall('extracted')
#     # extract specific file
#     demo_zip.extract('large_files/Very_Large_Telescope_Ready_for_Action_(ESO).jpeg')
