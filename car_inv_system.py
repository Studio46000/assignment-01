from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('inventory.db')
#insert entries to listbox
def populate_list():
    car_list.delete(0, END)
    for row in db.fetch():
        car_list.insert(END, row)

# add entry function
def add_item():
    #catch mileage error
    try:
        mileage = int(mi_text.get())
    except ValueError:
        messagebox.showerror('Invalid Input',"Mileage must be an integer")
        return
    #catch manufacturing year error
    manufacturing_year =my_text.get()
    if not manufacturing_year.isdigit() or len(manufacturing_year) != 4:
        messagebox.showerror('Invalid Input','Manufacturing Year must be a four digit number')
        return
    #catch missing field inputs error
    if cb_text.get() == '' or mn_text.get() == '' or bt_text.get() == '' or my_text.get() == '' or tr_text.get() == '' or mi_text.get() == '':
        messagebox.showerror('Required Fields','One (or more) of the fields are missing. Please include all fields')
        return
    db.insert(cb_text.get(),mn_text.get(),bt_text.get(),manufacturing_year,tr_text.get(),str(mileage))
    car_list.delete(0, END)
    car_list.insert (END,(cb_text.get(),mn_text.get(),bt_text.get(),manufacturing_year,tr_text.get(),str(mileage)))
    clear_text()
    populate_list()

    messagebox.showinfo('Success','Car added successfully!')


# define action when selecting items
def select_item(event):
    try:
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
    except IndexError:
        pass


# remove button
def remove_item():
    db.remove(selected_item[0])
    populate_list()
    clear_text()

    messagebox.showinfo('Success','Car has been removed successfully!')
#edit button
def edit_item():
    try:
        mileage = int(mi_text.get())
    except ValueError:
        messagebox.showerror('Invalid Input',"Mileage must be an integer")
        return
    manufacturing_year =my_text.get()
    if not manufacturing_year.isdigit() or len(manufacturing_year) != 4:
        messagebox.showerror('Invalid Input','Manufacturing Year must be a four digit number')
        return
    db.update(selected_item[0], cb_text.get(),mn_text.get(),bt_text.get(),manufacturing_year,tr_text.get(),str(mileage))
    populate_list()

    messagebox.showinfo('Success','Car details has been edited successfully!')
#clear text
def clear_text():
    cb_entry.delete(0,END)
    mn_entry.delete(0,END)
    bt_entry.delete(0,END)
    my_entry.delete(0,END)
    tr_entry.delete(0,END)
    mi_entry.delete(0,END)



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


#to create inventory entry list
car_list = Listbox(app, height=8,width=60, border=0)
car_list.grid(row=5, column=1, columnspan=3, rowspan=6, pady=20,padx=(20,0),sticky="nsew")

#to create scrollbar to the entry list
scrollbar = Scrollbar(app)
scrollbar.grid(row=5,column=4,rowspan=6,pady=20, padx=(0,20),sticky="ns")

#set scrollbbar to listbox
car_list.configure(yscrollcommand= scrollbar.set)
scrollbar.configure(command= car_list.yview)

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

#Clear Entry Button
clear_btn = Button(app,text= 'Clear Entry', width= 12, command= clear_text)
clear_btn.grid(row=4,column=3)


app.title ('Car Inventory System')
app.geometry ('750x400')

populate_list()

# to start the program
app.mainloop()
