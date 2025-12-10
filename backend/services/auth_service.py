"""
Auth Service - Authentication and authorization logic
"""

from typing import Optional
from db.database import Database


class AuthService:
    """Service for authentication operations."""

    def __init__(self, db: Database):
        self.db = db

    def authenticate(self, email: str, password: str) -> Optional[dict]:
        """Authenticate user with email and password."""
        user = self.db.fetch_one(
            "SELECT * FROM users WHERE email = :email",
            {"email": email}
        )

        if user and self._verify_password(password, user.get("password", "")):
            token = self.generate_token(user["id"])
            return {
                "access_token": token,
                "token_type": "bearer",
                "user_id": user["id"]
            }
        return None

    def generate_token(self, user_id: int) -> str:
        """Generate JWT token for user."""
        # Simplified token generation
        return f"jwt_token_{user_id}"

    def verify_token(self, token: str) -> Optional[dict]:
        """Verify and decode JWT token."""
        if token.startswith("jwt_token_"):
            user_id = int(token.split("_")[-1])
            return {"user_id": user_id}
        return None

    def _verify_password(self, plain: str, hashed: str) -> bool:
        """Verify password against hash."""
        # Simplified - in production use bcrypt
        return plain == hashed

    def hash_password(self, password: str) -> str:
        """Hash password for storage."""
        # Simplified - in production use bcrypt
        return password
