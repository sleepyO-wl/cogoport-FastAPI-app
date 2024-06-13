from fastapi import APIRouter
from app.api.endpoints import configurations

# Initialize the main API router
api_router = APIRouter()

# Include the configuration router
api_router.include_router(configurations.router, prefix="/configurations", tags=["configurations"])
