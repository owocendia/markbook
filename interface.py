from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import library as database

root = Tk()
root.geometry("1000x800")
database.Database(0, 4)
classes = ("F3-CS", "F4-CS", "F5-CS", "F6-CS")

def goback():
    omframe = optionsmenu()
    omframe.pack()

def optionsmenu():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    canvas.create_text(200, 40, text = "Welcome to better SEQTA!", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    options = ("View Class", "View Student", "Edit Class", "Add New Student", "Settings")
    optionbox = Listbox(
        frame,
        listvariable = Variable(value = options),
        height = 6,
        selectmode = SINGLE
    )

    def selecteditem():
        selected = 0
        for i in optionbox.curselection():
            selected = optionbox.get(i)
            frame.pack_forget()
            if selected == "View Class":
                vcframe = viewclass()
                vcframe.pack()
            elif selected == "View Student":
                vsframe = viewstudent()
                vsframe.pack()
            elif selected == "Edit Class":
                ecframe = editclass()
                ecframe.pack()
            elif selected == "Add New Student":
                asframe = addstudent()
                asframe.pack()
            elif selected == "Settings":
                sframe = settings()
                sframe.pack()

    optionbox.pack()
    
    btn = Button(frame, text = "Choose Option", command = selecteditem)
    btn.pack(side='bottom')

    return frame

def viewclass():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 100)
    canvas.create_text(200, 40, text = "Viewing Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar()
    clicked.set(classes[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = classes) 
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())

    def show():
        label.config(text = clicked.get())
        
        for i in tree.get_children():
            tree.delete(i)
        for i in cols:
            tree.heading(i, text = i)
            tree.column(i, width = 100)
            tree.column("Student", width = 300)

        tree.pack()

        for i in database.Database.database[classes.index(clicked.get())][1:]:
            tree.insert("", END, values = i)
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()

    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    tree = ttk.Treeview(frame, columns = cols, height = len(cols), show = "headings")
    
    for i in cols:
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)

    tree.pack()

    for i in database.Database.database[classes.index(clicked.get())][1:]:
        tree.insert("", END, values = i)


    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = "bottom")

    return frame

def viewstudent():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    canvas.create_text(200, 40, text = "Viewing Student", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar()
    clicked.set(classes[0])

    clicked2 = StringVar()
    clicked2.set(database.Database.database[classes.index(clicked.get())][1])

    drop = ttk.Combobox(frame, textvariable = clicked, values = classes) 
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())

    drops = ttk.Combobox(frame, textvariable = clicked2, values = database.Database.database[classes.index(clicked.get())]) 
    drops.pack()
    drops.configure(state = "readonly")

    labels = Label(frame, text = clicked2.get())

    def show():
        label.config(text = clicked.get())
        
        for i in tree.get_children():
            tree.delete(i)
        for i in cols:
            tree.heading(i, text = i)
            tree.column(i, width = 100)
            tree.column("Student", width = 300)

        tree.pack()

        for i in database.Database.database[classes.index(clicked.get())][1:]:
            tree.insert("", END, values = i)
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()

    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    tree = ttk.Treeview(frame, columns = cols, height = len(cols), show = "headings")
    
    for i in cols:
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)

    tree.pack()

    for i in database.Database.database[classes.index(clicked.get())][1:]:
        tree.insert("", END, values = i)


    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack()

    return frame

def editclass():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    canvas.create_text(200, 40, text = "Editing Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar()
    clicked.set(classes[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = classes) 
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())

    def show():
        label.config(text = clicked.get())
        
        for i in tree.get_children():
            tree.delete(i)
        for i in cols:
            tree.heading(i, text = i)
            tree.column(i, width = 100)
            tree.column("Student", width = 300)

        tree.pack()

        for i in database.Database.database[classes.index(clicked.get())][1:]:
            tree.insert("", END, values = i)
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()

    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    tree = ttk.Treeview(frame, columns = cols, height = len(cols), show = "headings")
    
    for i in cols:
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)

    tree.pack()

    for i in database.Database.database[classes.index(clicked.get())][1:]:
        tree.insert("", END, values = i)

    

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack()

    return frame

def addstudent():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 100)
    text = canvas.create_text(200, 40, text = "Add a Student", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar()
    clicked.set(classes[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = classes) 
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())

    def show():
        label.config(text = clicked.get())
        
        for i in tree.get_children():
            tree.delete(i)
        for i in cols:
            tree.heading(i, text = i)
            tree.column(i, width = 100)
            tree.column("Student", width = 300)

        tree.pack()

        for i in database.Database.database[classes.index(clicked.get())][1:]:
            tree.insert("", END, values = i)
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()

    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    tree = ttk.Treeview(frame, columns = cols, height = len(cols), show = "headings")
    
    for i in cols:
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)

    tree.pack()

    for i in database.Database.database[classes.index(clicked.get())][1:]:
        tree.insert("", END, values = i)
    
    name = Label(frame, text = "Student Name: ").pack()
    nameent = Entry(frame).pack()

    t1ca = Label(frame, text = "T1-CA: ").pack()
    t1caent = Entry(frame).pack()

    t2ca = Label(frame, text = "T2-CA: ").pack()
    t2caent = Entry(frame).pack()

    ma = Label(frame, text = "MA: ").pack()
    maent = Entry(frame).pack()

    enter = Button(frame, text = "Add Student", command = database.Database.add_entry())

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = "bottom")

    return frame

def settings():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Settings", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    return frame

omframe = optionsmenu()
omframe.pack()
root.mainloop()
