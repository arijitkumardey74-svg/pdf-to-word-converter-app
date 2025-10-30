from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from docx import Document
import fitz  # PyMuPDF

app = FastAPI()

# --- Allow frontend access ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Define /convert route ---
@app.post("/convert")
async def convert_pdf_to_word(file: UploadFile = File(...)):
    pdf_bytes = await file.read()
    pdf_name = file.filename.replace(".pdf", ".docx")

    # Convert PDF → Word
    doc = Document()
    pdf = fitz.open(stream=pdf_bytes, filetype="pdf")

    for page in pdf:
        text = page.get_text()
        doc.add_paragraph(text)

    pdf.close()
    doc.save(pdf_name)

    return FileResponse(
        pdf_name,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename=pdf_name
    )
