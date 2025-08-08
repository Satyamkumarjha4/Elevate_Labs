# To-Do List Application

A feature-rich console-based to-do list manager built with Python that provides task management with persistence, priority levels, and colorful terminal interface.

## 📋 Project Overview

This is a Python-based command-line to-do list application that allows users to manage tasks efficiently. The application features persistent storage, task prioritization, status tracking, and a colorful user interface using the `colorama` library for enhanced user experience.

## ✨ Features

### Core Functionality
- **Add Tasks**: Create new tasks with descriptions and priority levels
- **Remove Tasks**: Delete tasks from your list
- **View Tasks**: Display all tasks in a formatted table
- **Mark Completed**: Update task status to completed
- **Persistent Storage**: Tasks are automatically saved to a text file

### Advanced Features
- **Task Prioritization**: Set priority levels (Low, Medium, High)
- **Status Tracking**: Tasks can be "Pending" or "Completed"
- **Colorful Interface**: Enhanced terminal experience with color-coded output
- **Data Validation**: Input validation for priority levels and task numbers
- **File Management**: Automatic directory creation and file handling

### Visual Elements
- 🔴 Red color for pending tasks
- 🟢 Green color for completed tasks
- 🔵 Blue color for headers and menus
- 🟡 Yellow color for warnings and prompts
- 🟣 Magenta color for menu options

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- `colorama` library for colored terminal output

### Installation

1. Clone or download the repository:
   ```bash
   git clone <repository-url>
   cd To-Do-List
   ```

2. Install required dependencies:
   ```bash
   pip install colorama
   ```

### Running the Application

Navigate to the To-Do-List directory and run:

```bash
python to_do_list.py
```

## 📖 Usage

### Main Menu Options

The application presents a menu with the following options:

1. **Add Task** - Create a new task with description and priority
2. **Remove Task** - Delete an existing task
3. **View Tasks** - Display all current tasks
4. **Mark Task as Completed** - Change task status to completed
5. **Exit** - Close the application

### Adding Tasks

1. Select option `1` from the main menu
2. Enter a task description
3. Set priority level (Low/Medium/High)
4. Task is automatically saved

### Viewing Tasks

Tasks are displayed in a formatted table showing:
- Task number
- Description
- Status (Pending/Completed)
- Priority level

### Managing Tasks

- **Remove**: Select option `2`, view tasks, enter task number to remove
- **Complete**: Select option `4`, view tasks, enter task number to mark as completed

### Example Usage

```
📋 To-Do List Menu
1. Add Task
2. Remove Task
3. View Tasks
4. Mark Task as Completed
5. Exit

Choose an option (1-5): 1
Enter task description: Buy groceries
Enter priority (Low/Medium/High): High
Task 'Buy groceries' added.

📋 To-Do List Menu
...
Choose an option (1-5): 3

Your Tasks:
--------------------------------------------------
No.  Description              Status     Priority  
--------------------------------------------------
1    Buy groceries            Pending    High      
--------------------------------------------------
```

## 🏗️ Code Architecture

### Classes

#### `Task` Class
- **Attributes**:
  - `description`: Task description text
  - `status`: Current status (Pending/Completed)
  - `priority`: Priority level (Low/Medium/High)
- **Methods**:
  - `__str__()`: String representation for display
  - `to_line()`: Format for file storage
  - `from_line()`: Parse task from file line

#### `ToDoList` Class
- **Attributes**:
  - `filename`: Path to the tasks storage file
  - `tasks`: List of Task objects
- **Methods**:
  - `load_tasks()`: Load tasks from file
  - `save_tasks()`: Save tasks to file
  - `add_task()`: Add new task
  - `remove_task()`: Remove task by index
  - `mark_completed()`: Mark task as completed
  - `view_tasks()`: Display all tasks

### File Structure

```
To-Do-List/
├── to_do_list.py       # Main application file
├── tasks.txt           # Task storage file (auto-created)
└── README.md           # This documentation
```

## 💾 Data Persistence

Tasks are automatically saved to `tasks.txt` in the following format:
```
Task Description||Status||Priority
```

Example:
```
Buy groceries||Pending||High
Complete project||Completed||Medium
```

## 🛡️ Error Handling

The application includes comprehensive error handling for:

- **Invalid Menu Choices**: Handles incorrect option selections
- **Invalid Task Numbers**: Validates task indices for removal/completion
- **Invalid Priority Levels**: Defaults to "Medium" for invalid entries
- **Empty Task Lists**: Graceful handling of operations on empty lists
- **File I/O Errors**: Automatic directory creation and file management
- **Input Validation**: Numeric input verification

## 🎨 Dependencies

- **colorama**: For cross-platform colored terminal text output
  ```bash
  pip install colorama
  ```

## 🔧 Technical Details

- **Language**: Python 3.x
- **File I/O**: Text file storage with custom delimiter format
- **UI**: Console-based with colorama for enhanced visuals
- **Data Structure**: Object-oriented design with Task and ToDoList classes
- **Persistence**: Automatic save/load functionality

## 📁 File Management

- Tasks are stored in `To-Do-List/tasks.txt`
- Directory is automatically created if it doesn't exist
- File is created on first task addition
- Data is saved after every modification

## 🚀 Future Enhancements

Potential improvements for the application:

- **Due Dates**: Add deadline functionality
- **Categories**: Organize tasks by categories
- **Search**: Find tasks by keywords
- **Export**: Export tasks to different formats
- **Reminders**: Add notification system
- **GUI Version**: Create a graphical interface
- **Cloud Sync**: Synchronize across devices

## 🤝 Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional features (due dates, categories, etc.)
- Enhanced error handling
- Performance optimizations
- UI/UX improvements
- Code refactoring

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as part of the Elevate Labs development exercises.

## 🐛 Troubleshooting

### Common Issues

1. **Module not found (colorama)**:
   ```bash
   pip install colorama
   ```

2. **Permission errors**: Ensure write permissions in the application directory

3. **File not found**: The application automatically creates necessary files and directories

---

**Note**: This is a console-based application designed for learning purposes and demonstrates object-oriented programming, file I/O, and user interface design principles.