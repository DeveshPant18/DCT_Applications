import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
import cv2

# Load the color image in RGB format
image = cv2.imread('C:/Users/user/Desktop/Project/armas.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Separate the color channels
R, G, B = cv2.split(image_rgb)

# Apply 2D DCT to each channel
dct_R = dct(dct(R.T, norm='ortho').T, norm='ortho')
dct_G = dct(dct(G.T, norm='ortho').T, norm='ortho')
dct_B = dct(dct(B.T, norm='ortho').T, norm='ortho')

# Compress by keeping only the top-left 100x100 DCT coefficients
compressed_dct_R = np.zeros_like(dct_R)
compressed_dct_R[:100, :100] = dct_R[:100, :100]
compressed_dct_G = np.zeros_like(dct_G)
compressed_dct_G[:100, :100] = dct_G[:100, :100]
compressed_dct_B = np.zeros_like(dct_B)
compressed_dct_B[:100, :100] = dct_B[:100, :100]

# Reconstruct each channel using Inverse DCT
reconstructed_R = idct(idct(compressed_dct_R.T, norm='ortho').T, norm='ortho')
reconstructed_G = idct(idct(compressed_dct_G.T, norm='ortho').T, norm='ortho')
reconstructed_B = idct(idct(compressed_dct_B.T, norm='ortho').T, norm='ortho')

# Merge the channels back into an RGB image
reconstructed_image = cv2.merge([reconstructed_R, reconstructed_G, reconstructed_B])

# Display the original, compressed, and individual channel images
plt.figure(figsize=(16, 8))

# Original Image
plt.subplot(2, 3, 1)
plt.imshow(image_rgb)
plt.title('Original Color Image')
plt.axis('off')  # Hide axes

# Compressed Image
plt.subplot(2, 3, 2)
plt.imshow(np.clip(reconstructed_image, 0, 255).astype('uint8'))
plt.title('Compressed Color Image (100x100 DCT Coefficients)')
plt.axis('off')  # Hide axes

# Reconstructed Red Channel
plt.subplot(2, 3, 3)
plt.imshow(np.clip(reconstructed_R, 0, 255).astype('uint8'), cmap='Reds')
plt.title('Reconstructed Red Channel')
plt.axis('off')  # Hide axes

# Reconstructed Green Channel
plt.subplot(2, 3, 4)
plt.imshow(np.clip(reconstructed_G, 0, 255).astype('uint8'), cmap='Greens')
plt.title('Reconstructed Green Channel')
plt.axis('off')  # Hide axes

# Reconstructed Blue Channel
plt.subplot(2, 3, 5)
plt.imshow(np.clip(reconstructed_B, 0, 255).astype('uint8'), cmap='Blues')
plt.title('Reconstructed Blue Channel')
plt.axis('off')  # Hide axes

plt.tight_layout()
plt.show()

# Print the matrix representations
print("Original Image Matrix (RGB):")
print(image_rgb)

print("\nReconstructed Image Matrix:")
print(np.clip(reconstructed_image, 0, 255).astype('uint8'))

print("\nReconstructed Red Channel Matrix:")
print(np.clip(reconstructed_R, 0, 255).astype('uint8'))

print("\nReconstructed Green Channel Matrix:")
print(np.clip(reconstructed_G, 0, 255).astype('uint8'))

print("\nReconstructed Blue Channel Matrix:")
print(np.clip(reconstructed_B, 0, 255).astype('uint8'))