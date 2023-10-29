from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
from database_lib import data
import playsound

playsound.playsound("music.mp3", block = False) # free music, totally not bribery
root = Tk() # creating the window and its size
root.geometry("1000x800")

db = data.Database('storage') # too lazy to write that every time
old = ""

def check_func(func, i):
    try:
        return func(i)
    except Exception as e:
        print(e)
        return None

def goback(): # resets the frame to go back to main menu
    omframe = optionsmenu()
    omframe.pack()

def get_storage(): # fetch the storage file
    with open('storage_space.txt', "r") as f:
        return [i[:-1]for i in f.readlines()]
    
def optionsmenu(): # main menu
    frame = Frame(root) # frames are screens inside the window that can be cleared

    canvas = Canvas(frame, width = 430, height = 450) # for the title
    canvas.create_text(200, 40, text = "Welcome to better SEQTA!", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    options = ("View Class", "Edit Student", "Add/Remove Student", "Add/Remove Class", "Settings", "Credits") # creating the listbox to select an option
    optionbox = Listbox(
        frame,
        listvariable = Variable(value = options),
        height = 6,
        selectmode = SINGLE
    )
    def selecteditem(): # check which option is selected
        selected = 0
        for i in optionbox.curselection():
            selected = optionbox.get(i)
            frame.pack_forget() # forget just clears the frame so a new one can be packed
            if selected == "View Class":
                vcframe = viewclass()
                vcframe.pack()
            elif selected == "Edit Student":
                vsframe = viewstudent()
                vsframe.pack()
            elif selected == "Add/Remove Student":
                asframe = addstudent()
                asframe.pack()
            elif selected == "Add/Remove Class":
                acframe = addclass()
                acframe.pack()
            elif selected == "Settings":
                setframe = settings()
                setframe.pack()
            elif selected == "Credits":
                creditframe = credit()
                creditframe.pack()
    
    optionbox.pack() # displays it
    
    btn = Button(frame, text = "Choose Option", command = selecteditem) # button to go to next screen
    btn.pack(side='bottom')

    return frame

def viewclass(): # view the table of classes
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 100) # for the title
    canvas.create_text(200, 40, text = "Viewing Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar() # a string variable for the selected dropdown option
    clicked.set(db.return_whole()[0])

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()]) # go back to main menu button
    back.pack(side = TOP)

    drop = ttk.Combobox(frame, textvariable = clicked, values = db.return_whole()) # the dropdown for the classes
    drop.pack(padx = 10, side = TOP)
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get()) # shows which dropdown option is currently selected
    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade") # header for each column
    tree = ttk.Treeview(frame, columns = cols, height = 26, show = "headings") # creating the actual table

    for i in cols: # put the column headers inside the table
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)
        
    tree.pack(padx = 50, side = BOTTOM, expand = 1)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    def update_tree(tree,label): # automatically update tree when the class is changed
        for item in tree.get_children():
            tree.delete(item)
        for i in db.return_year(clicked.get())[1:]:
            tree.insert("", END, values = i)
        label.config(text = clicked.get())
        frame.after(100, update_tree, tree, label)

    update_tree(tree,label)

    return frame

def viewstudent(): # edit data of students
    old = ""
    frame = Frame(root)
    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")

    canvas = Canvas(frame, width = 430, height = 100)
    canvas.create_text(200, 40, text = "Editing Student", font = ("Helvetica", "30", "bold"))
    canvas.pack(side = TOP)

    clicked = StringVar() # variable for class dropdown
    clicked.set(db.return_whole()[0])
    clicked2 = StringVar() # variable for student dropdown
    clicked2.set(db.return_year(clicked.get())[0][0])

    types = ["student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade"]
    drop = ttk.Combobox(frame, textvariable = clicked, values = db.return_whole()) # the dropdown to select a class
    drop.pack(padx = 20,side=LEFT)
    drop.configure(state = "readonly")

    old2 = clicked.get()
    drop_student = ttk.Combobox(frame, textvariable = clicked2, values = [i[0] for i in db.return_year(clicked.get())]) # the dropdown to select a student within that class
    drop_student.pack(padx = 50,side=LEFT)
    drop_student.configure(state = "readonly")

    label = Label(frame, text = clicked2.get()) # shows selected student
    label.pack(side = TOP)

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()]) # go back to main menu button
    back.pack(side = LEFT)

    text_box = Text(frame, height = 13, width = 40, wrap = 'word', font = ('Arial', 30, 'bold')) # textbox where data can be inputted/edited
    text_box.pack(expand=True)
    text_box.insert('end', "")

    def check_update(text_box, label, old, old2): # checks for any update in both of the dropdowns
        if clicked.get() != old2:
            print(old2)
            old2 = clicked.get()
            print(f"newest: {old2}")
            drop_student.configure(values = [i[0] for i in db.return_year(clicked.get())])
            drop_student.current(0)
            old = ""
        elif clicked2.get() != old:
            print(old)
            old = clicked2.get()
            print(f"new: {old}")
            text_box.delete(1.0, 'end')
            if clicked.get() != None and clicked2.get()[0] != "(":
                data = db.search(year = clicked.get(), name = clicked2.get())
                print(db.search(year = clicked.get(), name = clicked2.get()))
                message = ""
                for i in types[1:]:
                    message += i + ": " + str(data[types.index(i)])+"\n"
                text_box.insert('end', message)
                label.config(text = clicked2.get())   

        frame.after(100, check_update, text_box, label, old, old2)
        
    def update_stuff(): # updates the data in storage
        delimiters = [': ', "\n"]
        result = [text_box.get('1.0', 'end')]
        for delimiter in delimiters:
            temp_result = []
            for item in result:
                temp_result.extend(item.split(delimiter))
            result = temp_result
        temp_result = temp_result[1:-2:2]
        temp_result[:-1] = [check_func(int, i) for i in temp_result[:-1]]
        db.replace_entry(year = clicked.get(), name = clicked2.get(), data = temp_result)
        data = text_box.get(1.0, 'end').split("\n")
        text_box.delete(1.0, 'end')
        if clicked.get() != None and clicked2.get()[0] != "(":
            data = db.search(year = clicked.get(), name = clicked2.get())
            message = ""
            for i in types[1:]:
                message +=i + ": " + str(data[types.index(i)])+ "\n"
            text_box.insert('end', message)

    back = Button(frame, text = "Change", command = update_stuff) # button to apply changes
    back.pack()

    check_update(text_box, label, old, old2)

    return frame

