"""
FastAPI Advanced Test - Various Route Patterns
"""

from fastapi import FastAPI, APIRouter, Depends, HTTPException, Query, Path
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Test API", version="1.0.0")
router = APIRouter(prefix="/api/v2", tags=["v2"])


# Pydantic models
class UserCreate(BaseModel):
    name: str
    email: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str


# Basic routes on app
@app.get("/")
async def root():
    return {"message": "Welcome"}


@app.get("/health")
async def health():
    return check_database_connection()


# Router-based routes
@router.get("/users", response_model=List[UserResponse])
async def list_users(skip: int = Query(0), limit: int = Query(10)):
    users = fetch_users_paginated(skip, limit)
    return users


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int = Path(..., gt=0)):
    user = find_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    validate_email(user.email)
    new_user = save_user_to_db(user)
    send_notification(new_user.id)
    return new_user


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate):
    existing = find_user_by_id(user_id)
    if not existing:
        raise HTTPException(status_code=404, detail="User not found")
    updated = update_user_in_db(user_id, user)
    return updated


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    delete_user_from_db(user_id)
    return {"deleted": True}


@router.patch("/users/{user_id}/email")
async def update_email(user_id: int, email: str):
    return patch_user_email(user_id, email)


# Route with multiple methods using api_route
@router.api_route("/resources", methods=["GET", "POST"])
async def handle_resources():
    return process_resources()


# Nested router
nested_router = APIRouter(prefix="/nested")


@nested_router.get("/deep/path")
async def deep_nested():
    return {"level": "deep"}


# Helper functions with calls
def check_database_connection():
    ping_db()
    return {"db": "connected"}


def fetch_users_paginated(skip, limit):
    query = build_query(skip, limit)
    return execute_query(query)


def find_user_by_id(user_id):
    return db_find_one("users", user_id)


def validate_email(email):
    if not is_valid_email(email):
        raise ValueError("Invalid email")


def save_user_to_db(user):
    return db_insert("users", user.dict())


def send_notification(user_id):
    push_to_queue("notifications", {"user_id": user_id})


def update_user_in_db(user_id, user):
    return db_update("users", user_id, user.dict())


def delete_user_from_db(user_id):
    db_delete("users", user_id)


def patch_user_email(user_id, email):
    return db_patch("users", user_id, {"email": email})


def process_resources():
    return []


def ping_db():
    pass


def build_query(skip, limit):
    return f"SELECT * LIMIT {limit} OFFSET {skip}"


def execute_query(query):
    return []


def db_find_one(table, id):
    pass


def db_insert(table, data):
    return {"id": 1, **data}


def db_update(table, id, data):
    return {"id": id, **data}


def db_delete(table, id):
    pass


def db_patch(table, id, data):
    return {"id": id, **data}


def is_valid_email(email):
    return "@" in email


def push_to_queue(queue, data):
    pass


# Include routers
app.include_router(router)
app.include_router(nested_router, prefix="/api/v2")
