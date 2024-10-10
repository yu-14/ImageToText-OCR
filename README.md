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

------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# With Deployment
# OCR Web Application

## Overview
This web application allows users to upload images and extract text in Hindi and English using Optical Character Recognition (OCR). Users can also search for specific keywords within the extracted text.

## Requirements
- Python 3.x
- Libraries: `gradio`, `pytesseract`, `Pillow`, `opencv-python-headless`, `numpy`

## Setup Instructions
    ```

1. **Create a Virtual Environment**:
    ```bash
    python -m venv ocr_env
    source ocr_env/bin/activate
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application Locally**:
    ```bash
    python app.py
    ```
    Open your browser and go to `http://127.0.0.1:7860`.

## Deployment Instructions
The application is deployed on Hugging Face Spaces. You can access it at:
[Live URL](<https://huggingface.co/spaces/YU14/ImagetotextAppl>)

## Example Usage
- Upload an image containing Hindi and English text.
- Enter a keyword in the textbox and click "Submit" to see highlighted occurrences in the extracted text.
