import zipfile
import os

zip_path = 'path/to/your/apple_music_data.zip'
extract_path = 'apple_music_data'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
