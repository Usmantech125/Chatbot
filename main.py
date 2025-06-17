import os
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

app = FastAPI()


API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("GROQ_API_KEY environment variable is not set")

client = Groq(api_key=API_KEY)


templates = Jinja2Templates(directory="templates")


class QueryRequest(BaseModel):
    prompt: str
    model: str
    max_tokens: int = 100

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chatbot.html", {"request": request})

@app.post("/api/query")
async def query_api(data: QueryRequest):
    try:
        completion = client.chat.completions.create(
            model=data.model,
            messages=[
                {"role": "user", "content": data.prompt}
            ],
            max_completion_tokens=data.max_tokens,
            stream=False
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error code: 400 - {str(e)}")

