from tkinter import *

# to create window object
app = Tk()

# to initialise label for serial number
sn_text = IntVar()
sn_text = 1001
sn_label = Label(app, text= 'Serial Number', font=('bold',14),pady=20)
sn_label.grid(row=0, column=0, sticky=W)
sn_number = Label(app,text= sn_text, font=(15),pady=20)
sn_number.grid(row=0,column=1)

# to initialise label for car brand
cb_text = StringVar()
cb_label = Label(app, text= 'Car Brand', font= ('bold',14))
cb_label.grid(row=1,column=0,sticky=W)
cb_label = Entry(app, textvariable=cb_text)
cb_label.grid(row=1,column=1)

# to initialise label for model name
mn_text = StringVar()
mn_label = Label(app, text= 'Model Name', font= ('bold',14))
mn_label.grid(row=2,column=0,sticky=W)
mn_label = Entry(app, textvariable=mn_text)
mn_label.grid(row=2,column=1)

# to initialise label for body type
bt_text = StringVar()
bt_label = Label(app, text= 'Body Type', font= ('bold',14))
bt_label.grid(row=3,column=0,sticky=W)
bt_label = Entry(app, textvariable=bt_text)
bt_label.grid(row=3,column=1)

# to initialise label for manufacturing year
my_text = StringVar()
my_label = Label(app, text= 'Manufacturing Year', font= ('bold',14))
my_label.grid(row=1,column=2,sticky=W)
my_label = Entry(app, textvariable=my_text)
my_label.grid(row=1,column=3)

# to initialise label for transmission
tr_text = StringVar()
tr_label = Label(app, text= 'Transmission', font= ('bold',14))
tr_label.grid(row=2,column=2,sticky=W)
tr_label = Entry(app, textvariable=tr_text)
tr_label.grid(row=2,column=3)

# to initialise label for mileage
mi_text = StringVar()
mi_label = Label(app, text= 'Mileage', font= ('bold',14))
mi_label.grid(row=3,column=2,sticky=W)
mi_label = Entry(app, textvariable=mi_text)
mi_label.grid(row=3,column=3)

# to initialise label for car status
cs_text = StringVar()
cs_label = Label(app, text= 'Car Status', font= ('bold',14))
cs_label.grid(row=0,column=2,sticky=W)
cs_label = Entry(app, textvariable=my_text)
cs_label.grid(row=0,column=3)

#to create inventory entry list
car_list = Listbox(app, height=8,width=60, border=0)
car_list.grid(row=5,column=1,columnspan=3,rowspan=6,pady=20,padx=20)

#to create scrollbar to the entry list
scrollbar = Scrollbar(app)
scrollbar.grid(row=5,column=4)
car_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=car_list.yview)

#Add Car Button
add_btn = Button(app,text= 'Add Car', width= 12, command= add_item)
add_btn.grid(row=4,column=0, pady=20)

#remove Car Button
remove_btn = Button(app,text= 'Remove Car', width= 12, command= remove_item)
remove_btn.grid(row=4,column=1)

#Edit Car Button
edit_btn = Button(app,text= 'Edit Car', width= 12, command= edit_item)
edit_btn.grid(row=4,column=2)

#Delete Car Button
delete_btn = Button(app,text= 'Delete Car', width= 12, command= delete_item)
delete_btn.grid(row=4,column=3)


app.title ('Car Inventory System')
app.geometry ('900x900')

# to start the program
app.mainloop()
