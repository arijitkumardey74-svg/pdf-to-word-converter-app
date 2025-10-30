# 🧾 PDF to Word Converter App

A simple web application that converts PDF files into Word documents using **FastAPI (Python)** for the backend and a minimal **HTML/JavaScript frontend**.

## 🚀 Features
- Upload PDF and convert to `.docx`
- Built with FastAPI
- Lightweight and easy to use

## 🛠️ Installation

### Backend setup
```bash
pip install fastapi uvicorn python-docx python-multipart
py -m uvicorn app:app --reload --port 8001
