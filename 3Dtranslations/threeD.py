from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'image/your_image.png'  # Replace with the path to your image
image = Image.open(image_path)
image = image.convert('RGB')  # Use 'L' if you want to convert to grayscale

# Convert the image to a numpy array
image_np = np.array(image)

# Translation transformation
def translate_image(image_np, tx, ty):
    translated_image = Image.fromarray(image_np).transform(
        image_np.shape[1::-1],
        Image.AFFINE,
        (1, 0, tx, 0, 1, ty)
    )
    return np.array(translated_image)

# Rotation transformation
def rotate_image(image_np, angle):
    rotated_image = Image.fromarray(image_np).rotate(angle, expand=True)
    return np.array(rotated_image)

# Scaling transformation
def scale_image(image_np, sx, sy):
    scaled_image = Image.fromarray(image_np).resize(
        (int(image_np.shape[1] * sx), int(image_np.shape[0] * sy)),
        resample=Image.BICUBIC
    )
    return np.array(scaled_image)

# Translation parameters
tx, ty = 50, 50  # Translation amounts in X and Y directions

# Rotation parameter
angle = 45  # Rotation angle in degrees

# Scaling parameters
sx, sy = 1.5, 1.5  # Scaling factors in X and Y directions

# Apply transformations
translated_image_np = translate_image(image_np, tx, ty)
rotated_image_np = rotate_image(translated_image_np, angle)
scaled_image_np = scale_image(rotated_image_np, sx, sy)

# Visualize the results
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.title("Original Image")
plt.imshow(image_np)

plt.subplot(2, 2, 2)
plt.title("Translated Image")
plt.imshow(translated_image_np)

plt.subplot(2, 2, 3)
plt.title("Rotated Image")
plt.imshow(rotated_image_np)

plt.subplot(2, 2, 4)
plt.title("Scaled Image")
plt.imshow(scaled_image_np)

plt.show()
