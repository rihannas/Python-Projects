#!/usr/bin/python3

"""
This module helps to organise file (on desktop) to specific folders based on their extensions
eg: Pdf file --> Document
"""

import os
import shutil
from pathlib import Path

path = '/Users/rihannaali/Desktop'

os.chdir(path)


# List of image extensions
imagesExt = ['.raw', '.png',  '.gif', '.jpg,' '.jpeg',
             '.tif' '.tiff', '.XCF', '.PSD']

# list of document extensions
documentsExt = ['.doc', '.docx', '.html', '.pdf',
                '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.txt']

# list of audio extensions
audiosExt = ['.mp3', '.m4a', '.wav']

# list of audio extensions
videosExt = ['.mp4', '.mov', '.wmv', '.webm']


contents = os.scandir(path)


for content in contents:
    if content.is_file() == True:
        name = content.name
        name, ext = os.path.splitext(name)
        if ext in imagesExt:
            shutil.move(content, "images")
            print(f"Added {name} to images")
        elif ext in videosExt:
            shutil.move(content, "videos")
            print(f"Added {name} to videos")
        elif ext in documentsExt:
            shutil.move(content, "documents")
            print(f"Added {name} to documents")
        elif ext in audiosExt:
            shutil.move(content, "audios")
            print(f"Added {name} to audios")
        else:
            print(f"No specified folder to add {name}")
