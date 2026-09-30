from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str
    character_name: str = "Hero"
    setting: str = "Forest"
    tone: str = "Dramatic"
    art_style: str = "Comic Book"

class ImageTestRequest(BaseModel):
    prompt: str