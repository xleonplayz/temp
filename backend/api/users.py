"""
User API Routes
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

from services.user_service import UserService
from db.database import get_db

router = APIRouter()


class UserCreate(BaseModel):
    email: str
    username: str
    password: str


class UserUpdate(BaseModel):
    email: Optional[str] = None
    username: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool


@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    """Get all users with pagination"""
    user_service = UserService(db)
    users = user_service.get_all_users(skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db=Depends(get_db)):
    """Get a specific user by ID"""
    user_service = UserService(db)
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserResponse)
async def create_user(user_data: UserCreate, db=Depends(get_db)):
    """Create a new user"""
    user_service = UserService(db)

    # Check if email already exists
    existing = user_service.get_user_by_email(user_data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = user_service.create_user(
        email=user_data.email,
        username=user_data.username,
        password=user_data.password
    )
    return user


@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user_data: UserUpdate, db=Depends(get_db)):
    """Update an existing user"""
    user_service = UserService(db)
    user = user_service.update_user(user_id, user_data.dict(exclude_unset=True))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}")
async def delete_user(user_id: int, db=Depends(get_db)):
    """Delete a user"""
    user_service = UserService(db)
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
