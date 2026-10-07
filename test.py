

import tkinter as tk

# বাটন ক্লিকের ফাংশন 
def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# স্ক্রিন ক্লিয়ার করার ফাংশন
def clear_button():
    global expression
    expression = " "
    input_text.set(" ")

# হিসার করার ফাংশন
def equal_button():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = " "

# মূল উইন্ডো সেটআপ
window = tk.Tk()
window.title("আমার ক্যালকুলেটর")
window.geometry("300x400")

expression = " "
input_text = tk.StringVar()

# ইনপুট স্ক্রিন
input_frame = tk.Entry(window, textvariable=input_text, font=('Arial', 20), bd=10, insertwidth=4, width=14, borderwidth=5, justify='right')
input_frame.pack(side=tk.TOP, ipady=10, fill=tk.BOTH)

# বাটনে লেআউট তৈরি
btns_frame = tk.Frame(window)
btns_frame.pack()

# প্রথম সারির বাটন
tk.Button(btns_frame, text="C", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=clear_button).grid(row=0, column=0, columnspan=3)
tk.Button(btns_frame, text="/", width=7, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click_button("/")).grid(row=0, column=3)

# সংখ্যা ও চিহ্নের বাটন সাজানো
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('-', 4, 1), ('=', 4, 2)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(btns_frame, text=text, width=7, height=3, bd=0, bg="#eee", cursor="hand2", command=equal_button).grid(row=row, column=col)
    else:
        tk.Button(btns_frame, text=text, width=7, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: click_button(t)).grid(row=row, column=col)

window.mainloop()