def addstudent():
    frame = Frame(root) # here's another frame

    canvas = Canvas(frame, width = 430, height = 100) # title once again
    text = canvas.create_text(200, 40, text = "Add/Remove Student", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar() # another variable for class dropdown
    clicked.set(db.return_whole()[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = db.return_whole()) # you can probably guess what this is (the class dropdown)
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())
    cols = ["Student"]
    tree = ttk.Treeview(frame, columns = cols, height = 10, show = "headings")
    tree.heading('Student', text='Student')
    tree.column("Student", width = 300)

    def show(label, tree):
        label.config(text = clicked.get())
        for item in tree.get_children():
            tree.delete(item)
        if len(db.return_year(clicked.get())[1:]) > 0:
            for i in db.return_year(clicked.get())[1:]:
                tree.insert("", END, values = (i[0], ))
        frame.after(300, show, label, tree)

    label.pack()
    
    name = Label(frame, text = "Student Name: ").pack() # enter student's name
    nameent = Entry(frame)
    nameent.pack()

    added = Label(frame, text = nameent.get()) # shows what was added/removed
    added.pack()
    
    def confirm(added): # updates the text for the added/removed
        added.config(text = nameent.get())
        frame.after(100, confirm, added)

    enter = Button(frame, text = "Add Student", command = lambda:[db.add_entry(name = str(nameent.get()), year = clicked.get()), confirm(added)])
    enter.pack()
    enter2 = Button(frame, text = "Remove Student", command = lambda:[db.remove_entry(name = str(nameent.get()), year = clicked.get()), confirm(added)])
    enter2.pack()

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()]) # go back to main menu button
    back.pack(side = "bottom")

    tree.pack(padx = 50, side = BOTTOM, expand = 1)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    show(label, tree)

    return frame

def addclass():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 100)
    text = canvas.create_text(200, 40, text = "Add/Remove Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()
    
    name = Label(frame, text = "Class Name: ").pack()
    nameent = Entry(frame)
    nameent.pack()

    added = Label(frame, text = "")
    added.pack()

    clicked = StringVar()
    clicked.set(db.return_whole()[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = db.return_whole()) 
    drop.pack()
    drop.configure(state = "readonly")

    label = Label(frame, text = "")
    label.pack()
    add = Button(frame, text = "Add Class", command = lambda:[db.add_year(nameent.get()), added.config(text = "Added class " + nameent.get()), drop.configure(values = db.return_whole()), drop.set(db.return_whole()[0])])
    add.pack()
    remove = Button(frame, text = "Remove Class", command = lambda:[db.remove_year(clicked.get()), label.config(text = "Removed class " + clicked.get()), drop.configure(values = db.return_whole()), drop.set(db.return_whole()[0])])
    remove.pack()

    def show(tree):
        for item in tree.get_children():
            tree.delete(item)
        for key in db.return_whole():
            tree.insert("", END, values = (key,))
        frame.after(100, show, tree)

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = "bottom")

    tree = ttk.Treeview(frame, columns = ["Year"], height = 10, show = "headings")
    tree.heading('Year', text='Year')
    tree.column("Year", width = 200)
    tree.pack(padx = 50, side = BOTTOM, expand = 1)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    show(tree)

    return frame

def settings():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 100) # title
    text = canvas.create_text(200, 40, text = "Settings", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    name = Label(frame, text = "Save file name: ").pack() # name of the save file so you can have multiple
    nameent = Entry(frame)
    nameent.pack()

    def change(new):
        print("yay") # matthew likes to print random stuff in the console
        if new != "":
            db.file = new
            print("stuff happened")
            with open('storage_space.txt', 'a') as f:
                f.write(f'{new}\n')
            drop.configure(values=get_storage())
            print(db.file)

    make_new = Button(frame, text = "Make New Save File", command = lambda:[change(nameent.get())])
    make_new.pack()

    clicked = StringVar()
    clicked.set(get_storage()[0])

    drop = ttk.Combobox(frame, textvariable = clicked, values = get_storage())
    drop.pack(padx = 20,side=LEFT)
    drop.configure(state = "readonly")

    def object_creation():
        db.file_change(clicked.get())
    drop.pack()

    btn2 = Button(frame, text = "Choose File", command = object_creation)
    btn2.pack()

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = "bottom")

    return frame

def credit():
    pass

omframe = optionsmenu()
omframe.pack()
root.mainloop()
