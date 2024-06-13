from fastapi import FastAPI
from app.api.endpoints import configurations

# Initialize the FastAPI app
app = FastAPI()

# Include the main API router
app.include_router(configurations.router)