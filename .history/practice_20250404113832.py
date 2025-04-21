from PIL import Image
import numpy as np
import pytesseract

# Load the images
mask_img = Image.open("/icons/mask.jpg").convert("L")  # Convert to grayscale
matrix_img = Image.open("word_matrix.jpg")

# Convert mask to numpy array and find white regions
mask_array = np.array(mask_img)
mask_threshold = mask_array > 240  # Boolean mask for white pixels

# Get bounding boxes of connected white regions
from scipy.ndimage import label, find_objects

labeled_array, num_features = label(mask_threshold)
regions = find_objects(labeled_array)

# Sort regions from top to bottom, then left to right
regions = sorted(regions, key=lambda r: r[0].start * 10000 + r[1].start)

# Extract words from matrix using mask regions
words = []

for region in regions:
    y_slice, x_slice = region
    roi = matrix_img.crop((x_slice.start, y_slice.start, x_slice.stop, y_slice.stop))
    text = pytesseract.image_to_string(roi, config="--psm 8").strip()
    if text:
        words.append(text)

# Output hidden message
print("Hidden Message:", " ".join(words))
