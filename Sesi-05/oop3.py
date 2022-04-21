# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age, breed):
#         self.name = name
#         self.age = age
#         self.breed = breed

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"


# miles = Dog("Miles", 4, "Jack Russell Terrier")
# buddy = Dog("Buddy", 9, "Dachshund")
# jack = Dog("Jack", 3, "Bulldog")
# jim = Dog("Jim", 5, "Bulldog")

# print(miles.name, miles.age, miles.breed)
# print()
# print(miles.description())
# print(miles.speak("Woof"))

# # parent class
# # child class bisa override atau extend dari parent class
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # kalo mau baca yang ini langsung declare nama aja, ngak usah pake (nama.description())
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    # ini 2 masih nggak tau buat apa
    # 1
    def __repr__(self):
        return f"to create instance :: Dog( name={self.name}, age={self.age} ) #REPR"
 
    # 2
    def __str__(self):
        return f"clean info :: {self.name} is {self.age} years old  #STR"

# child class
class JackRussellTerrier(Dog):
    # ini contoh override
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

# child class
class Dachshund(Dog):
    pass

# child class
class Bulldog(Dog):
    # pass

    def __init__(self, name, age, weight_in_lbs):
        # kenapa pake super?
        super().__init__(name, age )
        self.weight_in_lbs = weight_in_lbs


miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3, 120)
jim = Bulldog("Jim", 5, 89)

print(miles.name, miles.age)
print()
# ini kenapa kaya gini, soalnya di yang biasanya itu "description()" sekarang nggak ada deklarasinya (__str__)
print(miles)
# # karena dia udah di override buat anjing yang jackrousel suaranya kaya gimana, jadi udah langsung ada templatenya
# print(miles.speak("Woof"))
# # langsung gini aja
print(miles.speak())
# # tapi kalo misal di tulis, yang ditampilin yang ditulis, bukan template
print(miles.speak("Grrr"))

# ini manggil overridenya
# pake dict buat nampilin dlm bentuk dict "{}"
print(jim.__dict__)
print(jim)
print(jim.speak("Woof"))

# tambahan aja
# ini buat yang str & repr

print('REPR and STR part')
 
print(repr(miles))
print(miles.__repr__())
 
print(str(miles))
print(miles.__str__())
