import os
from fpdf import FPDF

def save_pdf(layout):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "ComicCraft AI Story", ln=True, align="C")
    pdf.ln(10)
    
    # layout ஒரு list-ஆவோ அல்லது dict-ஆவோ இருந்தாலும் handle செய்யக்கூடிய condition
    if isinstance(layout, dict):
        panels = layout.get("panels", [])
    elif isinstance(layout, list):
        panels = layout
    else:
        panels = []
    
    for idx, panel in enumerate(panels):
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 8, f"Panel {idx + 1}", ln=True)
        
        # Add Image if exists
        img_path = panel.get("image_path") if isinstance(panel, dict) else None
        if img_path and os.path.exists(img_path):
            try:
                pdf.image(img_path, x=10, w=90)
                pdf.ln(5)
            except Exception as e:
                print(f"Error adding image to PDF: {e}")
                
        # Add Text/Dialogue
        pdf.set_font("Arial", size=10)
        text = panel.get("text", "") if isinstance(panel, dict) else str(panel)
        pdf.multi_cell(0, 6, f"Description: {text}")
        pdf.ln(10)
        
    os.makedirs("generated_pdfs", exist_ok=True)
    output_path = os.path.join("generated_pdfs", "comic_output.pdf")
    pdf.output(output_path)
    return output_path