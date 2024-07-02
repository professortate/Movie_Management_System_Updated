from tkinter import *
from tkinter import messagebox
from MiniProject_Backend import *

def get_selected_row(event):
    global selected_tuple
    if list1.curselection():
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[0])  # Movie_ID
        e2.delete(0, END)
        e2.insert(END, selected_tuple[1])  # Movie_Name
        e3.delete(0, END)
        e3.insert(END, selected_tuple[2])  # Release_Date
        e4.delete(0, END)
        e4.insert(END, selected_tuple[3])  # Director_Name
        e5.delete(0, END)
        e5.insert(END, selected_tuple[4])  # Casts
        e6.delete(0, END)
        e6.insert(END, selected_tuple[5])  # Budget
        e7.delete(0, END)
        e7.insert(END, selected_tuple[6])  # Duration
        e8.delete(0, END)
        e8.insert(END, selected_tuple[7])  # Rating

def view_command():
    list1.delete(0, END)
    for row in ViewMovieData():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    print(f"Search parameters - Movie_ID: {Movie_ID_text.get()}, Movie_Name: {Movie_Name_text.get()}")
    for row in SearchMovieData(Movie_ID_text.get(), Movie_Name_text.get()):
        list1.insert(END, row)

def add_command():
    AddMovieRec(Movie_ID_text.get(), Movie_Name_text.get(), Release_Date_text.get(), Director_text.get(), Cast_text.get(), Budget_text.get(), Duration_text.get(), Rating_text.get())
    list1.delete(0, END)
    list1.insert(END, (Movie_ID_text.get(), Movie_Name_text.get(), Release_Date_text.get(), Director_text.get(), Cast_text.get(), Budget_text.get(), Duration_text.get(), Rating_text.get()))

def delete_command():
    if 'selected_tuple' in globals():
        DeleteMovieRec(selected_tuple[0])
        view_command()

def update_command():
    if 'selected_tuple' in globals():
        UpdateMovieData(selected_tuple[0], Movie_ID_text.get(), Movie_Name_text.get(), Release_Date_text.get(), Director_text.get(), Cast_text.get(), Budget_text.get(), Duration_text.get(), Rating_text.get())
        view_command()

def close_command():
    window.destroy()

window = Tk()
window.wm_title("Movie Store")

l1 = Label(window, text="Movie ID")
l1.grid(row=0, column=0)

l2 = Label(window, text="Movie Name")
l2.grid(row=0, column=2)

l3 = Label(window, text="Release Date")
l3.grid(row=1, column=0)

l4 = Label(window, text="Director")
l4.grid(row=1, column=2)

l5 = Label(window, text="Cast")
l5.grid(row=2, column=0)

l6 = Label(window, text="Budget")
l6.grid(row=2, column=2)

l7 = Label(window, text="Duration")
l7.grid(row=3, column=0)

l8 = Label(window, text="Rating")
l8.grid(row=3, column=2)

Movie_ID_text = StringVar()
e1 = Entry(window, textvariable=Movie_ID_text)
e1.grid(row=0, column=1)

Movie_Name_text = StringVar()
e2 = Entry(window, textvariable=Movie_Name_text)
e2.grid(row=0, column=3)

Release_Date_text = StringVar()
e3 = Entry(window, textvariable=Release_Date_text)
e3.grid(row=1, column=1)

Director_text = StringVar()
e4 = Entry(window, textvariable=Director_text)
e4.grid(row=1, column=3)

Cast_text = StringVar()
e5 = Entry(window, textvariable=Cast_text)
e5.grid(row=2, column=1)

Budget_text = StringVar()
e6 = Entry(window, textvariable=Budget_text)
e6.grid(row=2, column=3)

Duration_text = StringVar()
e7 = Entry(window, textvariable=Duration_text)
e7.grid(row=3, column=1)

Rating_text = StringVar()
e8 = Entry(window, textvariable=Rating_text)
e8.grid(row=3, column=3)

list1 = Listbox(window, height=8, width=50)
list1.grid(row=4, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=4, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=4, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=5, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=6, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=7, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=8, column=3)

b6 = Button(window, text="Close", width=12, command=close_command)
b6.grid(row=9, column=3)

window.mainloop()
