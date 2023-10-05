from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import data

root = Tk()
root.geometry("1000x800")

classes = ("F3-CS", "F4-CS", "F5-CS", "F6-CS")

def optionsmenu():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Welcome to better SEQTA!", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    options = ("View Class", "View Student", "Edit Class", "Add New Student", "Settings")
    optionbox = Listbox(
        frame,
        listvariable = Variable(value = options),
        height = 6,
        selectmode = SINGLE
    )

    def selected_item():
        for i in optionbox.curselection():
            selected = optionbox.get(i)
            print(selected)
            omframe.destroy()
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
    
    btn = Button(frame, text = "Choose Option", command = selected_item)
    
    btn.pack(side='bottom')
    optionbox.pack()
    return frame

def viewclass():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Viewing Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    clicked = StringVar()
    clicked.set("F3-CS")

    drop = OptionMenu(frame, clicked, *classes) 
    drop.pack()

    label = Label(frame, text = "F3-CS")

    def show():
        label.config(text = clicked.get())
  
    btn = Button(frame, text = "Select", command = show)
    btn.pack()
    label.pack()

    cols = ("student", "T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade")
    
    tree = ttk.Treeview(frame, columns = cols, height = 8, show = "headings")
    tree.heading("student", text = "Student Name")
    tree.heading("T1_CA", text = "T1-CA")
    tree.heading("T1_FM", text = "T1-FM")
    tree.heading("T2_CA", text = "T2-CA")
    tree.heading("MA", text = "MA")
    tree.heading("T2_FM", text = "T2-FM")
    tree.heading("FM", text = "FM")
    tree.heading("Grade", text = "Grade")

    for i in data.database[drop.index(classes)]:
        tree.insert("", tk.END, values = data.database[drop.index(classes)])

    tree.pack()

    return frame

def viewstudent():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Viewing Student", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    return frame

def editclass():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Editing Class", font = ("Helvetica", "30", "bold"))
    canvas.pack()

    return frame

def addstudent():
    frame = Frame(root)

    canvas = Canvas(frame, width = 430, height = 450)
    text = canvas.create_text(200, 40, text = "Add a Student", font = ("Helvetica", "30", "bold"))
    canvas.pack()

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
