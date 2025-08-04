# Calculator CLI App

A simple command-line calculator application built with Python that supports basic arithmetic operations.

## 📋 Project Overview

This is a Python-based command-line interface (CLI) calculator that allows users to perform basic mathematical operations including addition, subtraction, multiplication, and division. The application features a user-friendly menu system and continuous operation until the user chooses to exit.

## ✨ Features

- **Basic Arithmetic Operations**:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)

- **User-Friendly Interface**:
  - Clear menu options/instructions
  - Interactive input prompts
  - Continuous operation loop
  - Graceful exit option

- **Error Handling**:
  - Division by zero protection
  - Invalid input validation
  - Numeric input verification

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system
- Command line/terminal access

### Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/Satyamkumarjha4/Elevate_Labs.git
   cd Calculator
   ```

2. No additional dependencies required - uses only Python standard library

### Running the Application

Navigate to the Calculator directory and run:

```bash
python Calculator.py
```

## 📖 Usage

1. **Start the Application**: Run the Python script to launch the calculator
2. **Select Operation**: Choose from the menu options (1-4) or 'q' to quit:
   - `1` - Addition
   - `2` - Subtraction
   - `3` - Multiplication
   - `4` - Division
   - `q` - Quit the application

3. **Enter Numbers**: Input two numbers when prompted
4. **View Result**: The calculation result will be displayed
5. **Continue or Exit**: Choose another operation or quit

### Example Usage

```
Welcome to the Calculator CLI App!
Select operation:
1. Add (+)
2. Subtract (-)
3. Multiply (*)
4. Divide (/)

Enter choice (1/2/3/4) or 'q' to quit: 1
Enter first number: 15
Enter second number: 25
15.0 + 25.0 = 40.0

Enter choice (1/2/3/4) or 'q' to quit: 4
Enter first number: 10
Enter second number: 2
10.0 / 2.0 = 5.0

Enter choice (1/2/3/4) or 'q' to quit: q
Exiting the calculator. Goodbye!
```

## 🏗️ Code Structure

The application is organized into the following functions:

- `add(x, y)` - Performs addition
- `subtract(x, y)` - Performs subtraction
- `multiply(x, y)` - Performs multiplication
- `divide(x, y)` - Performs division with zero-division error handling
- `calculator()` - Main function containing the user interface and program loop

## 🛡️ Error Handling

The application includes robust error handling for:

- **Division by Zero**: Prevents crashes when dividing by zero
- **Invalid Input**: Catches non-numeric inputs and prompts for valid entries
- **Invalid Menu Choices**: Handles incorrect operation selections

## 🔧 Technical Details

- **Language**: Python 3.x
- **Dependencies**: None (uses Python standard library only)
- **Input/Output**: Command-line interface using `input()` and `print()`
- **Data Types**: Supports floating-point numbers for precise calculations

## 📝 Development Notes

This project was developed as part of a learning exercise focusing on:
- Function-based programming structure
- User input handling
- Loop control structures
- Error handling and validation
- Clean code practices


## 👨‍💻 Author

Created as part of the Elevate Labs development exercises.

---

**Note**: This is a basic calculator implementation designed for learning purposes and can be extended with additional features as needed.