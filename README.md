Scientific Calculator
Description:
This is a simple Scientific Calculator built using Python and the Tkinter library. It provides basic arithmetic operations along with scientific functions like sine, cosine, tangent, logarithm, square root, exponentiation, and pi.
Features:
Basic arithmetic operations: Addition, Subtraction, Multiplication, and Division.
Scientific functions: sin, cos, tan, log, sqrt, and exp.
A graphical user interface (GUI) using Tkinter.
Clear (AC) button to reset the input.
Evaluation of expressions using Python’s eval() function.
Installation & Setup
Prerequisites
Ensure you have Python 3.x installed on your system.
Steps to Run the Application
Download or clone the repository.
Navigate to the project directory.
Run the following command:
python calculator.py
The calculator GUI should launch.
Code Breakdown
1. Initializing the Calculator Class
The Calculator class is created, taking master (Tk root window) as an argument.
It initializes an expression string and a StringVar to store the input.
The main display (Entry widget) is created.
2. Creating Buttons
A function create_buttons() defines and places buttons for digits (0-9), operations (+, -, *, /), and scientific functions.
Buttons are mapped to respective functions using lambda.
3. Handling Button Clicks
click(item): Appends numbers/operators to the input expression.
evaluate(): Parses and evaluates the expression using eval().
scientific_func(func): Performs scientific calculations using math functions.
clear(): Resets the display.
4. Scientific Functionality
Functions like sin, cos, tan, and log convert values and apply the respective math module functions.
5. Running the Application
The main() function initializes Tkinter and starts the main event loop.
if __name__ == "__main__": Ensures the script runs only when executed directly.
Potential Improvements
Add support for parentheses to handle complex expressions.
Implement an error-handling mechanism for division by zero.
Improve the UI with additional themes and better button spacing.
Include more scientific functions like factorial and power functions.
License
This project is licensed under the MIT License.
Author
Developed by Ryan M.
