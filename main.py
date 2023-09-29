
import math
import random
from tabulate import tabulate
#we don't do the 2023_2024 because its akward for input and processing
#turns out its becoming a 3D_array


database = {
    0: [["student","T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"],
          ["Matthew",0,0,0,0,0,0,0]]
}

data_order = {
    "student" :0,"T1_CA":1, "T1_FM":2, "T2_CA":3,"MA":4, "T2_FM":5, "FM":6, "Grade":7
}

def make_list(year):
    database[year] = [["student","T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"]]


def add_entry(year, name):
    #index starts from 1, 2, 3, 4, 5 for user convenience
    database[year].append([None for i in range(7)])
    database[year][len(database[year])-1].insert(0, name)

def check_data(student_entry):
    if student_entry[1] != None:
        student_entry[2] = student_entry[1]
    if student_entry[3] != None and student_entry[4] != None:
        student_entry[5] = student_entry[3] * 60/100 + student_entry[4] * 40/100
    if (student_entry[2] != None) and (student_entry[5] != None):
        student_entry[6] = (student_entry[2]+ student_entry[5])/2
    if student_entry[6] != None:
        match math.ceil(int(student_entry[6]/10)):
            case 1:
                student_entry[7] = "E"
            case 2:
                student_entry[7] = "E"
            case 3:
                student_entry[7] = "E"
            case 4:
                student_entry[7] = "E"
            case 5:
                student_entry[7] = "D"
            case 6:
                student_entry[7] = "C"
            case 7:
                student_entry[7] = "B"
            case 8:
                student_entry[7] = "A"
            case 9:
                student_entry[7] = "A*"
            case 10:
                student_entry[7] = "A**"
    return student_entry
    
def add_data(year,name, **kwargs):
    student_entry = database[year][search(year, name)]
    for keys, values in kwargs.items():
        student_entry[data_order[keys]] = values
    database[year][search(year, name)] = check_data(student_entry)

def search(year, name):
    for i in database[year]:
        if i[0] == name:
            return database[year].index(i)
def show_data(year):
    print(tabulate(database[year]))

if __name__ == "__main__":
    make_list(int(input("please input starting year: ")))
    print(database)
    while True:
        bro = input("select options \n1. new year \n2. new student\n3. new data\n4. table up ")
        match bro:
            case "1":
                make_list(int(input("input new year: ")))
            case "2":
                add_entry(int(input("input year: ")), input("input new student: "))
            case "3":
                add_data(int(input("input year: ")), input("input new student: "), T1_CA=int(input("T1CA? ")), T2_CA=int(input("T2CA? ")), MA=int(input("MA? ")))
            case "4":
                show_data(int(input("input year: ")))