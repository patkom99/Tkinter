import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os



"""
I created this GUI with the help of tkinter.
Basically it take user details through form and store it in csv file or text file.

"""





win = tk.Tk()
win.title("GUI")

#Label
name_label = tk.Label(win, text = "Enter Your Name : ")
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text = "Enter Your Age : ")
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text="Enter Your Email : ")
email_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text="Select your Gender : ")
gender_label.grid(row=3,column=0, sticky=tk.W)


# Entry box
name_var = tk.StringVar()
name_entry_box = ttk.Entry(win, width=19, textvariable = name_var)
name_entry_box.grid(row=0, column=1)
name_entry_box.focus()

age_var = tk.StringVar()
age_entry_box = ttk.Entry(win, width=19, textvariable=age_var)
age_entry_box.grid(row=1, column=1)

email_var = tk.StringVar()
email_entry_box = ttk.Entry(win, width=19, textvariable=email_var)
email_entry_box.grid(row=2, column=1)



# combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, width=16, state='readonly', textvariable=gender_var)
gender_combobox['value'] = ('Male', 'Female', 'others')
gender_combobox.current(0)
gender_combobox.grid(row=3, column=1)


# radiobutton
user_var = tk.StringVar()
user_radiobtn1 = ttk.Radiobutton(win, text="Student", value="Student", variable=user_var)
user_radiobtn1.grid(row=4, column=0)


user_radiobtn2 = ttk.Radiobutton(win, text="Teacher", value="Teacher", variable=user_var)
user_radiobtn2.grid(row=4, column=1)


# check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text="check if you want to subscribe our news letter.", variable=checkbtn_var)
checkbtn.grid(row=6, columnspan=3)


# def action():
#     username = name_var.get()
#     userage = age_var.get() 
#     user_email = email_var.get()
#     user_gender = gender_var.get()
#     user_type = user_var.get() 
#     user_check = checkbtn_var.get()
#     print(f"{username} {user_email} {userage} {user_gender} {user_type} {user_check}")

#     if user_check == 0:
#         messaged = "NO"
#     else: 
#         messaged = "YES" 

#     with open("file.txt", 'a') as f:
#         f.write(f"{username},{user_email},{userage},{user_gender},{user_type},{messaged}\n")

#     name_entry_box.delete(0, tk.END)
#     age_entry_box.delete(0, tk.END)
#     email_entry_box.delete(0, tk.END)


#write to csv file
def action():
    username = name_var.get()
    user_email = email_var.get()
    userage = age_var.get() 
    user_gender = gender_var.get()
    user_type = user_var.get() 
    user_check = checkbtn_var.get()

    if user_check == 0:
        messaged = "NO"
    else: 
        messaged = "YES" 

    with open("op_file.csv", 'a', newline="") as f:
        dict_writer = DictWriter(f, fieldnames=['Name', 'Email ID', 'Age', 'Gender', 'Profession', 'Subscribed'])
        if os.stat('op_file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Name' : username,
            'Email ID' : user_email,
            'Age' : userage,
            'Gender' : user_gender,
            'Profession' : user_type,
            'Subscribed' : messaged
        })




    name_entry_box.delete(0, tk.END)
    age_entry_box.delete(0, tk.END)
    email_entry_box.delete(0, tk.END)


# button
submit_btn = ttk.Button(win, width=12, text="Submit", command=action)
submit_btn.grid(row=7, column=0)

win.mainloop()