"""
Posts API Routes
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

from services.post_service import PostService
from db.database import get_db

router = APIRouter()


class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int


class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: str


@router.get("/", response_model=List[PostResponse])
async def get_posts(skip: int = 0, limit: int = 50, db=Depends(get_db)):
    """Get all posts with pagination"""
    post_service = PostService(db)
    posts = post_service.get_all_posts(skip=skip, limit=limit)
    return posts


@router.get("/{post_id}", response_model=PostResponse)
async def get_post(post_id: int, db=Depends(get_db)):
    """Get a specific post by ID"""
    post_service = PostService(db)
    post = post_service.get_post_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.get("/user/{user_id}", response_model=List[PostResponse])
async def get_user_posts(user_id: int, db=Depends(get_db)):
    """Get all posts by a specific user"""
    post_service = PostService(db)
    posts = post_service.get_posts_by_user(user_id)
    return posts


@router.post("/", response_model=PostResponse)
async def create_post(post_data: PostCreate, db=Depends(get_db)):
    """Create a new post"""
    post_service = PostService(db)
    post = post_service.create_post(
        title=post_data.title,
        content=post_data.content,
        author_id=post_data.author_id
    )
    return post


@router.put("/{post_id}", response_model=PostResponse)
async def update_post(post_id: int, post_data: PostUpdate, db=Depends(get_db)):
    """Update an existing post"""
    post_service = PostService(db)
    post = post_service.update_post(post_id, post_data.dict(exclude_unset=True))
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.delete("/{post_id}")
async def delete_post(post_id: int, db=Depends(get_db)):
    """Delete a post"""
    post_service = PostService(db)
    success = post_service.delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
