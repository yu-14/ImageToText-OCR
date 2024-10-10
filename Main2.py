import gradio as gr
import pytesseract
from PIL import Image
import cv2
import numpy as np

def preprocess_image(image):
    img_array = np.array(image)
    gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    processed_image = Image.fromarray(thresh)
    return processed_image

def extract_text_from_image(image):
    processed_image = preprocess_image(image)
    text = pytesseract.image_to_string(processed_image, lang='eng+hin')
    return text

def search_keyword(text, keyword):
    if keyword:
        highlighted_text = text.replace(keyword, f"<mark>{keyword}</mark>")
        return highlighted_text
    return text

def process_and_search(image, keyword):
    text = extract_text_from_image(image)
    highlighted_text = search_keyword(text, keyword)
    return highlighted_text
iface = gr.Interface(
    fn=process_and_search,
    inputs=[
        gr.Image(type="pil"),
        gr.Textbox(placeholder="Enter keyword to search...", label="Keyword")
    ],
    outputs="html",
    title="OCR Web App with Preprocessing and Keyword Search",
    description="Upload an image to extract text in Hindi and English after preprocessing. Enter a keyword to highlight in the extracted text."
)
iface.launch(share=True)