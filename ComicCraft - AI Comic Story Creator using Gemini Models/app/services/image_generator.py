import os
import urllib.parse
import urllib.request
import uuid
import random

def generate_image(prompt: str) -> str:
    try:
        # Static & output directory create panrom
        os.makedirs("static/generated_images", exist_ok=True)
        filename = f"{uuid.uuid4().hex[:8]}.jpg"
        filepath = os.path.join("static/generated_images", filename)
        
        # Ovvoru panel-kum thani image vara random seed
        random_seed = random.randint(1, 999999)
        
        # Pollinations AI - Unique image prompt with random seed
        encoded_prompt = urllib.parse.quote(f"anime style comic book panel, Demon Slayer Tanjiro, {prompt}")
        image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=512&height=512&seed={random_seed}&nologo=true"
        
        # Image-a download panni save panrom
        req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
            
        return filepath
    except Exception as e:
        print(f"Image generation error: {e}")
        return "static/placeholder.png"