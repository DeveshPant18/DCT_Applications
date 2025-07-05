# DCT_Applications

# Image and Signal Compression Using Discrete Cosine Transform (DCT)

## Overview
This project demonstrates compression techniques using the Discrete Cosine Transform (DCT) applied to both 1D signals and 2D color images. The project highlights the process of transforming data into the frequency domain, compressing it by retaining significant coefficients, and reconstructing the original data using inverse transforms.

The work was conducted under the guidance of **Dr. A.K.B. Chand** from the Department of Mathematics, IIT Madras.

## Features
- **Signal Compression:**
  - Generation of synthetic sine wave signals.
  - Compression by keeping only the top 10% of DCT coefficients.
  - Reconstruction of signals via Inverse DCT (IDCT).
  - Visualization of original, compressed, and reconstructed signals.

- **Image Compression:**
  - Application of 2D DCT on RGB image channels.
  - Compression by retaining top-left 100×100 frequency coefficients per channel.
  - Reconstruction of compressed images.
  - Visualization of original and compressed images along with individual color channels.

## Tools and Technologies
- Python
- NumPy
- SciPy
- OpenCV
- Matplotlib

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/DeveshPant18/DCT_Applications.git
