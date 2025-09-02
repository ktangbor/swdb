from fastapi import FastAPI
from swdb_app.api.v1.routes import health, characters, films

app = FastAPI(title="Star Wars Database")

app.include_router(health.router)
app.include_router(characters.router)
app.include_router(films.router)


@app.get("/")
def root():
    return {"message": "May the force be with you!"}
