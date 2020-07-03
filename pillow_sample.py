# Import Pillow:
from PIL import Image

# Load the original image:
img = Image.open("/Users/harley/wKgBZ1kN2j6ATFuOAAWnqfcTiWI950.png")

img_processed = img.rotate(45)

img_processed.save("/Users/harley/Documents/pillow.png")