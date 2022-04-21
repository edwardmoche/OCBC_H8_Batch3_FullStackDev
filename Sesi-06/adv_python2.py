# generator
# def my_generator():
#     print("Inside my generator")
#     # yield itu salah 1 statement buat generator   
#     yield 'a'
#     yield 'b'
#     yield 'c'

# print(my_generator())
# print(next(my_generator()))
# print(next(my_generator()))
# print(next(my_generator()))

# def my_generator():
#     print("Inside my generator")
#     # yield itu salah 1 statement buat generator   
#     yield 'a'
#     yield 'b'
#     yield 'c'

# # ini kl mo di terminal
# print(my_generator())
# print(next(my_generator()))
# print(next(my_generator()))
# print(next(my_generator()))

# # ini kl mau run
# for x in my_generator():
#     print(x)

# # urutan run
# def counter_generator(low, high): #2 // 5 sampe 10
#     while low <= high:            #3 // dicek apa masih <= // ini kalo di run sampe 11, cman yg di print sampe 10
#        yield low                  #4 // return loo
#        low += 1                   #6 // nilai yang tadi di tambah 1

# for i in counter_generator(5,10): #1 // ini nanti masuk ke low high
#   print(i, end=' ')               #5 // ini di print i trs di setiap i selesai dikasih "" (spasi)

# # functions
# # ini run di terminal
# def add_one(number):
#      return number + 1
# # itu bisa berapa aj nggak harus 2
# add_one(2)


# # first class object

# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))


# # inner function

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# print(parent())


# # Returning Functions From Functions

# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child

# # ini kalo 1 diganti auto nampilin second_child
# first = parent(1)
# # kalo pake ini yang di print cuma reference doang
# print(first)

# print(first())
# # ini bisa berapa aja selain 1 soalny cuman if else
# second = parent(3)
# print(second)

# print(second())


# # simple decorators

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")

# # ini yang di kiri (=) bisa d ganti apa aj, kebetulan aj sama2 say_whee
# say_whee = my_decorator(say_whee)
# print(say_whee)

# # ini nggak perlu print buat nampilin
# say_whee()

# # ini cuman biar keliatan aja, kalo atas fungsi sama var kecampur
# say_whe = my_decorator(say_whee)
# print(say_whe)
# say_whe()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# ini buat ganti yang "say_whe = my_decorator(say_whee)"
@my_decorator

# mungkin kl sempet nanya sih, "ini kan contoh 1 function doang, kalo misal ada lebih dari 1 gimana? ky python tuh bisa bedain mana yg mananya gak buat yang @my_decorator nya ini"

def say_whee():
    print("Whee!")

print(say_whee)
say_whee()

