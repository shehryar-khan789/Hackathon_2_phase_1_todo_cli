"""
Interactive Menu-Based CLI interface for the Todo application.
"""
import sys
from typing import Optional
from src.services.todo_service import TodoService
from src.models.todo import TodoItem
from src.lib.constants import STATUS_SYMBOL_COMPLETE, STATUS_SYMBOL_PENDING


class TodoCLI:
    """
    Interactive Menu-Based Command Line Interface for the Todo application.
    """
    def __init__(self):
        """Initialize the CLI with a TodoService instance."""
        self.service = TodoService()

    def display_menu(self) -> None:
        """Display the main menu options."""
        print("\n" + "="*40)
        print("TODO APPLICATION - INTERACTIVE MENU")
        print("="*40)
        print("1. Add Todo")
        print("2. View Todos")
        print("3. Update Todo")
        print("4. Delete Todo")
        print("5. Mark Todo as Complete")
        print("0. Exit")
        print("="*40)

    def get_user_choice(self) -> int:
        """Get and validate user's menu choice."""
        try:
            choice = int(input("Enter your choice (0-5): "))
            if 0 <= choice <= 5:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
                return -1
        except ValueError:
            print("Invalid input. Please enter a number.")
            return -1

    def run(self) -> None:
        """
        Run the interactive CLI application with menu options.
        """
        print("Welcome to the Interactive Todo Application!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == -1:
                # Invalid input, continue the loop
                input("\nPress Enter to continue...")
                continue

            if choice == 0:
                print("Thank you for using the Todo Application. Goodbye!")
                break
            elif choice == 1:
                self.handle_add_interactive()
            elif choice == 2:
                self.handle_list()
            elif choice == 3:
                self.handle_update_interactive()
            elif choice == 4:
                self.handle_delete_interactive()
            elif choice == 5:
                self.handle_complete_interactive()

            # Pause to let user see the result before showing menu again
            if choice != 0:
                input("\nPress Enter to continue...")

    def handle_add_interactive(self) -> None:
        """Handle adding a todo interactively."""
        title = input("Enter todo title: ").strip()

        if not title:
            print("Error: Title cannot be empty.")
            return

        try:
            todo = self.service.add_todo(title)
            print(f"Todo added successfully! ID {todo.id} - '{todo.description}'")
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)

    def handle_list(self) -> None:
        """Handle listing all todos."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos found.")
            return

        print("\n" + "-"*50)
        print("YOUR TODOS:")
        print("-"*50)

        for todo in todos:
            status_symbol = STATUS_SYMBOL_COMPLETE if todo.status == "complete" else STATUS_SYMBOL_PENDING
            print(f"{todo.id}. [{status_symbol}] {todo.description}")

        print("-"*50)

    def handle_complete_interactive(self) -> None:
        """Handle marking a todo as complete interactively."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to mark as complete.")
            return

        self.handle_list()

        try:
            todo_id = int(input("Enter the ID of the todo to mark as complete: "))

            # Check if todo exists
            todo = self.service.get_todo_by_id(todo_id)
            if not todo:
                print(f"Error: Todo with ID {todo_id} not found.")
                return

            if todo.status == "complete":
                print(f"Todo with ID {todo_id} is already marked as complete.")
                return

            success = self.service.mark_complete(todo_id)
            if success:
                print(f"Todo marked as complete! '{todo.description}'")
            else:
                print(f"Error: Could not mark todo as complete.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def handle_delete_interactive(self) -> None:
        """Handle deleting a todo interactively."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to delete.")
            return

        self.handle_list()

        try:
            todo_id = int(input("Enter the ID of the todo to delete: "))

            # Find the todo to show its title before deletion
            todo = self.service.get_todo_by_id(todo_id)
            if not todo:
                print(f"Error: Todo with ID {todo_id} not found.")
                return

            success = self.service.delete_todo(todo_id)
            if success:
                print(f"Todo deleted successfully! '{todo.description}'")
            else:
                print(f"Error: Could not delete todo.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")

    def handle_update_interactive(self) -> None:
        """Handle updating a todo interactively."""
        todos = self.service.get_all_todos()

        if not todos:
            print("No todos available to update.")
            return

        self.handle_list()

        try:
            todo_id = int(input("Enter the ID of the todo to update: "))

            # Check if todo exists
            todo = self.service.get_todo_by_id(todo_id)
            if not todo:
                print(f"Error: Todo with ID {todo_id} not found.")
                return

            new_title = input("Enter new title: ").strip()
            if not new_title:
                print("Error: Title cannot be empty.")
                return

            old_title = todo.description
            success = self.service.update_todo(todo_id, new_title)
            if success:
                print(f"Todo updated successfully! '{old_title}' -> '{new_title}'")
            else:
                print(f"Error: Could not update todo.")

        except ValueError:
            print("Invalid input. Please enter a valid ID.")


def main():
    """Main entry point for the CLI application."""
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()