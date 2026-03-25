from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastApI with CSV! anurag singh is here"}