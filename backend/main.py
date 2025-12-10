"""
FastAPI Backend Server
User Management API
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.users import router as users_router
from api.posts import router as posts_router
from api.auth import router as auth_router

app = FastAPI(
    title="User Management API",
    description="API for managing users and posts",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(posts_router, prefix="/api/posts", tags=["posts"])


@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
