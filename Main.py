import cv2
import pytesseract
from PIL import Image

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    
    return thresh

def extract_text_from_image(image_path):
    try:
        processed_image = preprocess_image(image_path)
        pil_image = Image.fromarray(processed_image)
        text = pytesseract.image_to_string(pil_image, lang='eng+hin')
        
        return text
    except Exception as e:
        print(f"An error occurred: {e}")
image_path = r'C:\Users\pilli uttej\OneDrive\Documents\Uttej\intern2\id2.jpg'  # Adjust this line
text = extract_text_from_image(image_path)

if text:
    print("Extracted Text:")
    print(text)
else:
    print("No text was extracted.")