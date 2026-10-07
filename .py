# পার্ট ১: ভ্যারিয়েবল, ডেটা টাইপ ও কমেন্ট
# --- ১.১ এক লাইনের কমেন্ট (Single-line Comment) ---
# এই লাইনের কোড পাইথন রান করবে না, এটি শুধু নোট।

name = "Siam"  # স্ট্রিং বা টেক্সট ডেটা টাইপ (String) - এটি কোটেশনের ভেতরে থাকে
age = 25        # পূর্ণসংখ্যা ডেটা টাইপ (Integer)
price = 10.50   # দশমিক সংখ্যা ডেটা টাইপ (Float)

# --- ১.২ আউটপুট দেখানো (Print) ---
print(name)
print(age)
print(price)

# --- ১.৩ লেখা জোড়া দেওয়া (String Concatenation) ---
countrty = "Bangladesh"
print("My name is " + name)
print("I live in " + countrty)

# --- ১.৪ একাধিক লাইনের েকমেন্ট (Multi-line Comment) ---
"""
এখানে আমি অনেকগুলো লাইন একসাথে 
নোট হিসেবে লিখে রাখতে পারবো।
পাইথন এগুলোকে এড়িয়ে যাবে।
"""
print("পার্ট ১ সফলভাবে শেষ হলো!")


# পার্ট ২: ইউজার ইনপুট ও টাইপ কাস্টিং
# --- ২.১ ইউজার ইনপুট নেওয়া ---
user_name = input("Enter your name: ")
print("Welcome, " + user_name)

# --- ২.২ টাইপ কাস্টিং ও বয়স হিসাবের ম্যাজিক ---
# input() দিয়ে নেওয়া জন্ম সালকে int() দিয়ে সংখ্যায় রূপান্তর করা হয়েছে
birth_year = input("Enter your birth year: ")
age = 2026 - int(birth_year)

# সংখ্যাকে লেখার সাথে প্রিন্ট করার জন্য str() দিয়ে আবার টেক্সট করা হয়েছে
print("In 2026, your age will be: " + str(age))


# পার্ট ৩: কন্ডিশনাল লজিক (If, Elif(else+if), Else)
# --- ৩.১ ভোটের বয়স পরীক্ষা ---
user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You can vote!") # শর্ত সত্য হলে রান হবে
else:
    print("You are too young to vote.") # শর্ত মিথ্যা হলে রান হবে

# --- ৩.২ একাধিক শর্ত পরীক্ষা (গ্রেডিং সিস্টেম) ---
marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 40:
    print("Grade: C")
else:
    print("Grade: F (Fail)")
    

# পার্ট ৪: লুপের ব্যবহার (For & While Loop)
# --- ৪.১ ফর লুপ (For Loop) ---
# ১০ বার একই লেখা প্রিন্ট করার নিয়ম

for i in range(10):
    print("আমার নাম জাবের")

# ১ থেকে ১০ পর্যন্ত সংখ্যা গণনা করা
for i in range(1, 11):
    print(i)

# --- ৪.২ হোয়াইল লুপ (While Loop) ---
# যতক্ষণ শর্ত সত্যি থাকবে, ততক্ষণ ঘুরবে
count = 1
while count <= 5:
    print("হোয়াইল লুপের সংখ্যা:", count)
    count = count + 1 # মান ১ করে বাড়ানো হচ্ছে যেন আজীবন না চলে


# পার্ট ৫: ডেটা কালেকশন (List, Tuple, Dictionary)
# --- ৫.১ লিস্ট (List) - পরিবর্তনযোগ্য কালেকশন ে---
friends = ["Rahim", "Karim", "Jaber", "Siam"]
print(friends[0]) # ইনডেক্স ০ মানে প্রথম বন্ধু 'Rahim'
print(friends[2]) # ইনডেক্স 2 মানে তৃতীয় বন্ধু 'Jaber'

# লুপ দিয়ে লিস্টের সব আইটেম এক এক করে প্রিন্ট করা
for friend in friends:
    print("বন্ধুর নাম:", friend)

# --- ৫.২ টাপল (Tuple) - পরিবর্তন অযোগ্য কালেকশন ---
days = ("Sunday", "Monday", "Tuesday")
print(days[0]) # এটি তৈরির পর আর বদলানো যায় না

# --- ৫.৩ ডিকশনারি (Dictionary) - চাবি ও মানের জোড়া (Key-Value) ---
student = {
    "name": "Jaber",
    "age": 22,
    "city": "Dhaka"
}
print(student["name"]) # চাবি "name" লিখে মান "Jaber" বের করা হলো
print(student["city"])


# পার্ট ৬: ফাংশন তৈরি ও ব্যবহার (Functions)
# --- ৬.১ সাধারণ ফাংশন ---
def Welcome_message():
    print("হ্যালো জাবের! পাইথন ফাংশন ক্লাসে স্বাগতম।")

