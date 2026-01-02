# Quickstart Guide: Todo In-Memory Python Console App

## Prerequisites
- Python 3.13+ installed on your system

## Getting Started

1. **Run the application**:
   ```bash
   python -m src.cli.todo_cli
   ```

2. **Add a new todo**:
   ```bash
   python -m src.cli.todo_cli add "Buy groceries"
   ```

3. **View all todos**:
   ```bash
   python -m src.cli.todo_cli list
   ```

4. **Mark a todo as complete**:
   ```bash
   python -m src.cli.todo_cli complete 1
   ```

5. **Delete a todo**:
   ```bash
   python -m src.cli.todo_cli delete 1
   ```

6. **Update a todo**:
   ```bash
   python -m src.cli.todo_cli update 1 "Buy groceries and cook dinner"
   ```

## Available Commands
- `add <description>` - Add a new todo
- `list` or `view` - View all todos
- `complete <id>` or `mark <id> complete` - Mark a todo as complete
- `delete <id>` - Delete a todo
- `update <id> <new_description>` - Update a todo description

## Example Workflow
```bash
# Add some todos
python -m src.cli.todo_cli add "Complete project proposal"
python -m src.cli.todo_cli add "Schedule team meeting"
python -m src.cli.todo_cli add "Review code changes"

# View all todos
python -m src.cli.todo_cli list

# Mark a todo as complete
python -m src.cli.todo_cli complete 1

# Update a todo
python -m src.cli.todo_cli update 2 "Schedule team meeting with stakeholders"

# View updated list
python -m src.cli.todo_cli list
```