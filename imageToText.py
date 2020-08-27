# using tesseract lib install tesseract

import pytesseract

# install on C:\Program Files\Tesseract-OCR

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#print the output

print(pytesseract.image_to_string(r'test.png'))