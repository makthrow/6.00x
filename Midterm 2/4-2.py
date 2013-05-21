class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        if self.idNum == other.idNum:
            return self.name < other.name
        return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)

