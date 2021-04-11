import zipfile

# Context manager
with zipfile.ZipFile('after_compression.zip', 'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as demo_zip:
    demo_zip.write('large_files/100MB.txt')
    demo_zip.write(
        'large_files/Very_Large_Telescope_Ready_for_Action_(ESO).jpeg')
    
