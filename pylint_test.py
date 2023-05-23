class myperson:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age

    def GetName(self):
        self.AskedForm = True
        return self.name


print(myperson('Cami', 27, 'F'))
