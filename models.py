"""Data models for the Library Assistant."""

from typing import Optional
from pydantic import BaseModel


class UserContext(BaseModel):
    """User context with name and member_id."""
    name: str
    member_id: Optional[str] = None
