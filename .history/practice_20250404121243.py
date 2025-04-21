'''from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage import label, find_objects
mask_img = Image.open("/Users/dana/uiren_full/main/static/icons/mask.jpg").convert("L")
matrix_img = Image.open("/Users/dana/uiren_full/main/static/icons/word-matrix.jpg")
mask_resized = mask_img.resize(matrix_img.size)
mask_array = np.array(mask_resized)
mask_threshold = mask_array > 240 

labeled_array, num_features = label(mask_threshold)
regions = find_objects(labeled_array)

regions = sorted(regions, key=lambda r: r[0].start * 10000 + r[1].start)

draw = ImageDraw.Draw(matrix_img)
for region in regions:
    y_slice, x_slice = region
    draw.rectangle([x_slice.start, y_slice.start, x_slice.stop, y_slice.stop], outline="red", width=2)

matrix_img.show()'''

import re
from pypdf import PdfReader
pattern=[]
reader=PdfReader("/Users/dana/uiren_full/main/static/icons/document 2.pdf")
pattern1=r"\+1-\d{3}-\d{3}-\d{4}"
pattern2=r"\@\gmail\.com"
combined_pattern=f
for page in reader.pages:
    text = page.extract_text()
    if text:
        count += text.lower().count("data")
print("The word 'data' appears", count, "times in the document.")