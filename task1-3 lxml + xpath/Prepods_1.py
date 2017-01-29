class Prepod:
    Name = ''
    Subname = ''
    Lastname = ''
    Tel = ''
    Address = ''
    Doljn = ''
    Email = ''

    def __init__(self, name, subname, lastname, tel, address, doljn, email):
        self.Name = name
        self.Subname = subname
        self.Lastname = lastname
        self.Tel = tel
        self.Address = address
        self.Doljn = doljn
        self.Email = email

    def saveToFile(self, outfile):
        outfile.write(self.Name + ';' + self.Subname + ';' + self.Lastname + ';' + self.Tel + ';' + self.Address + ';' + self.Doljn + ';' + self.Email + '\n')

    def readFromFile(self, line):
        L = line.split(";")
        self.Name = L[0]
        self.Subname = L[1]
        self.Lastname = L[2]
        self.Tel = L[3]
        self.Address = L[4]
        self.Doljn = L[5]
        self.Email = L[6]

    def printPrepod(self):
        print(str(self))

    def __str__(self):
        return str(self.Name) + ' ' + str(self.Subname) + ' ' + str(self.Lastname) + ' ' + str(self.Tel) + ' ' + str(self.Address) + ' ' + str(self.Doljn) + ' ' + str(self.Email)

#чтобы при импорте этот код не выполнялся
if __name__ == '__main__':
    f = open('Prepods_1.txt', 'r')
    for line in f:
        P1 = Prepod("", "", "", "", "", "", "")
        P1.readFromFile(line)
        P1.printPrepod()

    f.close()

'''
P1 = Prepod("Vasya", "Petrovish", "Petin", "88005553535", "street N", "ml_sotrudnik", "vasyaPP@gmail.ru")
f = open('Prepods_1.txt', 'w')
P1.saveToFile(f)
f.close()
'''
