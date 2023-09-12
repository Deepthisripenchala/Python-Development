import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result.set(num1 + num2)
        elif operation == "Subtraction":
            result.set(num1 - num2)
        elif operation == "Multiplication":
            result.set(num1 * num2)
        elif operation == "Division":
            if num2 == 0:
                result.set("Cannot divide by zero")
            else:
                result.set(num1 / num2)
    except ValueError:
        result.set("Invalid input")

# Create the main application window
app = tk.Tk()
app.title("Calculator")

# Entry fields for numbers
entry1 = tk.Entry(app)
entry2 = tk.Entry(app)

entry1.grid(row=0, column=0, padx=10, pady=10)
entry2.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for selecting the operation
operation_var = tk.StringVar(app)
operation_var.set("Addition")  # Default operation

operation_menu = tk.OptionMenu(app, operation_var, "Addition", "Subtraction", "Multiplication", "Division")
operation_menu.grid(row=0, column=2, padx=10, pady=10)

# Button to perform calculation
calculate_button = tk.Button(app, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Result display
result = tk.StringVar(app)
result_label = tk.Label(app, textvariable=result)
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Button to clear the input fields
clear_button = tk.Button(app, text="Clear", command=lambda: [entry1.delete(0, 'end'), entry2.delete(0, 'end'), result.set("")])
clear_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Run the application
app.mainloop()
