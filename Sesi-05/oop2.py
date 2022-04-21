# method sama atributnya udah sepaket di class
# class Dog:
#     # Class attribute
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         # instance attribute
#         self.name = name
#         self.age = age

#     # # ini buat bypass kalo ada kaya yang Dog() biar gak error, cuman ya nggak ada outputnya
#     # def __init__(self):
#     #     pass


# instantiating
# dog1 = Dog("miles", 2)
# dog2 = Dog("abby", 2)
# # ini tetep bisa d run, tapi paling cuma nampilin species doang
# dog3 = Dog("", "")
# # # kalo pake yang ini error, soalnya kurang parameter
# # dog3 = Dog()
# print(dog1.name, dog1.age, dog1.species)
# print(dog2.name, dog2.age, dog2.species)
# print(dog3.name, dog3.age, dog3.species)

# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)

# print(buddy.name)
# print(miles.name)

# print(buddy.age)
# print(miles.age)

# print(buddy.species)
# print(miles.species)

# # ------Instance Methods------

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         # # bisa gini
#         # return f"{self.name} is {self.age} years old"
#         # # atau gini
#         return self.name + " is " + str(self.age) + " years old"

#     # Another instance method
#     def speak(self, sound):
#         # return f"{self.name} says {sound}"
#         # # sama
#         return self.name + " says " + sound


# dog1 = Dog("miles", 2)
# dog2 = Dog("abby", 2)
# dog3 = Dog("", "")
# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)

# # bisa kaya gini
# print(buddy.description())
# print(buddy.speak("Woof Woof"))
# print()
# # ato kek gini
# description_of_buddy = buddy.description()
# print(description_of_buddy)
# sound_of_buddy = buddy.speak("Bow Wow")
# print(sound_of_buddy)

# ------Inheritance------

