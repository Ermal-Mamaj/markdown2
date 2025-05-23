from fastapi import FastAPI, Request, UploadFile, File, Form
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uuid

from utils.converter import markdown_to_html, html_to_pdf
from db import get_db_connection, init_db  
init_db()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_markdown(file: UploadFile = File(...), theme: str = Form("default")):
    contents = await file.read()
    md_text = contents.decode("utf-8")

    html = markdown_to_html(md_text)
    filename = f"{uuid.uuid4().hex}.pdf"
    os.makedirs("output", exist_ok=True)
    pdf_path = os.path.join("output", filename)

    html_to_pdf(html, pdf_path, theme)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, description) VALUES (?, ?)",
        (filename, file.filename)
    )
    conn.commit()
    conn.close()

    return JSONResponse({
        "download_url": f"/download/{filename}",
        "html": html
    })

@app.get("/download/{filename}")
def download_pdf(filename: str):
    file_path = os.path.join("output", filename)
    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=filename
    )

@app.get("/history", response_class=HTMLResponse)
def show_history(request: Request):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items ORDER BY id DESC")
    items = cursor.fetchall()
    print("Fetched items:", items)
    conn.close()
    return templates.TemplateResponse("history.html", {"request": request, "items": items})
