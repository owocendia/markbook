import math
import pickle
import asyncio
#we don't do the 2023_2024 because its akward for input and processing
#turns out its becoming a 3D_array

class Database:
    data_order = {
        "student" :0,"T1_CA":1, "T1_FM":2, "T2_CA":3,"MA":4, "T2_FM":5, "FM":6, "Grade":7
    }

    def __init__(self, startyear : int, numyear:int):
        self.year = startyear
        for i in range(numyear):
            self.make_list(startyear+i)

    def update_list(self, a_list):
        with open('storage', 'wb') as fp:
            pickle.dump(a_list, fp)
            print('Done writing list into a binary file')
        with open('storage', 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

    def write_list(self, a_list):
        with open('storage', 'wb') as fp:
            pickle.dump(a_list, fp)
            print('Done writing list into a binary file')

    def read_list(self):
        with open('storage', 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

    def make_list(self, year): 
        database = self.read_list()
        try: database[year]
        except KeyError: 
            self.year = year
            database[year] = [["student", "T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"]]
            self.update_list(database) 
        else: pass

    def add_entry(self, name:str, year:int): #have year be defaulted as self.year if nothing valid is inputted
        database = self.read_list()
        if year != None:
            self.year = year
        if self.search(year, name) != -1:
            return -1
        else:
            #index starts from 1, 2, 3, 4, 5 for user convenience
            database[year].append([0 for i in range(6)])
            database[year][len(database[year])-1].insert(0, name)
            database[year][len(database[year])-1].insert(7, "N")
            self.update_list(database)
    def remove_entry(self, name:str, year:int): #have year be defaulted as self.year if nothing valid is inputted
        database = self.read_list()
        if year != None:
            self.year = year
        if self.search_index(year, name) == -1:
            return -1
        else:
            #index starts from 1, 2, 3, 4, 5 for user convenience
            del database[year][self.search_index(year, name)]
            self.update_list(database)
    def add_year(self, year:int): #have year be defaulted as self.year if nothing valid is inputted
        database = self.read_list()
        if year == len(database):
            self.make_list(1)
    def remove_year(self, year:int):
        database = self.read_list()
        try: database[year]
        except: return -1
        else: del database[year]
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
        database = self.read_list()
        return database[year]
    def return_student(self,year,student):
        database = self.read_list()
        return database[year][self.search(year, student)]
    def add_data(self, year,name, **kwargs):
        database = self.read_list()
        if year != None:
            self.year = year
        if name != None:
            self.name = name
        entry_chosen = database[year][self.search(year, name)]
        for keys, values in kwargs.items():
            entry_chosen[self/self.data_order[keys]] = values
        database[year][self.search(year, name)] = self.check_data(entry_chosen)
        print(database[year][self.search(year, name)])
        self.update_list(database)
    def replace_entry(self, year:int, name:str, data: list):
        database = self.read_list()
        for i in database[year]:
            if i[0] == name:
                database[year][database[year].index(i)][1:] = data
                self.check_data(database[year][database[year].index(i)])
        self.update_list(database)
    def search(self, year:int, name:str):
        database = self.read_list()
        for i in database[year]:
            if i[0] == name:
                return database[year][database[year].index(i)]
        return -1
    def search_index(self, year:int, name:str):
        database = self.read_list()
        for i in database[year]:
            if i[0] == name:
                return database[year].index(i)
        return -1
bro = Database(1, 4)
