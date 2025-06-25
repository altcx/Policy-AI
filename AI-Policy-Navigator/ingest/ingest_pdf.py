# AI Policy Navigator: PDF Ingestion Script

import sys
import os
import fitz  # PyMuPDF
from PIL import Image
import pytesseract

def extract_text_from_pdf(pdf_path, output_txt_path):
    doc = fitz.open(pdf_path)
    full_text = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        if text.strip():
            full_text.append(text)
        else:
            # If no text, try OCR
            pix = page.get_pixmap()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            ocr_text = pytesseract.image_to_string(img)
            full_text.append(ocr_text)
    with open(output_txt_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(full_text))
    print(f"Extracted text saved to {output_txt_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python ingest_pdf.py <input.pdf> <output.txt>")
        sys.exit(1)
    extract_text_from_pdf(sys.argv[1], sys.argv[2])
