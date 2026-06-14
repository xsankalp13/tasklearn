# AI Content Generator

A proof-of-concept application demonstrating how Large Language Models (LLMs) can streamline the creation of short-form marketing content. The application accepts a topic and content type as input, then generates platform-specific content using Google's Gemini models.

---

## Overview

Marketing teams often spend significant time brainstorming and drafting content for multiple platforms. This project demonstrates how generative AI can accelerate that workflow by producing first-draft content tailored to specific social media channels.

The application supports generating:

* Instagram Captions
* Twitter Thread Ideas
* LinkedIn Posts
* Short Blog Post Outlines

The generated content is optimized through prompt engineering techniques that provide the model with clear instructions regarding audience, tone, constraints, and expected output format.

---

## Features

### Content Generation

Generate marketing content based on:

* Topic
* Content Type
* Model Selection
* Temperature
* Maximum Token Count

### Supported Content Types

| Content Type            | Description                              |
| ----------------------- | ---------------------------------------- |
| Instagram Caption       | Engagement-focused social media caption  |
| Twitter Thread Idea     | Structured thread with a compelling hook |
| LinkedIn Post           | Professional and value-driven content    |
| Short Blog Post Outline | Blog title and structured outline        |

### Model Selection

Users can choose between multiple Gemini models for experimentation and comparison.

### REST API

Backend exposes a simple API endpoint that can be integrated into internal tools and workflows.

### Simple Frontend

A lightweight single-page HTML interface allows users to interact with the API without requiring API tools such as Postman.

---

# System Architecture

```text
+------------------+
|    Frontend      |
|    index.html    |
+--------+---------+
         |
         | HTTP POST
         v
+------------------+
|     FastAPI      |
|     Backend      |
+--------+---------+
         |
         | Prompt Construction
         v
+------------------+
| Prompt Template  |
+--------+---------+
         |
         | Request
         v
+------------------+
| Gemini API       |
| LLM Generation   |
+--------+---------+
         |
         | Response
         v
+------------------+
| Generated Content|
+------------------+
```

---

# Design Philosophy

## 1. Separation of Concerns

The application separates:

* User Interface
* Business Logic
* Prompt Engineering
* AI Model Invocation

This makes the system easier to maintain and extend.

---

## 2. Prompt-Driven Behavior

Instead of hardcoding generation logic, behavior is controlled through a structured prompt template.

The prompt explicitly defines:

* Role
* Objective
* Audience
* Tone
* Constraints
* Output Format

This approach improves consistency and portability across models.

---

## 3. Type Safety

The backend uses Python Literal types and Pydantic models to:

* Restrict supported content types
* Validate incoming requests
* Improve API documentation
* Reduce runtime errors

---

## 4. Configurable Generation

Users can experiment with:

* Different Gemini models
* Temperature values
* Maximum token limits

This enables testing different creativity and response-length settings.

---

## 5. Extensibility

New content formats can be added by:

1. Extending the ContentType literal.
2. Updating the prompt instructions.
3. Adding a frontend dropdown option.

No architectural changes are required.

---

# Technology Stack

## Backend

* FastAPI
* Google Gemini SDK
* Pydantic
* Python 3.10+

## Frontend

* HTML5
* CSS3
* Vanilla JavaScript

## AI

* Gemini Generative Models

---

# Project Structure

```text
project-root/
│
├── main.py
├── index.html
├── requirements.txt
├── .env
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd <repository-name>
```

---

## 2. Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Configuration

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_api_key_here
```

Replace the value with a valid Gemini API key.

---

# Running the Backend

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Server will start on:

```text
http://localhost:8000
```

---

# API Documentation

FastAPI automatically generates interactive documentation.

Swagger UI:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# Running the Frontend

Open:

```text
index.html
```

in your browser.

Alternatively, serve it using a local server:

```bash
python -m http.server 5500
```

Then visit:

```text
http://localhost:5500
```

---

# API Usage

## Endpoint

```http
POST /generate
```

### Request Body

```json
{
  "topic": "Artificial Intelligence in Marketing",
  "content_type": "LinkedIn Post",
  "model": "gemini-3.5-flash",
  "max_tokens": 500,
  "temperature": 0.7
}
```

### Successful Response

```json
{
  "topic": "Artificial Intelligence in Marketing",
  "content_type": "LinkedIn Post",
  "generated_content": "AI is transforming marketing..."
}
```

---

# Prompt Engineering Strategy

The prompt follows a structured framework:

## Role

Defines the model's expertise.

Example:

```text
You are an expert social media content strategist.
```

---

## Objective

Specifies the task.

Example:

```text
Generate a LinkedIn post about AI in Marketing.
```

---

## Audience

Defines who will consume the content.

---

## Tone

Controls writing style.

Examples:

* Professional
* Conversational
* Engaging

---

## Constraints

Provides generation boundaries.

Examples:

* Stay on topic
* Avoid misinformation
* Follow platform-specific best practices

---

## Output Format

Ensures predictable and clean responses.

---

# Future Improvements

Potential enhancements include:

* User authentication
* Content history
* Content editing workflow
* Multiple prompt templates
* Streaming responses
* Content export options
* A/B content generation
* Analytics and feedback collection
* Multi-language support

---

# Limitations

* Content quality depends on model capabilities.
* Generated content may require human review.
* This project is intended as a proof-of-concept and not a production-ready marketing platform.
* Rate limits and quotas are determined by the Gemini API.

---

# Conclusion

This project demonstrates how modern LLMs can be integrated into internal marketing workflows to accelerate content ideation and drafting. By combining FastAPI, prompt engineering, and Gemini models, the application provides a simple yet extensible foundation for AI-assisted content creation.
