import tkinter as tk

def on_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def on_clear():
    global expression
    expression = ""
    input_text.set("")

def on_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("Error")
        expression = ""

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x350")

expression = ""
input_text = tk.StringVar()

# Frame for the input field
input_frame = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

# Input field inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for the buttons
btns_frame = tk.Frame(root, width=312, height=272.5, bg="grey")
btns_frame.pack()

# First row (7, 8, 9, *)
tk.Button(btns_frame, text='7', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(7)).grid(row=0, column=0, padx=1, pady=1)
tk.Button(btns_frame, text='8', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(8)).grid(row=0, column=1, padx=1, pady=1)
tk.Button(btns_frame, text='9', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(9)).grid(row=0, column=2, padx=1, pady=1)
tk.Button(btns_frame, text='/', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click('/')).grid(row=0, column=3, padx=1, pady=1)

# Second row (4, 5, 6, *)
tk.Button(btns_frame, text='4', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(4)).grid(row=1, column=0, padx=1, pady=1)
tk.Button(btns_frame, text='5', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(5)).grid(row=1, column=1, padx=1, pady=1)
tk.Button(btns_frame, text='6', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(6)).grid(row=1, column=2, padx=1, pady=1)
tk.Button(btns_frame, text='*', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click('*')).grid(row=1, column=3, padx=1, pady=1)

# Third row (1, 2, 3, -)
tk.Button(btns_frame, text='1', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(1)).grid(row=2, column=0, padx=1, pady=1)
tk.Button(btns_frame, text='2', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(2)).grid(row=2, column=1, padx=1, pady=1)
tk.Button(btns_frame, text='3', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(3)).grid(row=2, column=2, padx=1, pady=1)
tk.Button(btns_frame, text='-', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click('-')).grid(row=2, column=3, padx=1, pady=1)

# Fourth row (C, 0, =, +)
tk.Button(btns_frame, text='C', fg='black', width=10, height=3, bd=0, bg='#fff', command=on_clear).grid(row=3, column=0, padx=1, pady=1)
tk.Button(btns_frame, text='0', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click(0)).grid(row=3, column=1, padx=1, pady=1)
tk.Button(btns_frame, text='=', fg='black', width=10, height=3, bd=0, bg='#fff', command=on_equal).grid(row=3, column=2, padx=1, pady=1)
tk.Button(btns_frame, text='+', fg='black', width=10, height=3, bd=0, bg='#fff', command=lambda: on_click('+')).grid(row=3, column=3, padx=1, pady=1)

root.mainloop()
