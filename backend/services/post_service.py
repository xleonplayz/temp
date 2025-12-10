"""
Post Service - Business logic for post management
"""

from typing import Optional, List
from db.database import Database


class PostService:
    """Service for post-related operations."""

    def __init__(self, db: Database):
        self.db = db

    def get_all_posts(self) -> List[dict]:
        """Retrieve all posts."""
        result = self.db.fetch_all("SELECT * FROM posts ORDER BY created_at DESC")
        return result or []

    def get_post_by_id(self, post_id: int) -> Optional[dict]:
        """Get a specific post by ID."""
        result = self.db.fetch_one(
            "SELECT * FROM posts WHERE id = :id",
            {"id": post_id}
        )
        return result

    def get_posts_by_user(self, user_id: int) -> List[dict]:
        """Get all posts by a specific user."""
        result = self.db.fetch_all(
            "SELECT * FROM posts WHERE user_id = :user_id ORDER BY created_at DESC",
            {"user_id": user_id}
        )
        return result or []

    def create_post(self, title: str, content: str, user_id: int) -> dict:
        """Create a new post."""
        self.db.execute(
            "INSERT INTO posts (title, content, user_id) VALUES (:title, :content, :user_id)",
            {"title": title, "content": content, "user_id": user_id}
        )
        return {"id": 1, "title": title, "content": content, "user_id": user_id}

    def update_post(self, post_id: int, data: dict) -> Optional[dict]:
        """Update an existing post."""
        self.db.execute(
            "UPDATE posts SET title = :title, content = :content WHERE id = :id",
            {"id": post_id, **data}
        )
        return {"id": post_id, **data}

    def delete_post(self, post_id: int) -> bool:
        """Delete a post by ID."""
        self.db.execute(
            "DELETE FROM posts WHERE id = :id",
            {"id": post_id}
        )
        return True
