import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operation = operation_var.get()

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error! Division by zero."
        else:
            result = num1 / num2

    result_label.config(text="Result: " + str(result))

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Create entry widgets for input
entry1 = tk.Entry(window)
entry1.grid(row=0, column=0, padx=5, pady=5)

entry2 = tk.Entry(window)
entry2.grid(row=0, column=1, padx=5, pady=5)

# Create dropdown for operation selection
operations = ["+", "-", "*", "/"]
operation_var = tk.StringVar(window)
operation_var.set("+")  # default value
operation_dropdown = tk.OptionMenu(window, operation_var, *operations)
operation_dropdown.grid(row=0, column=2, padx=5, pady=5)

# Create button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Create label to display result
result_label = tk.Label(window, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
