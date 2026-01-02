"""
Todo service for managing todo items in memory.
"""
from typing import List, Optional
from src.models.todo import TodoItem
from src.lib.constants import TODO_STATUS_COMPLETE, TODO_STATUS_PENDING


class TodoService:
    """
    Service class for managing todo items with in-memory storage.
    """
    def __init__(self):
        """Initialize the service with an empty list of todos."""
        self.todos: List[TodoItem] = []
        self._next_id = 1

    def add_todo(self, description: str) -> TodoItem:
        """
        Add a new todo item with the given description.

        Args:
            description: The description of the todo item

        Returns:
            The created TodoItem with assigned ID and timestamp

        Raises:
            ValueError: If description is empty
        """
        if not description or not description.strip():
            raise ValueError("Description must not be empty or contain only whitespace")

        todo = TodoItem(
            id=self._get_next_id(),
            description=description.strip()
        )
        self.todos.append(todo)
        return todo

    def get_all_todos(self) -> List[TodoItem]:
        """
        Get all todo items.

        Returns:
            List of all todo items
        """
        return self.todos

    def get_todo_by_id(self, todo_id: int) -> Optional[TodoItem]:
        """
        Get a todo item by its ID.

        Args:
            todo_id: The ID of the todo item

        Returns:
            The todo item if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo item as complete.

        Args:
            todo_id: The ID of the todo item to mark complete

        Returns:
            True if the todo was found and marked complete, False otherwise
        """
        todo = self.get_todo_by_id(todo_id)
        if todo and todo.status != TODO_STATUS_COMPLETE:
            todo.status = TODO_STATUS_COMPLETE
            return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo item by its ID.

        Args:
            todo_id: The ID of the todo item to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                self.todos.pop(i)
                return True
        return False

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update a todo item's description.

        Args:
            todo_id: The ID of the todo item to update
            new_description: The new description for the todo

        Returns:
            True if the todo was found and updated, False otherwise
        """
        if not new_description or not new_description.strip():
            raise ValueError("New description must not be empty or contain only whitespace")

        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.description = new_description.strip()
            return True
        return False

    def _get_next_id(self) -> int:
        """
        Get the next available ID for a new todo item.

        Returns:
            The next available ID
        """
        current_id = self._next_id
        self._next_id += 1
        return current_id