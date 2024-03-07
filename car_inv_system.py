from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('sample.db')

def populate_list():
    car_list.delete(0, END)
    for row in db.fetch():
        car_list.insert(END, row)

def add_item():
    if cb_text.get() == '' or mn_text.get() == '' or bt_text.get() == '' or my_text.get() == '' or tr_text.get() == '' or mi_text.get() == '' or cs_text.get() == '':
        messagebox.showerror('Required Fields','One (or more) of the fields are missing. Please include all fields')
        return
    db.insert(cb_text.get(),mn_text.get(),bt_text.get(),my_text.get(),tr_text.get(),mi_text.get(),cs_text.get())
    car_list.delete(0, END)
    car_list.insert (END,(cb_text.get(),mn_text.get(),bt_text.get(),my_text.get(),tr_text.get(),mi_text.get(),cs_text.get()))
    populate_list()
    #print ('add item')

def select_item(event):
    global selected_item 
    index = car_list.curselection()[0]
    selected_item = car_list.get(index)
    cb_entry.delete(0,END)
    cb_entry.insert(END, selected_item[1])
    mn_entry.delete(0,END)
    mn_entry.insert(END, selected_item[2])
    bt_entry.delete(0,END)
    bt_entry.insert(END, selected_item[3])
    my_entry.delete(0,END)
    my_entry.insert(END, selected_item[4])
    tr_entry.delete(0,END)
    tr_entry.insert(END, selected_item[5])
    mi_entry.delete(0,END)
    mi_entry.insert(END, selected_item[6])
    cs_entry.delete(0,END)
    cs_entry.insert(END, selected_item[7])


def remove_item():
    db.remove(selected_item[1])
    populate_list()
    #print ('remove item')

def edit_item():
    print ('edit item')

def delete_item():
    print ('delete item')


# to create window object
app = Tk()

# to initialise label for car brand
cb_text = StringVar()
cb_label = Label(app, text= 'Car Brand', font= ('bold',14))
cb_label.grid(row=1,column=0,sticky=W)
cb_entry = Entry(app, textvariable=cb_text)
cb_entry.grid(row=1,column=1)

# to initialise label for model name
mn_text = StringVar()
mn_label = Label(app, text= 'Model Name', font= ('bold',14))
mn_label.grid(row=2,column=0,sticky=W)
mn_entry = Entry(app, textvariable=mn_text)
mn_entry.grid(row=2,column=1)

# to initialise label for body type
bt_text = StringVar()
bt_label = Label(app, text= 'Body Type', font= ('bold',14))
bt_label.grid(row=3,column=0,sticky=W)
bt_entry = Entry(app, textvariable=bt_text)
bt_entry.grid(row=3,column=1)

# to initialise label for manufacturing year
my_text = StringVar()
my_label = Label(app, text= 'Manufacturing Year', font= ('bold',14))
my_label.grid(row=1,column=2,sticky=W)
my_entry = Entry(app, textvariable=my_text)
my_entry.grid(row=1,column=3)

# to initialise label for transmission
tr_text = StringVar()
tr_label = Label(app, text= 'Transmission', font= ('bold',14))
tr_label.grid(row=2,column=2,sticky=W)
tr_entry = Entry(app, textvariable=tr_text)
tr_entry.grid(row=2,column=3)

# to initialise label for mileage
mi_text = StringVar()
mi_label = Label(app, text= 'Mileage', font= ('bold',14))
mi_label.grid(row=3,column=2,sticky=W)
mi_entry = Entry(app, textvariable=mi_text)
mi_entry.grid(row=3,column=3)

# to initialise label for car status
cs_text = StringVar()
cs_label = Label(app, text= 'Car Status', font= ('bold',14))
cs_label.grid(row=0,column=2,sticky=W)
cs_entry = Entry(app, textvariable=cs_text)
cs_entry.grid(row=0,column=3)

#to create inventory entry list
car_list = Listbox(app, height=8,width=60, border=0)
car_list.grid(row=5,column=1,columnspan=3,rowspan=6,pady=20,padx=20)

#to create scrollbar to the entry list
scrollbar = Scrollbar(app)
scrollbar.grid(row=5,column=4)
#set scrollbbar to listbox
car_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=car_list.yview)
# Bind select
car_list.bind('<<ListboxSelect>>',select_item)

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

populate_list()

# to start the program
app.mainloop()
