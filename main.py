import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    name = en.get()
    weight = en1.get()
    height = en2.get()
    gender = selected_option.get()
    age = en3.get()

    try:
        # Convert inputs to appropriate data types
        weight = float(weight)
        height = float(height) / 100  # Convert height to meters
        age = int(age)

        # Validate inputs
        if weight <= 0 or height <= 0 or name == '' or age < 0:
            raise ValueError("Invalid input")

        # Calculate BMI
        bmi = weight / (height ** 2)
        formatted_bmi = "{:.2f}".format(bmi)

        # Determine BMI status
        bmi_status = get_bmi_status(bmi)

        # Display BMI result and status
        result_text = f"{formatted_bmi}\n  {bmi_status}"
        result_label.config(text=result_text)

        # Save result to text file
        save_to_file(name, formatted_bmi, bmi_status,age,gender)

    except ValueError:
        messagebox.showerror(title="BMI Calculator", message="Please enter valid details for valid calculations.")

def get_bmi_status(bmi): 
    if bmi < 18.5:
        result_label.config(fg="Blue",bg="gray")
        # bmiwin.config(bg="blue")
        return "Underweight"
    elif 18.5 <= bmi < 25:
        result_label.config(fg="green",bg="gray")
        # bmiwin.config(bg="green")
        return "Normal"
    elif 25 <= bmi < 30:
        result_label.config(fg="yellow",bg="gray")
        # bmiwin.config(bg="yellow")
        return "Overweight"
    else:
        result_label.config(fg="red",bg="gray")
        # bmiwin.config(bg="red")
        return "Obese"

def save_to_file(name, bmi, status,age,gender):
    with open("bmi_results.txt", "a") as file:
        file.write(f"Name: {name}\nBMI: {bmi}\nStatus: {status}\nGender: {gender}\nage: {age} \n \n")

bmiwin = tk.Tk()
bmiwin.geometry("400x600")
bmiwin.title("BMI Calculator")

l1 = tk.Label(bmiwin, text="BMI CALCULATOR", font=('console', 12, 'bold'), bg="black", fg="white")
l1.place(x=130, y=20)

l2 = tk.Label(bmiwin, text="Name : ", font=('console', 10, 'bold'), bg="gray", fg="white")
l2.place(x=50, y=60)
en = tk.Entry(bmiwin, width=20, font=('console', 16, "bold"))
en.place(x=100, y=62)

l3 = tk.Label(bmiwin, text="Weight : ", font=('console', 10, 'bold'), bg="gray", fg="white")
l3.place(x=50, y=100)
en1 = tk.Entry(bmiwin, width=10, font=('console', 15, "bold"))
en1.place(x=120, y=102)
l4 = tk.Label(bmiwin, text="kg", bg="gray", fg="black", font=('console', 10, 'bold'))
l4.place(x=280, y=102)

l5 = tk.Label(bmiwin, text="Height : ", font=('console', 10, 'bold'), bg="gray", fg="white")
l5.place(x=50, y=150)
en2 = tk.Entry(bmiwin, width=10, font=('console', 15, "bold"))
en2.place(x=120, y=152)
l6 = tk.Label(bmiwin, text="cm", bg="gray", fg="black", font=('console', 10, 'bold'))
l6.place(x=280, y=152)

options = ["Male", "Female", "Other"]
l7 = tk.Label(bmiwin, text="Gender", bg="gray", fg="White", font=('console', 10, 'bold'))
l7.place(x=50, y=200)
selected_option = tk.StringVar(bmiwin)
selected_option.set(options[0])
option_menu = tk.OptionMenu(bmiwin, selected_option, *options)
option_menu.config(width=10)
option_menu.place(x=120, y=200)

l8 = tk.Label(bmiwin, text="Age : ", font=('console', 10, 'bold'), bg="gray", fg="white")
l8.place(x=250, y=200)
en3 = tk.Entry(bmiwin, width=3, font=('console', 15, "bold"))
en3.place(x=300, y=200)

btn = tk.Button(bmiwin, text="Calculate", bg="red", fg="white", font=('console', 12, 'bold'), width=10, command=calculate_bmi)
btn.place(x=150, y=250)

result_label = tk.Label(bmiwin, text="", font=('console', 25, 'bold'), bg="gray", fg="white", wraplength=300)
result_label.place(x=100, y=300)

def show_saved_results():
    saved_window = tk.Toplevel(bmiwin)
    saved_window.title("History")
    saved_window.geometry("300x400")

    saved_label = tk.Label(saved_window, text="Saved BMI Results", font=('console', 12, 'bold'))
    saved_label.pack()

    with open("bmi_results.txt", "r") as file:
        saved_text = file.read()

    saved_textbox = tk.Text(saved_window, width=40, height=20)
    saved_textbox.insert(tk.END, saved_text)
    saved_textbox.pack()

view_saved_btn = tk.Button(bmiwin, text="History", bg="blue", fg="white", font=('console', 12, 'bold'), width=15, command=show_saved_results)
view_saved_btn.place(x=120, y=550)

bmiwin.resizable(width=False, height=False)
bmiwin.config(bg="gray")
bmiwin.mainloop()
