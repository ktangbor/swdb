from fastapi import FastAPI

app = FastAPI(title="Star Wars API")


@app.get("/")
def root():
    return {"message": "May the force be with you!"}
