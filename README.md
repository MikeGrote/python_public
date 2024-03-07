# python_public

# Using the PdfOrganizer script
Introduction
The PdfOrganizer script is an effective tool for organizing PDF files stored in a specific folder based on their creation date and moving them to new, appropriately dated folders. This Python script uses the PyPDF4 library to analyze PDF metadata and os as well as shutil for file operations. The following instructions will guide you through the setup and use of this script.

# Preparation
Python installation: Make sure that Python is installed on your system. The script was written with Python 3.
Install dependencies: The script requires the PyPDF4 library. Install it via Pip with the command:

pip install PyPDF4

Download script: Download the PdfOrganizer script from your GitHub repository or copy the provided code into a new Python file.

# Configuration
Define source folder (src_folder): Define the path to the folder containing the PDF files to be organized.
Set destination folder (dst_root_folder): Define the path to the destination folder to which the organized PDF files are to be moved.
Usage
Customize script: Edit the src_folder and dst_root_folder variables in the script to set them to your specific folder paths.
Execute script: Run the script in your Python environment or from the command line using the python PdfOrganizer.py command.
Check: After executing the script, check the target folder. You should see that the PDF files have been organized into appropriately named subfolders based on their creation date.
Troubleshooting
If the script does not move any files, check the PDF metadata for valid creation dates and make sure that the file paths are specified correctly.
In case of errors related to PyPDF4, make sure that the library is installed correctly.
Safety instructions
Always run scripts and programs in a safe environment and make sure you understand the code to avoid unwanted side effects.
Support
For further support and updates, visit the script's GitHub repository or contact the author via the channels provided there.

# License
Make sure to check the license terms of the script to ensure its use according to the author's specifications.

With this user documentation, you should be able to use the PdfOrganizer script effectively to keep your PDF files organized and accessible.
