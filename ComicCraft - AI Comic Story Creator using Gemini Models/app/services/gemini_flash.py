import json
import google.generativeai as genai
from app.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_outline(prompt: str, character_name: str = "Hero", setting: str = "Forest", tone: str = "Dramatic", art_style: str = "Comic Book") -> list:
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        system_prompt = f"""
        You are a professional comic book creator.
        Generate a 5-panel comic story outline based on:
        - Story Prompt: {prompt}
        - Main Character: {character_name}
        - Setting: {setting}
        - Tone: {tone}
        - Art Style: {art_style}

        Return strictly a JSON array containing exactly 5 objects.
        Each object must have:
        - "panel": Integer (1 to 5)
        - "title": Title of the panel
        - "scene_description": Detailed description of scene setting
        - "image_prompt": Prompt for image in {art_style} style featuring {character_name} in {setting}
        """
        response = model.generate_content(system_prompt)
        text_response = response.text.strip()
        
        if text_response.startswith("```json"):
            text_response = text_response[7:]
        if text_response.startswith("```"):
            text_response = text_response[3:]
        if text_response.endswith("```"):
            text_response = text_response[:-3]
            
        return json.loads(text_response.strip())
    except Exception as e:
        print(f"Error in generate_outline: {e}")
        return [
            {
                "panel": i,
                "title": f"Panel {i}: The Journey Begins",
                "scene_description": f"{character_name} navigates through {setting}.",
                "image_prompt": f"A comic panel in {art_style} style showing {character_name} in {setting}, {tone} mood."
            }
            for i in range(1, 6)
        ]