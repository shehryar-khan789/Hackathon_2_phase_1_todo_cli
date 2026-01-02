"""
Application constants for the Todo CLI app.
"""

# Status constants
TODO_STATUS_PENDING = "pending"
TODO_STATUS_COMPLETE = "complete"

# Status symbols for display
STATUS_SYMBOL_COMPLETE = "✔"
STATUS_SYMBOL_PENDING = "❌"

# Command constants
COMMAND_ADD = "add"
COMMAND_LIST = "list"
COMMAND_VIEW = "view"
COMMAND_COMPLETE = "complete"
COMMAND_MARK = "mark"
COMMAND_DELETE = "delete"
COMMAND_UPDATE = "update"

# Error messages
ERROR_EMPTY_DESCRIPTION = "Error: Description cannot be empty"
ERROR_INVALID_ID = "Error: Invalid todo ID"
ERROR_TODO_NOT_FOUND = "Error: Todo not found"
ERROR_EMPTY_UPDATE = "Error: New description cannot be empty"

# Success messages
SUCCESS_TODO_ADDED = "Todo added successfully"
SUCCESS_TODO_COMPLETED = "Todo marked as complete"
SUCCESS_TODO_DELETED = "Todo deleted successfully"
SUCCESS_TODO_UPDATED = "Todo updated successfully"