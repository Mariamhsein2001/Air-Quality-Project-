from fastapi import FastAPI
from air_pollution.endpoints.health import router as health_router
from air_pollution.endpoints.train_pipeline import router as pipeline_router
from air_pollution.endpoints.inference_pipeline import router as inference_router

# Initialize the FastAPI app
app = FastAPI(title="ML Data Pipeline API", version="1.0")

# Include API routes
app.include_router(health_router, prefix="/api", tags=["Health"])
app.include_router(pipeline_router, prefix="/api", tags=["Train"])
# app.include_router(inference_router, prefix="/api", tags=["Inference"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
