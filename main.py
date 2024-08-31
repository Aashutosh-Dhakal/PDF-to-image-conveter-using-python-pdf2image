from pdf2image import convert_from_path, convert_from_bytes
import tempfile
import os

pdf_folder_path = './pdf'
file_names = os.listdir(pdf_folder_path)
file_names = [
    f for f in file_names
    if os.path.isfile(os.path.join(pdf_folder_path, f)) and not f.startswith('.')
]

print('Program Started')
try:
    print('Starting Convertion...')
    for each in file_names:
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(
                f'pdf/{each}', output_folder='./images')
    print('Successfully Converted.')
except:
    print('Sorry there was an error encounterd.')
