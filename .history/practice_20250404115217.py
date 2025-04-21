from PIL import Image, ImageDraw
import numpy as np
from scipy.ndimage import label, find_objects
mask_img = Image.open("/Users/dana/uiren_full/main/static/icons/mask.jpg").convert("L")
matrix_img = Image.open("/Users/dana/uiren_full/main/static/icons/word-matrix.jpg")
mask_resized = mask_img.resize(matrix_img.size)

# Convert resized mask to binary array
mask_array = np.array(mask_resized)
mask_threshold = mask_array > 240  # True for white regions

# Label white rectangles
labeled_array, num_features = label(mask_threshold)
regions = find_objects(labeled_array)

# Sort by top-to-bottom, left-to-right
regions = sorted(regions, key=lambda r: r[0].start * 10000 + r[1].start)

# Draw rectangles on matrix image for visualization
draw = ImageDraw.Draw(matrix_img)
for region in regions:
    y_slice, x_slice = region
    draw.rectangle([x_slice.start, y_slice.start, x_slice.stop, y_slice.stop], outline="red", width=2)

# Show result
matrix_img.show()
