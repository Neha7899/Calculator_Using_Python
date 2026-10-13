
import tkinter as tk

# Main application window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#202124")

# Display screen
expression = ""

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=0,
    bg="#303134",
    fg="white",
    insertbackground="white"
)
display.pack(fill="x", padx=15, pady=20, ipady=15)


# Function to display button values
def press(value):
    display.insert(tk.END, value)


# Function to clear the display
def clear():
    display.delete(0, tk.END)


# Function to calculate the result
def calculate():
    try:
        result = eval(display.get())

        if isinstance(result, float):
            result = round(result, 10)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid Expression")


# Calculator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", ".", "+"],
    ["="]
]

# Button layout
for row_index, row in enumerate(buttons):
    frame = tk.Frame(root, bg="#202124")
    frame.pack(expand=True, fill="both", padx=10)

    for value in row:
        color = "#f9ab00" if value in ["/", "*", "-", "+", "="] else "#3c4043"

        if value == "C":
            color = "#d93025"

        button = tk.Button(
            frame,
            text=value,
            font=("Arial", 16, "bold"),
            bg=color,
            fg="white",
            activebackground="#5f6368",
            activeforeground="white",
            bd=0,
            command=(
                clear if value == "C"
                else calculate if value == "="
                else lambda v=value: press(v)
            )
        )

        button.pack(
            side="left",
            expand=True,
            fill="both",
            padx=4,
            pady=4
        )

# Run the application
root.mainloop()
