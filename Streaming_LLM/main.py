from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from google import genai
from dotenv import load_dotenv  
import json
from fastapi.responses import FileResponse


load_dotenv()  # Load environment variables from .env file

app = FastAPI(
    title="Streaming LLM API",
    description="An API for streaming responses from a language model.",
    version="1.0.0"
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client()



def stream_response(prompt:str) :
    stream = client.interactions.create(
        model="gemini-3-flash-preview",
        input=prompt,
        stream=True,
    )

    for event in stream:
        if event.event_type == "step.delta":
            if event.delta.type == "text":
                payload = {
                    "type": "token",
                    "content": event.delta.text
                }

                yield f"data: {json.dumps(payload)}\n\n"
        
    
    yield f"data: {json.dumps({'type': 'done'})}\n\n"



@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/api/v1/chat/stream")
def chat_stream(prompt: str):

    return StreamingResponse(
        stream_response(prompt=prompt),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"}
    )
