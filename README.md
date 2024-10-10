# Text Extraction from Image

## Description
This project utilizes OpenCV and Tesseract OCR to extract text from images. It preprocesses the image to enhance text visibility and then uses Optical Character Recognition (OCR) to convert the image content into machine-readable text.

## Features
- Image preprocessing using OpenCV.
- Text extraction from images in English and Hindi.
- Error handling for robust performance.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- Tesseract OCR (`pytesseract`)
- Pillow (`PIL`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yu-14/text-extraction.git
   cd text-extraction
2. Install the required packages:
   pip install opencv-python pytesseract Pillow
3. Install Tesseract OCR:
   Windows: Download the installer from Tesseract at UB Mannheim and follow the installation instructions.
   Linux: Install via package manager:

          sudo apt-get install tesseract-ocr
   Mac: Use Homebrew:
        brew install tesseract

## Usage
1. Update the image_path variable in the script to point to your image file:
   ```python
   image_path = r'C:\path\to\your\image.jpg'  # Adjust this line
2. Run the script:
   ```bash
   python text_extraction.py
3. The extracted text will be printed in the console.