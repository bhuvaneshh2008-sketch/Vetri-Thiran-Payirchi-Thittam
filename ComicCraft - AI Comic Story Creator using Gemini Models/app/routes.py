import os
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, FileResponse

from app.services.gemini_flash import generate_outline
from app.services.gemini_pro import generate_story
from app.services.image_generator import generate_image
from app.services.layout_builder import build_comic_layout
from app.services.exporters import save_pdf

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse(
        request=request, 
        name="index.html"
    )

@router.post("/generate", response_class=HTMLResponse)
async def generate_comic(
    request: Request,
    prompt: str = Form(...),
    character_name: str = Form("Hero"),
    setting: str = Form("Forest"),
    tone: str = Form("Dramatic"),
    art_style: str = Form("Comic Book")
):
    # 1. Outline generate pannudhu (Gemini Flash)
    outline = generate_outline(prompt, character_name, setting, tone, art_style)
    
    # 2. Narration/Story generate pannudhu (Gemini Pro)
    story_text = generate_story(outline)
    
    # 3. Images generate pannudhu (Stable Diffusion)
    image_paths = []
    for item in outline:
        img_prompt = item.get("image_prompt", prompt)
        img_path = generate_image(img_prompt)
        image_paths.append(img_path)
        
    # 4. Comic Layout set pannudhu
    layout = build_comic_layout(image_paths, story_text, outline)
    
    # 5. PDF Save pannudhu
    pdf_path = save_pdf(layout)
    
    return templates.TemplateResponse(
        request=request,
        name="comic_preview.html", 
        context={"layout": layout, "pdf_path": pdf_path}
    )

@router.get("/export-success", response_class=HTMLResponse)
async def export_success(request: Request, pdf_path: str = ""):
    return templates.TemplateResponse(
        request=request,
        name="export_success.html", 
        context={"pdf_path": pdf_path}
    )

@router.get("/download-pdf")
async def download_pdf(pdf_path: str):
    if os.path.exists(pdf_path):
        return FileResponse(pdf_path, media_type='application/pdf', filename=os.path.basename(pdf_path))
    return {"error": "File not found"}