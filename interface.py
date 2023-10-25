from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import library as database
import re

root = Tk()
root.geometry("1000x800")
bro = database.Database(0, 4)
classes = ("F3-CS", "F4-CS", "F5-CS", "F6-CS")
old = ""
def goback():
    omframe = optionsmenu()
    omframe.pack()

def optionsmenu():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    canvas.create_text(200, 40, text = "Welcome to better SEQTA!", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    options = ("View Class", "Edit Student", "Add New Student")
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
            elif selected == "Edit Student":
                vsframe = viewstudent()
                vsframe.pack()
            elif selected == "Add New Student":
                asframe = addstudent()
                asframe.pack()

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
    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side =TOP)
    drop = ttk.Combobox(frame, textvariable = clicked, values = classes) 
    drop.pack(padx = 10, side = TOP)
    drop.configure(state = "readonly")

    label = Label(frame, text = clicked.get())
    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    tree = ttk.Treeview(frame,columns = cols, height = 26, show = "headings")
    for i in cols:
        tree.heading(i, text = i)
        tree.column(i, width = 100)
        tree.column("Student", width = 300)
        
    tree.pack(padx = 50, side = BOTTOM, expand = 1)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    #scrollbar.pack(side="right", fill="y")
    def update_tree(tree):
        label.config(text = clicked.get())
        for item in tree.get_children():
            tree.delete(item)
        for i in bro.database[classes.index(clicked.get())][1:]:
            tree.insert("", END, values = i)
        frame.after(100, update_tree, tree)
        frame.after(100, update_tree, label)


    update_tree(tree)

    return frame

def viewstudent():
    global old
    frame = Frame(root)
    cols = ("Student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade")
    canvas = Canvas(frame, width = 430, height = 100)
    canvas.create_text(200, 40, text = "Editing Student", font = ("Helvetica", "30", "bold"))
    canvas.pack(side = TOP)
    clicked = StringVar()
    clicked.set(classes[0])
    clicked2 = StringVar()
    clicked2.set(bro.database[classes.index(clicked.get())][1])
    types = ["student", "T1-CA", "T1-FM", "T2-CA","MA", "T2-FM", "FM", "Grade"]
    drop = ttk.Combobox(frame, textvariable = clicked, values = classes)
    drop.pack(padx = 20,side=LEFT)
    drop.configure(state = "readonly")

    #label = Label(frame, text = clicked.get())

    drop_student = ttk.Combobox(frame, textvariable = clicked2, values = [i[0] for i in bro.database[classes.index(clicked.get())]])
    drop_student.pack(padx = 50,side=LEFT)
    drop_student.configure(state = "readonly")
    label = Label(frame, text = clicked2.get())
    label.pack(side = TOP)
    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = LEFT)
    text_box = Text(frame,height=13,width=40,wrap='word',font= ('Arial', 30, 'bold'))
    text_box.pack(expand=True)
    text_box.insert('end', "")

    def check_update(text_box, label):
        global old
        if clicked2.get() != old:
            old = clicked2.get()
            text_box.delete(1.0, 'end')
            if clicked.get() != None and clicked2.get()[0] != "(":
                data = bro.search(year = classes.index(clicked.get()), name = clicked2.get())
                message = ""
                for i in types[1:]:
                    message += i + ": " + str(data[types.index(i)])+"\n"
                text_box.insert('end', message)
                label.config(text = clicked2.get())   

        frame.after(100, check_update, text_box, label)
    def update_stuff():
        delimiters = [': ', "\n"]
        result = [text_box.get('1.0', 'end')]
        for delimiter in delimiters:
            temp_result = []
            for item in result:
                temp_result.extend(item.split(delimiter))
            result = temp_result
        temp_result = temp_result[1:-2:2]
        temp_result = [int(i) if temp_result[-1] != i else i for i in temp_result]
        bro.replace_entry(year = classes.index(clicked.get()), name = clicked2.get(), data = temp_result)
        data = text_box.get(1.0, 'end').split("\n")
        text_box.delete(1.0, 'end')
        if clicked.get() != None and clicked2.get()[0] != "(":
            data = bro.search(year = classes.index(clicked.get()), name = clicked2.get())
            message = ""
            for i in types[1:]:
                message +=i + ": " + str(data[types.index(i)])+ "\n"
            text_box.insert('end', message)
    back = Button(frame, text = "Change", command = update_stuff)
    back.pack()

    check_update(text_box, label)

    return frame

def editclass():
    global classes
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

        for i in bro.database[classes.index(clicked.get())][1:]:
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

    for i in bro.database[classes.index(clicked.get())][1:]:
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

    def show(label):
        label.config(text = clicked.get())
        frame.after(100, show, label)
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()
    
    name = Label(frame, text = "Student Name: ").pack()
    nameent = Entry(frame)
    nameent.pack()

    added = Label(frame, text = nameent.get())
    added.pack()

    def confirm(added):
        added.config(text = nameent.get())
        frame.after(100, confirm, added)

    enter = Button(frame, text = "Add Student", command = lambda:[bro.add_entry(name = str(nameent.get()), year = classes.index(clicked.get())), confirm(added), print(bro.search(classes.index(clicked.get()), str(nameent.get())))])
    enter.pack()

    back = Button(frame, text = "Go Back", command = lambda:[frame.pack_forget(), goback()])
    back.pack(side = "bottom")
    show(label)
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
