from fastapi import FastAPI

app = FastAPI(
    title="Platform Engineering Demo",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Platform Engineering Demo API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.get("/api/info")
def info():
    return {
        "application": "developer-platform-demo",
        "version": "1.0.0",
        "environment": "development"
    }