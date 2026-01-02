# Todo API Contracts

## CLI Command Contracts

### Add Todo
**Command**: `todo add <description>`
- **Input**: description (string) - the todo task description
- **Output**: Success message with assigned ID
- **Error cases**:
  - Empty description → Error message to stderr
  - Invalid command format → Error message to stderr

### List Todos
**Command**: `todo list` or `todo view`
- **Input**: None
- **Output**: List of all todos with ID, description, and status
- **Error cases**: None (empty list is valid)

### Complete Todo
**Command**: `todo complete <id>` or `todo mark <id> complete`
- **Input**: id (integer) - the unique ID of the todo to mark complete
- **Output**: Success confirmation message
- **Error cases**:
  - Non-existent ID → Error message to stderr
  - Invalid ID format → Error message to stderr

### Delete Todo
**Command**: `todo delete <id>`
- **Input**: id (integer) - the unique ID of the todo to delete
- **Output**: Success confirmation message
- **Error cases**:
  - Non-existent ID → Error message to stderr
  - Invalid ID format → Error message to stderr

### Update Todo
**Command**: `todo update <id> <new_description>`
- **Input**: id (integer) - the unique ID of the todo to update, new_description (string) - the new description
- **Output**: Success confirmation message
- **Error cases**:
  - Non-existent ID → Error message to stderr
  - Invalid ID format → Error message to stderr
  - Empty new_description → Error message to stderr

## Data Contracts

### TodoItem Response Format
```
{
  "id": integer,
  "description": string,
  "status": "pending" | "complete",
  "created_at": string (ISO 8601 format)
}
```

### Success Response Format
```
{
  "status": "success",
  "message": string,
  "data": object (optional)
}
```

### Error Response Format
```
{
  "status": "error",
  "message": string
}
```

## CLI Output Format
- All successful operations output to stdout
- All error messages output to stderr
- Human-readable format for all outputs