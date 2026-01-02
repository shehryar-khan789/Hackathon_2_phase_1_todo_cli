# Data Model: Todo In-Memory Python Console App (Phase I)

## TodoItem Entity

**Definition**: Represents a single todo item in the application

**Fields**:
- `id`: Integer - Unique identifier for the todo item (auto-incremented)
- `description`: String - The text description of the todo task (required, non-empty)
- `status`: String - Current status of the todo item, either "pending" or "complete" (default: "pending")
- `created_at`: String - Timestamp of when the todo was created (format: ISO 8601)

**Validation Rules**:
- `id` must be unique within the application instance
- `description` must not be empty or contain only whitespace
- `status` must be either "pending" or "complete"
- `created_at` is automatically set when the item is created

**State Transitions**:
- `pending` → `complete`: When user marks the todo as complete
- No reverse transition allowed (completed todos remain complete)

## In-Memory Storage

**Structure**: Python list containing TodoItem objects

**Behavior**:
- Items are stored in the order they were added
- Items persist only in memory for the duration of the application run
- No external persistence mechanism
- All operations are performed in memory only

## Relationships

None - The TodoItem is a standalone entity with no relationships to other entities in this Phase I implementation.