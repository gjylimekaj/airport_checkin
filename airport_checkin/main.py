import sys
import uvicorn
import asyncio
import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


# Initializing main app
app = FastAPI(
    title="Vloris backend API",
    description="""
    The API backend is used for Vlori platform.
    More descriptions coming soon.
    """,
    version="1.0.0",
    docs_url="/",
    redoc_url="/docs",  # Is this needed or can Redoc be removed?
)

# Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Include apps



if __name__ == "__main__":
    try:
        if sys.argv[1] == "serve":
            uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

    except IndexError:
        print("No command line args found.")
        print("Command to pass: 1. serve: to start the server")
print("hello")
print("i just started to create a small project for airport checkin system")
print("hope youll like it :)")