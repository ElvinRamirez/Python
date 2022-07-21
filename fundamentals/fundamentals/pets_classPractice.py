class Pet:
    def __init__(self, name,breed,gender,age,owner):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.owner = owner
    def printPet(self):
        print(f"{self.name}, is a {self.gender} {self.breed}, and is owned by {self.owner}.")

    def agePrediction(self,newYear,currYear):
        new_age=self.age + newYear % currYear
        print(f"{self.name} will be", new_age, "in", newYear)


mango = Pet('Mango','Siamese', 'Female',2, 'Elvin')
elliot = Pet('Elliot','Bengal','Male',2,'Masha')

mango.printPet()
mango.agePrediction(2025,2022)
elliot.agePrediction(2032,2022)

