from fastapi import FastAPI

app = FastAPI()

notes = []

@app.get("/")
def read_root():
    return {"message": "Welcome to simple notes app!"}

@app.post("/notes/")
def create_note(note: str):
    notes.append(note)
    return {"message": "Note created successfully!", "note": note}

@app.get("/notes/")
def get_notes():
    return {"notes": notes}

