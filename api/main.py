from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routes import dialflo_bot


app = FastAPI(
    title="Dialflo - Backend Task",
    description="Task assigned by Dialflo for backend eng role. Simple backend system for a voice AI agent that can handle basic customer interactions via API.",
    version="1.0.0",
    swagger_ui_parameters={"defaultModelsExpandDepth": -1}
)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

Base.metadata.create_all(bind=engine)

# app.include_router(property.router)
app.include_router(dialflo_bot.router, prefix="/api")
