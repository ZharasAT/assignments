from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, nfactorial!"}

@app.post("/meaning-of-life")
def meaning_of_life():
        return {"meaning": "42"}