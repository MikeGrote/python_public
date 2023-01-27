import os
import shutil
from datetime import datetime
from PyPDF4 import PdfFileReader

class PdfOrganizer:
    def __init__(self, src_folder, dst_root_folder):
        self.src_folder = src_folder
        self.dst_root_folder = dst_root_folder

    def move_pdfs_by_creation_date(self):
        for filename in os.listdir(self.src_folder):
            filepath = os.path.join(self.src_folder, filename)
            if os.path.isdir(filepath):
                organizer_sub = PdfOrganizer(filepath, self.dst_root_folder)
                organizer_sub.move_pdfs_by_creation_date()
            elif filename.endswith('.pdf'):
                pdf_reader = PdfFileReader(open(filepath, 'rb'))
                pdf_info = pdf_reader.getDocumentInfo()
                try:
                    # Try parsing the creation date in format '%Y%m%d%H%M%S'
                    creation_date = datetime.strptime(pdf_info['/CreationDate'][2:10:], '%Y%m%d' )
                except ValueError:
                    # If it fails, try parsing in format 'D:%Y%m%d%H%M%S'
                    exit()
                dst_folder = os.path.join(self.dst_root_folder, creation_date.strftime('%Y-%m'))
                os.makedirs(dst_folder, exist_ok=True)
                new_filename = f"{creation_date.strftime('%Y%m%d')}_{filename}"
                shutil.copy(filepath, os.path.join(dst_folder, new_filename))

# Path to the original folder with the PDF files
src_folder = r"C:\temp"
# Path to the destination folder
dst_root_folder = r"C:\temp"
organizer = PdfOrganizer(src_folder, dst_root_folder)
organizer.move_pdfs_by_creation_date()