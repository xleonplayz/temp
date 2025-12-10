"""
Database Connection and Session Management
"""

from typing import Generator


class Database:
    """Simple database abstraction layer."""

    def __init__(self, connection_string: str = "sqlite:///./app.db"):
        self.connection_string = connection_string
        self._connected = False

    def connect(self):
        """Establish database connection."""
        self._connected = True
        return self

    def disconnect(self):
        """Close database connection."""
        self._connected = False

    def execute(self, query: str, params: dict = None):
        """Execute a database query."""
        # Simulated execution
        return {"query": query, "params": params}

    def fetch_one(self, query: str, params: dict = None):
        """Fetch a single row."""
        return None

    def fetch_all(self, query: str, params: dict = None):
        """Fetch all rows."""
        return []


# Global database instance
_db = Database()


def get_db() -> Generator[Database, None, None]:
    """Dependency injection for database sessions."""
    try:
        _db.connect()
        yield _db
    finally:
        _db.disconnect()
