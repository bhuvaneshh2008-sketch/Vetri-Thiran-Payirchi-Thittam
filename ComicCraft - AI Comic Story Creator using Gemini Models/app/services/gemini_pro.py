import google.generativeai as genai
from app.config import GEMINI_API_KEY

if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

def generate_story(outline):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"Write an epic comic book narration for each panel in this outline: {outline}. Keep it short and dramatic."
        response = model.generate_content(prompt)
        
        if response and response.text:
            return response.text
    except Exception as e:
        print(f"Gemini Pro Story Error: {e}")
    
    # API வொர்க் ஆகலைனாலும் 5 Panels-க்கும் அழகா Story Text செட் ஆகிடும்:
    return "Kamado Tanjiro braves the freezing snow, focusing his breathing technique to unleash his true strength against the forces of darkness."