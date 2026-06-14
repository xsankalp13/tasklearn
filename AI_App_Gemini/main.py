from fastapi import FastAPI, Query
from google import genai
from google.genai import types
from dotenv import load_dotenv
from typing import Literal
from fastapi import HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware



load_dotenv()

app = FastAPI(
    title="AI Content Generator",
    description="Generate social media content using Gemini",
    version="1.0.0")
client = genai.Client()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

PROMPT_TEMPLATE = """
Role -
You are an expert social media content strategist and copywriter with experience creating engaging, platform-specific content for digital audiences.

Objective -
Generate a high-quality {CONTENT_TYPE} about the topic "{TOPIC}". The content should be informative, engaging, and optimized for the selected platform while encouraging audience interaction.

Audience -
General social media users interested in the topic. Adapt the language, complexity, and style based on the content type and platform conventions.

Tone -
Professional, creative, conversational, and engaging. Maintain a positive and audience-friendly tone while ensuring clarity and relevance.

Constraints -

1. Focus only on the provided topic: "{TOPIC}".
2. Tailor the content specifically for the selected content type: "{CONTENT_TYPE}".
3. Keep the content concise and suitable for short-form digital consumption.
4. Avoid misinformation, offensive language, and unsupported claims.
5. Use clear and compelling language.
6. Include a strong hook at the beginning when applicable.
7. Include relevant hashtags only if appropriate for the content type.
8. Ensure originality and avoid repetitive phrasing.
9. Maintain platform-specific best practices:

   * Twitter Thread: Short, connected tweets with a strong opening and logical flow.
   * Instagram Caption: Attention-grabbing opening, storytelling style, and engagement-focused ending.
   * Blog Idea: Catchy title and a brief content summary.
10. Do not explain your reasoning.
11. Do not include markdown code blocks.

Output Format -
Content Type: {CONTENT_TYPE}

Topic: {TOPIC}

Generated Content: <Generated Content Here>

Optional Hashtags: <List of relevant hashtags if applicable>


"""

ContentType = Literal["Instagram caption", "Twitter Thread Idea", "Short Blog Post Outline"]
GenerativeModels = Literal["gemini-3.5-flash", "gemini-3.1-flash-lite", "gemini-3.1-flash", "gemini-3.0-flash"]

class GenerateRequest(BaseModel):
    topic: str
    content_type: ContentType
    model: GenerativeModels = "gemini-3.5-flash"
    max_tokens: int = Field(500, ge=50, le=2048)
    temperature: float = Field(0.7, ge=0.0, le=2.0)

class ContentResponse(BaseModel):
    topic: str
    content_type: str
    generated_content: str


@app.post("/generate", response_model=ContentResponse)
async def generate_text(
    request: GenerateRequest
):
    topic = request.topic
    content_type = request.content_type
    model = request.model
    max_tokens = request.max_tokens
    temperature = request.temperature

    prompt = PROMPT_TEMPLATE.format(CONTENT_TYPE=content_type, TOPIC=topic)
    

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )


        generated_text = response.text or ""
        if not generated_text.strip():
            raise HTTPException(
                status_code=500,
                detail="Model returned an empty response."
            )

        return ContentResponse(
            topic=topic,
            content_type=content_type,
            generated_content=generated_text
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while generating content: {str(e)}"
        )