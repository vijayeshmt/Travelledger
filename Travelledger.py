""""
This code is created by Vijayesh M T
Code contains simole GUI for a small travel company

"""
from tkinter import *


def getvals():
	a = namevalue.get()
	b = phonevalue.get()
	c = gendervalue.get()
	d = paymentvalue.get()
	e = foodservicevalue.get()

	print("submitting form")
	with open("records.txt", "a") as f:
		f.write(str(a) + "\n" + str(b) + "\n" + str(c) + "\n" + str(d) + "\n" + str(e) + "\n\n")


root = Tk()
root.geometry("700x350")
root.title("Travel services")
# heading
Label(root, text="Vijayesh Travels", font=("comicsansms", 9, "bold"), pady=15).grid(row=0, column=3)

# parameters
name = Label(root, text="Name", padx=5)
name.grid(row=1)

phone = Label(root, text="Phone no", padx=5)
phone.grid(row=2)
gender = Label(root, text="Gender", padx=5)
gender.grid(row=3)
payment = Label(root, text="Paymeny mode", padx=5)
payment.grid(row=4)

# entries

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
paymententry = Entry(root, textvariable=paymentvalue)

# packing entries

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
paymententry.grid(row=4, column=3)
# foodserviceentry.grid(row=,column=3)


# checkbox
foodservice = Checkbutton(text="Want to prebook your meals", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)

root.mainloop()
