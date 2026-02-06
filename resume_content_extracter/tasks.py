from celery import Celery
import fitz # PyMuPDF
import pytesseract
from PIL import Image
import io

celery_app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

@celery_app.task(bind=True)
def process_resume(self, file_bytes, file_ext):
    text = ""
    try:
        if file_ext == ".pdf":
            doc = fitz.open(stream=file_bytes, filetype="pdf")
            for page in doc:
                page_text = page.get_text()
                if page_text.strip():
                    text += page_text
                else:
                    # OCR Fallback for scanned PDFs
                    pix = page.get_pixmap()
                    img = Image.open(io.BytesIO(pix.tobytes()))
                    text += pytesseract.image_to_string(img)
        else:
            # Direct OCR for JPG/PNG
            img = Image.open(io.BytesIO(file_bytes))
            text = pytesseract.image_to_string(img)
            
        return {"status": "success", "content": text.strip()}
    except Exception as e:
        return {"status": "error", "message": str(e)}