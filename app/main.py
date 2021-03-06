from fastapi import FastAPI

from . import models
from .database import engine
from .routers import user, auth, organisation


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(organisation.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World!"}
