import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import dct, idct
# Generate a sample signal (sine wave)
fs = 100 # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False) # Time vector
frequency = 5 # Frequency of the sine wave
signal = np.sin(2 * np.pi * frequency * t) # Original signal
# Function to compress the signal
def compress_signal(signal, compression_ratio):
 # Perform DCT
 transformed_signal = dct(signal, norm='ortho')

 # Determine the number of coefficients to keep
 num_coefficients = int(len(transformed_signal) * compression_ratio)

 # Zero out the rest of the coefficients
 compressed_signal = np.zeros_like(transformed_signal)
 compressed_signal[:num_coefficients] = transformed_signal[:num_coefficients]

 return compressed_signal
# Function to reconstruct the signal from compressed data
def reconstruct_signal(compressed_signal):
 # Perform inverse DCT
 reconstructed_signal = idct(compressed_signal, norm='ortho')
 return reconstructed_signal
# Compress the signal
compression_ratio = 0.1 # Keep 10% of the coefficients
compressed_signal = compress_signal(signal, compression_ratio)
# Reconstruct the signal
reconstructed_signal = reconstruct_signal(compressed_signal)
# Plot the original and reconstructed signals
plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.grid()
plt.subplot(3, 1, 2)
plt.plot(t, compressed_signal)
plt.title('Compressed Signal (DCT Coefficients)')
plt.grid()
plt.subplot(3, 1, 3)
plt.plot(t, reconstructed_signal)
plt.title('Reconstructed Signal')
plt.grid()
plt.tight_layout()
plt.show()
