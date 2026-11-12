# Session 1: Trace One HTTP Request

## How a request travels through a backend

```text
Browser / Client
       |
       | HTTP Request
       v
Backend Logic
       |
       | Reads or updates data
       v
Data Store
       |
       | Returns data
       v
Backend Logic
       |
       | HTTP Response (JSON)
       v
Browser / Client
```

## Key Terms

- **Client:** The application or browser that sends a request.
- **Server:** The system that receives and processes the request.
- **Request:** A message sent by the client to the server.
- **Response:** The result sent back by the server.
- **JSON:** A structured format used to exchange data.x`