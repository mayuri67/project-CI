from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello CI"}

@app.get("/health")
def health():
    return {"status": "UP"}