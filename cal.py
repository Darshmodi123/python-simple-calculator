import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

# Display box
entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4)


# Add number/operator
def press(value):
    entry.insert(tk.END, value)


# Calculate
def equal():
    result = eval(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, result)


# Clear display
def clear():
    entry.delete(0, tk.END)


# Buttons
data = [
["7","8","9","/"],
["4","5","6","*"],
["1","2","3","-"],
["C","0","=","+"]
]

# Create buttons
for i in range(4):
    for j in range(4):

        value = data[i][j]

        if value == "=":
            command = equal

        elif value == "C":
            command = clear

        else:
            command = lambda x=value: press(x)

        tk.Button(
            root,
            text=value,
            width=6,
            height=3,
            command=command
        ).grid(row=i+1, column=j)


root.mainloop()
