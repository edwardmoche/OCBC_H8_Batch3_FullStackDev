
def nama_fungsi ( parameter ):
    pass

class Dog:
    # pass

    # ini dua2nya sama
    def __init__(self, name, age):
        # self.___ itu atribut yang ada di class (pada instance tertentu ditandain pake self.)
        # yang kanan (=) itu nilai yang di assign ke atribut
        self.name = name
        self.age = age
    
    # sama ini
    # def __init__(self, inputted_name, inputted_age):
    #     self.name = inputted_name
    #     self.age = inputted_age
    #     # self.name = "Miles"
    #     # self.age = '4'
    

# instantiating
dog1 = Dog("miles", 2)
dog2 = Dog("abby", 2)
print(dog1.name, dog1.age)
print(dog2.name, dog2.age)

print("aman")
