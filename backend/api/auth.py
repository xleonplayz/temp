"""
Authentication API Routes
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

from services.auth_service import AuthService
from services.user_service import UserService
from db.database import get_db

router = APIRouter()


class LoginRequest(BaseModel):
    email: str
    password: str


class RegisterRequest(BaseModel):
    email: str
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int


@router.post("/login", response_model=TokenResponse)
async def login(credentials: LoginRequest, db=Depends(get_db)):
    """Login with email and password"""
    auth_service = AuthService(db)
    result = auth_service.authenticate(credentials.email, credentials.password)
    if not result:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return result


@router.post("/register", response_model=TokenResponse)
async def register(data: RegisterRequest, db=Depends(get_db)):
    """Register a new user"""
    user_service = UserService(db)
    auth_service = AuthService(db)

    # Check if email exists
    existing = user_service.get_user_by_email(data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create user
    user = user_service.create_user(
        email=data.email,
        username=data.username,
        password=data.password
    )

    # Generate token
    token = auth_service.generate_token(user.id)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": user.id
    }


@router.post("/logout")
async def logout():
    """Logout current user"""
    return {"message": "Logged out successfully"}


@router.get("/me")
async def get_current_user(db=Depends(get_db)):
    """Get current authenticated user"""
    # This would normally extract user from JWT token
    return {"id": 1, "email": "user@example.com", "username": "user"}
