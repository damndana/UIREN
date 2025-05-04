import zipfile
import os

zip_path ='/Users/dana/uiren_full/main/analytics/analytics/part1.zip'
extract_path = '/Users/dana/uiren_full/main/analytics/analytics/part1.unzip'

with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)
