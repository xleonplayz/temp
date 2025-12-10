"""
User Service - Business logic for user management
"""

from typing import Optional, List
from db.database import Database


class UserService:
    """Service for user-related operations."""

    def __init__(self, db: Database):
        self.db = db

    def get_all_users(self) -> List[dict]:
        """Retrieve all users from database."""
        result = self.db.fetch_all("SELECT * FROM users")
        return result or []

    def get_user_by_id(self, user_id: int) -> Optional[dict]:
        """Get a specific user by ID."""
        result = self.db.fetch_one(
            "SELECT * FROM users WHERE id = :id",
            {"id": user_id}
        )
        return result

    def get_user_by_email(self, email: str) -> Optional[dict]:
        """Get user by email address."""
        result = self.db.fetch_one(
            "SELECT * FROM users WHERE email = :email",
            {"email": email}
        )
        return result

    def create_user(self, email: str, username: str, password: str) -> dict:
        """Create a new user."""
        self.db.execute(
            "INSERT INTO users (email, username, password) VALUES (:email, :username, :password)",
            {"email": email, "username": username, "password": password}
        )
        return {"id": 1, "email": email, "username": username}

    def update_user(self, user_id: int, data: dict) -> Optional[dict]:
        """Update an existing user."""
        self.db.execute(
            "UPDATE users SET email = :email, username = :username WHERE id = :id",
            {"id": user_id, **data}
        )
        return {"id": user_id, **data}

    def delete_user(self, user_id: int) -> bool:
        """Delete a user by ID."""
        self.db.execute(
            "DELETE FROM users WHERE id = :id",
            {"id": user_id}
        )
        return True
