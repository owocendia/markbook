import math

#we don't do the 2023_2024 because its akward for input and processing
#turns out its becoming a 3D_array

class Database:
    database = {
        0: [["student","T1_CA", "T1_FM", "T2_CA","MA", "T2_FM", "FM", "Grade"],
            ["Matthew",0,0,0,0,0,0,0]]
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

    def add_entry(self, name, year = None): #have year be defaulted as self.year if nothing valid is inputted
        if year != None:
            self.year = year
        if self.search(year, name) == -1:
            return -1
        else:
            #index starts from 1, 2, 3, 4, 5 for user convenience
            self.database[year].append([None for i in range(7)])
            self.database[year][len(self.database[year])-1].insert(0, name)


    def check_data(self, entry_chosen):
        if entry_chosen[1] != None:
            entry_chosen[2] = entry_chosen[1]
        if entry_chosen[3] != None and entry_chosen[4] != None:
            entry_chosen[5] = entry_chosen[3] * 60/100 + entry_chosen[4] * 40/100
        if (entry_chosen[2] != None) and (entry_chosen[5] != None):
            entry_chosen[6] = (entry_chosen[2]+ entry_chosen[5])/2
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
    
    def add_data(self, year,name, **kwargs):
        if year != None:
            self.year = year
        if name != None:
            self.name = name
        entry_chosen = self.database[year][self.search(year, name)]
        for keys, values in kwargs.items():
            entry_chosen[self/self.data_order[keys]] = values
        self.database[year][self.search(year, name)] = self.check_data(entry_chosen)

    def search(self, year, name):
        for i in self.database[year]:
            if i[0] == name:
                return self.database[year].index(i)
        return -1