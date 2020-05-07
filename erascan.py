import tkinter as tk
from tkinter import *
from tkinter import ttk
win = tk.Tk()
win.geometry("800x800")
win.title("RC/DL STATUS")
label1 = Label(win,text = "Home",bd=1,relief="solid",fg="white",font="Times 14",padx=800,pady=10,bg="#337ab7")
label = Label(win,text="",pady=10)
label2 = Label(win,text = "Know your DL status",bd=1,relief="solid",font="Times 18",padx=450,pady=10,bg="#94c6e0")


label1.pack()
label.pack()
label2.pack()

label_frame = ttk.Labelframe(win)
label_frame.pack(fill='both',padx=20,pady=20)

# Driving licence
Dlic = tk.Label(label_frame,text='Driving Licence no. :',font='arial 10 bold',bg='light blue')
Dlic.pack()

Dlic_enterybox = ttk.Entry(label_frame,font=('arial',10,'bold'),background="powder blue",justify='left')
Dlic_enterybox.focus_set()
Dlic_enterybox.pack(pady=30)

# entry dob
DOB = tk.Label(label_frame,text='Date of Birth: ',font='arial 10 bold',bg='light blue')
DOB.pack()

DOB_enterybox = tk.Entry(label_frame,font=('arial',10,'bold'),background="powder blue",justify='left')
DOB_enterybox.pack(pady = 30)


# verification code
vercode = tk.Label(label_frame,text='Enter Verification Code: ',font='arial 10 bold',bg='light blue')
vercode.pack()

vercode_enterybox = tk.Entry(label_frame,font=('arial',10,'bold'),background="powder blue",justify='left')
vercode_enterybox.pack(pady = 30)

# create button

login_button= tk.Button(label_frame,text='Check status',command=next,activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',12,'bold'),relief='sunken')
login_button.pack(padx=20,pady=20)

login_button= tk.Button(label_frame,text='Reset',command=next,activebackground='red',bd=5,activeforeground='yellow',bg='powder blue', width=15,font=('arial',12,'bold'),relief='sunken')
login_button.pack(padx=20,pady=20)

note= tk.Label(label_frame,text="Driving Licence number can be entered in any of the following formats: DL-1420110012345 or DL14 20110012345\n " \
       "Total number of input characters should be exactly 16 (including space or '-').\nIf you hold an old driving " \
       "license with a different format, please convert the format as per below rule before " \
       "entering.\nSS-RRYYYYNNNNNNN OR SSRR YYYYNNNNNNN\nWhere\nSS - Two character State Code (like RJ for Rajasthan, " \
       "TN for Tamil Nadu etc)\nRR - Two digit RTO Code\nYYYY - 4-digit Year of Issue (For Example: If year is " \
       "mentioned in 2 digits, say 99, then it should be converted to 1999. Similarly use 2012 for 12).\nRest of the " \
       "numbers are to be given in 7 digits. If there are less number of digits, then additional 0's(zeros) may be " \
       "added to make the total 7.\nFor example: If the Driving Licence Number is RJ-13/DLC/12/ 123456 then please " \
       "enter RJ-1320120123456 OR RJ13 20120123456. ",fg="red",padx=600)
note.pack()




win.mainloop()