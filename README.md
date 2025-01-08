# Image Processing - Histogram Operations

This repository contains the implementation of histogram equalization and histogram stretching operations as part of an assignment for the **Image Processing** course.

---

## 📚 Project Description

### Key Features:
- **Histogram Equalization**: Enhances the contrast of an image by redistributing the intensity values.
- **Histogram Stretching**: Adjusts the intensity range of the image to improve visibility and contrast.
- **Gray Image Processing**: Focuses on single-channel grayscale images.

### Tools & Libraries Used:
- **Programming Language**: Python
- **Libraries**: OpenCV, NumPy, Matplotlib

---

## 🚀 How to Use

### 1. Clone the repository:
    ```bash
    git clone https://github.com/zgokceaynaci/image-processing-histogram.git


### 📄 Functionality
Histogram Equalization:
**Reads a grayscale image.
**Computes the histogram of the image.
**Redistributes pixel intensity values to enhance contrast.
**Saves the processed image and plots the new histogram.
Histogram Stretching:
**Reads a grayscale image.
**Identifies the minimum and maximum intensity values.
**Linearly stretches the pixel intensity values to cover the full range (0-255).
**Saves the processed image and plots the stretched histogram.
