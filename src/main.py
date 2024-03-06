from fastapi import FastAPI
from src.routes import cluster_colors

app = FastAPI(
    title="Cluster colors",
    version="0.0.1",
    description="Cluster colors in images"
)

app.include_router(cluster_colors.router, prefix="/funtions", tags=["Cluster colors"])

@app.get("/")
async def root():
    """Root endpoint for the API.

    Returns:
        dict: A dictionary with a message and a success flag.
    """
    return {"message": "Hello World!", "success": True}