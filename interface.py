from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import re

import math

#we don't do the 2023_2024 because its akward for input and processing
#turns out its becoming a 3D_array

class Database:
    database = {
        0: [["student","T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"],
            ["Matthew",0,0,0,0,0,0,"N"],["Matthew2",0,0,0,0,0,0,"N"],["Matthew3",0,0,0,0,0,0,"N"],["Matthew4",0,0,0,0,0,0,"N"]]
    }
    data_order = {
        "student" :0,"T1_CA":1, "T1_FM":2, "T2_CA":3,"MA":4, "T2_FM":5, "FM":6, "Grade":7
    }
    def __init__(self, startyear : int, numyear:int):
        self.year = startyear
        for i in range(numyear):
            self.make_list(startyear+i)

    def make_list(self, year): 
        try: self.database[year]
        except KeyError: 
            self.year = year
            self.database[year] = [["student","T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"]]
        else: pass

    def add_entry(self, name:str, year:int): #have year be defaulted as self.year if nothing valid is inputted
        if year != None:
            self.year = year
        if self.search(year, name) != -1:
            return -1
        else:
            #index starts from 1, 2, 3, 4, 5 for user convenience
            self.database[year].append([None for i in range(6)])
            self.database[year][len(self.database[year])-1].insert(0, name)
            self.database[year][len(self.database[year])-1].insert(-1, "N")
            print("success")


    def check_data(self, entry_chosen):
        if entry_chosen[1] != None:
            entry_chosen[2] = entry_chosen[1]
        if entry_chosen[3] != None and entry_chosen[4] != None:
            entry_chosen[5] = int(entry_chosen[3] * 60/100 + entry_chosen[4] * 40/100)
        if (entry_chosen[2] != None) and (entry_chosen[5] != None):
            entry_chosen[6] = int((entry_chosen[2]+ entry_chosen[5])/2)
        if entry_chosen[6] != None:
            match math.ceil(int(entry_chosen[6]/10)):
                case 1:
                    entry_chosen[7] = "E"
                case 2:
                    entry_chosen[7] = "E"
                case 3:
                    entry_chosen[7] = "E"
                case 4:
                    entry_chosen[7] = "E"
                case 5:
                    entry_chosen[7] = "D"
                case 6:
                    entry_chosen[7] = "C"
                case 7:
                    entry_chosen[7] = "B"
                case 8:
                    entry_chosen[7] = "A"
                case 9:
                    entry_chosen[7] = "A*"
                case 10:
                    entry_chosen[7] = "A**"
        return entry_chosen
    def return_year(self, year):
        return self.database[year]
    def return_student(self,year,student):
        return self.database[year][self.search(year, student)]
    def add_data(self, year,name, **kwargs):
        if year != None:
            self.year = year
        if name != None:
            self.name = name
        entry_chosen = self.database[year][self.search(year, name)]
        for keys, values in kwargs.items():
            entry_chosen[self/self.data_order[keys]] = values
        self.database[year][self.search(year, name)] = self.check_data(entry_chosen)
    def replace_entry(self, year:int, name:str, data: list):
        for i in self.database[year]:
            if i[0] == name:
                self.database[year][self.database[year].index(i)][1:] = data
                self.check_data(self.database[year][self.database[year].index(i)])
    def search(self, year:int, name:str):
        for i in self.database[year]:
            if i[0] == name:
                return self.database[year][self.database[year].index(i)]
        return -1
    

root = Tk()
root.geometry("1000x800")
bro = Database(0, 4)
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

    options = ("View Class", "View Student", "Add New Student")
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
    canvas.create_text(200, 40, text = "Viewing Student", font = ("Helvetica", "30", "bold"))
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


omframe = optionsmenu()
omframe.pack()
root.mainloop()
