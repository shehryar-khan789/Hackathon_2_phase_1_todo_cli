# 📝 Simple Interactive Todo CLI (Python)

A simple in-memory Todo application built in Python.  
The app is interactive, menu-based, and stores tasks only in memory (data will be lost when you exit).  

This project was built using **Spec-Driven Development** with **Claude Code** and **Spec-Kit Plus** for planning and implementation. ✅

# 1. Features

1. Add new Todos  
2. View all Todos with status ✔ / ❌  
3. Update existing Todos  
4. Delete Todos  
5. Mark Todos as complete  
6. Simple menu-based interaction, no need to type commands  

# 2. Installation

1. Clone the repository
git clone <https://github.com/shehryar-khan789/Hackathon_2_phase_1_todo_cli>
cd <phase_1_todo_cli>



2. Run the application
python todo_cli.py


# 3. How to Use

1. Run `python todo_cli.py`  
2. Menu will appear with numbered options  
3. Type the number to select an action:
   1. Add Todo
   2. View Todos
   3. Update Todo
   4. Delete Todo
   5. Mark Complete
   0. Exit  
4. Follow on-screen prompts to manage your Todos  

# 4. Approach / How It Works

1. **In-Memory Storage**: Todos are stored in a Python list of dictionaries. No files or databases are used. Data is lost when the app exits.  
2. **Interactive Menu Loop**: The app runs in a continuous loop, showing a menu for the user to select options — no commands need to be typed.  
3. **Function-Based Design**: Each action has its own function (`add_todo()`, `view_todos()`, etc.) for clean and maintainable code.  
4. **Error Handling**: Handles invalid indexes and wrong inputs gracefully, preventing crashes.  
5. **Optional Colors / Icons**: Can display colored success/error messages and ✔ / ❌ icons for better UX.  
6. **Simple CLI UX**: Users interact via prompts, select menu options, and see immediate feedback — like a small console app.  
7. **Spec-Driven Development**: The project was planned and implemented using Claude Code and Spec-Kit Plus, following a spec-driven approach to ensure clarity, modularity, and structured development.  

# 5. Contributing

Feel free to fork the repo, improve features, or suggest changes. Pull requests are welcome. 👍  

# 6. License

MIT License  

Made with ❤️ by Shehryar








