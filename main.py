from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from googletrans import Translator, LANGCODES

app = FastAPI()
translator = Translator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Check the language codes supported by googletrans
print(LANGCODES)

@app.post("/translate/")
async def translate_text(request: Request):
    data = await request.json()
    text = data.get("text", "")
    
    # Translate from English to Igbo
    translation = translator.translate(text, src="en", dest="ig")
    translated_text = translation.text
    return {"translated_text": translated_text}
