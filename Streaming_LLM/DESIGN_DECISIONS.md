# Design Decisions and Architecture Rationale

## Objective

The primary objective was to reduce perceived latency in an AI-powered content generation platform by streaming generated content to users as soon as it becomes available.

---

## Why Streaming?

Traditional request-response flow:

```text
User
  ↓
Backend
  ↓
LLM
  ↓
Wait for complete response
  ↓
Backend
  ↓
User
```

Problems:

* Long waiting times
* Poor user experience
* No visibility into generation progress

Streaming flow:

```text
User
  ↓
Backend
  ↓
LLM Stream
  ↓
Token
  ↓
Token
  ↓
Token
  ↓
User
```

Benefits:

* Immediate feedback
* Reduced perceived latency
* Better user engagement
* ChatGPT-like experience

---

## Why Server-Sent Events (SSE)?

Several approaches were evaluated.

### Polling

Rejected because:

* Inefficient
* Increased server load
* Delayed updates

### WebSockets

Advantages:

* Full duplex communication
* Real-time bidirectional messaging

Disadvantages:

* Higher implementation complexity
* Additional connection management
* Not required for one-way token streaming

### Server-Sent Events

Selected because:

* Native browser support
* Lightweight implementation
* Ideal for server-to-client streaming
* Simpler than WebSockets
* Well suited for LLM response streaming

---

## Why FastAPI?

FastAPI was selected because:

* High performance
* Native support for streaming responses
* Excellent developer experience
* Strong type validation using Pydantic
* Production-ready ecosystem

---

## Why Gemini?

Gemini provides:

* Streaming API support
* Low latency generation
* Modern SDK
* Strong content generation capabilities

The SDK exposes a stream interface which aligns naturally with Python generators.

---

## Why Python Generators?

Example:

```python
def stream():
    yield token
```

Benefits:

* Memory efficient
* Natural fit for streaming
* Incremental delivery
* Clean integration with FastAPI StreamingResponse

Generators allow tokens to be forwarded immediately instead of buffering the entire response.

---

## Why a Single Shared Client?

Instead of:

```python
client = genai.Client()
```

per request, the application initializes one client instance and reuses it.

Benefits:

* Reduced initialization overhead
* Better resource utilization
* Cleaner architecture

This follows a production-style dependency management approach.

---

## Why JSON SSE Events?

Instead of sending raw text:

```text
data: hello
```

the design supports structured payloads:

```json
{
  "type": "token",
  "content": "hello"
}
```

Advantages:

* Extensible protocol
* Supports metadata
* Easier frontend processing
* Supports future event types

Examples:

```json
{
  "type": "token"
}
```

```json
{
  "type": "done"
}
```

```json
{
  "type": "error"
}
```

---

## Scalability Considerations

Future production improvements may include:

### Redis

For:

* Caching
* Session storage
* Rate limiting

### PostgreSQL

For:

* Conversation history
* Analytics
* User management

### Authentication

Using:

* JWT
* OAuth

### Observability

Using:

* Structured logging
* Request IDs
* Metrics
* Tracing

---

## Final Architecture

```text
Browser
   ↓
HTML + JavaScript
   ↓
SSE Connection
   ↓
FastAPI
   ↓
Gemini Streaming API
   ↓
Token Stream
   ↓
FastAPI
   ↓
Browser Rendering
```

This architecture prioritizes simplicity, low latency, maintainability, and a responsive user experience while remaining extensible for future production requirements.