Welcome_message() # ফাংশনটি কল বা চালু করা হলো

# --- ৬.২ আর্গুমেন্টসহ ফাংশন (ডেটা পাঠানো) ---
def greet_user(user_name):
    print("হ্যালো " + user_name + ", কেমন আছেন?")

greet_user("Jaber") # 'Jaber' নাম পাঠিয়ে কল করা হলো
greet_user("Siam")


# পার্ট ৭: ফাইল হ্যান্ডলিং (File Handling)
# --- ৭.১ ফাইল তৈরি ও লেখা (Write Mode) ---
file = open("my_story.txt", "w", encoding="utf-8")
file.write("আমি পাইথন প্রোগ্রামিং শিখছি।\n")
file.write("আজ আমি ফাইল হ্যান্ডলিং শিখলাম।")
file.close() # কাজ শেষে ফাইল বন্ধ করা জরুরি
print("ফাইল তৈরি হয়েছে!")

# --- ৭.২ ফাইল পড়া ও টার্মিনালে দেখানো (Read Mode) ---
file = open("my_story.txt", "r", encoding="utf_8")
content = file.read()
print(content) # ফাইলের লেখা টার্মিনালে প্রিন্ট হবে
file.close()


# পার্ট ৮: অবজেক্ট ওরিয়েন্টেড প্রোগ্রামিং (OOP)
# --- ৮.১ ক্লাস বা নকশা তৈরি ---
class Car:
    def __init__(self, brand, color):
        self.brand = brand # গাড়ির নাম
        self.color = color # গাড়ির রং
    
    def start_engine(self):
        print(self.brand + " গাড়ির ইঞ্জিন চালু হয়েছে!")

# --- ৮.২ অবজেক্ট বা আসল গাড়ি তৈরি ---
car1 = Car("Toyota", "Red")
car2 = Car("BMW", "Black")

# --- ৮.৩ অবজেক্ট ব্যবহার ---
print(car1.brand)   # আউটপুট: Toyota
car2.start_engine() # আউটপুট: BMW গাড়ির ইঞ্জিন চালু হয়েছে!


# পার্ট ৯: ভিজ্যুয়াল ও রেসপন্সিভ ক্যালকুলেটর প্রজেক্ট (Tkinter GUI)

import tkinter as tk

def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear_button():
    global expression
    expression = ""
    input_text.set("")

def equal_button():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# মূল উইন্ডো সেটিংস
window = tk.Tk()
window.title("রেসপন্সিভ ক্যালকুলেটর")
window.geometry("350x450")
window.configure(bg="#17171c")

expression = ""
input_text = tk.StringVar()

# ইনপুট স্ক্রিন ডিজাইন
input_frame= tk.Entry(window, textvariable=input_text, font=('Arial', 24, 'bold'), bd=0, bg="#17171c", fg="#ffffff", justify='right')
input_frame.pack(side=tk.TOP, ipady=20, fill=tk.BOTH, padx=10, pady=10)

btns_frame = tk.Frame(window, bg="#17171c")

# সি এবং ভাগ বাটন
tk.Button(btns_frame, text="C", width=16, height=2, font=('Arial', 14, 'bold'), bd=0, bg="#a5a5a5", fg="#000000", cursor="hand2", command=clear_button).grid(row=0, column=0, columnspan=3, padx=2, pady=2)
tk.Button(btns_frame, text="/", width=5, height=2, font=('Arial', 14, 'bold'), bd=0, bg="#ff9f0a", fg="#ffffff", cursor="hand2", command=lambda: click_button("/")).grid(row=0, column=3, padx=2, pady=2)

# বাটন লেআউট
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
    ('0', 4, 0), ('-', 4, 1), ('=', 4, 2)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(btns_frame, text=text, width=5, height=2, font=('Arial', 14, 'bold'), bd=0, bg="#ff9f0a", fg="#ffffff", cursor="hand2", command=equal_button).grid(row=row, column=col, padx=2, pady=2)
    elif text in ['*', '-', '+']:
        tk.Button(btns_frame, text=text, width=5, height=2, font=('Arial', 14, 'bold'), bd=0, bg="#ff9f0a", fg="#ffffff", cursor="hand2", command=lambda t=text: click_button(t)).grid(row=row, column=col, padx=2, pady=2)
    else:
        tk.Button(btns_frame, text=text, width=5, height=2, font=('Arial', 14, 'bold'), bd=0, bg="#333333", fg="#ffffff", cursor="hand2", command=lambda t=text: click_button(t)).grid(row=row, column=col, padx=2, pady=2)
    
# --- রেসপন্সিভ করার ম্যাজিক কোড ---
for r in range(5):
    btns_frame.rowconfigure(r, weight=1)
for c in range(4):
    btns_frame.columnconfigure(c, weight=1)

window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)
btns_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

window.mainloop()