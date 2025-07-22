from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load image and convert to grayscale
img = Image.open("sample.jpg").convert("L")  # "L" means grayscale
img_array = np.array(img)

# Step 2: Display original image
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(img_array, cmap="gray")
plt.axis("off")

# Step 3: Brightness increase (matrix operation)
brightness_value = 50  # You can change this value (10–100)
bright_img_array = np.clip(img_array + brightness_value, 0, 255)  # Keep values in range

# Step 4: Display brightened image
plt.subplot(1, 2, 2)
plt.title("Brightened Image")
plt.imshow(bright_img_array, cmap="gray")
plt.axis("off")

# Step 5: Show both images
plt.tight_layout()
plt.show()
