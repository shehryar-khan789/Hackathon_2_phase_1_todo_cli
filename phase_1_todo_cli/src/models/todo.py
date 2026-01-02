"""
Module for the TodoItem data class.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TodoItem:
    """
    Represents a single todo item in the application.

    Attributes:
        id: Unique identifier for the todo item (auto-incremented)
        description: The text description of the todo task (required, non-empty)
        status: Current status of the todo item, either "pending" or "complete" (default: "pending")
        created_at: Timestamp of when the todo was created (format: ISO 8601)
    """
    id: int
    description: str
    status: str = "pending"
    created_at: str = ""

    def __post_init__(self):
        """Validate the TodoItem after initialization."""
        if not self.description or not self.description.strip():
            raise ValueError("Description must not be empty or contain only whitespace")

        if self.status not in ["pending", "complete"]:
            raise ValueError("Status must be either 'pending' or 'complete'")

        if not self.created_at:
            # Set the created_at timestamp if not provided
            self.created_at = datetime.now().isoformat()