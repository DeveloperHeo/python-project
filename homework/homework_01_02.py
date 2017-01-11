class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

class Cowoker(Person):
    def __init__(self,name,age,gender,rank="대리"):
        super().__init__(name,age,gender)
        self.rank = rank

person = Person("동우","30","남자")
cowork = Cowoker("소현","26","여자","신입")

print(person.name)
print(cowork.name)
print(cowork.rank)

