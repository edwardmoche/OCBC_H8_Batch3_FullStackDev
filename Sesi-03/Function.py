# # basic fungsi function
# tambahin def kalo mau buat fungsi (def=definition)
# def function_name( parameters ):
#    '''docstring'''
#    statement(s)

# # Contoh pembuatan function

# # penghitungan luas
# def my_function(p, l):
#     '''Function to calculate area of a square'''
#     print(p * l)

# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# # pemanggilan fungsi

# # pendefinisian fungsi (buat dulu apa yg mau dipanggil)
# # str input itu dia ngambil dari isi panggilan printme
# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# # panggil fungsi yang udah dibuat tadi
# # ini isinya d proses sama def printme, dijadiin str_input
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")

# perbedaan pass by reference & value

# # buat fungsinya
# def changeme( mylist ):
#    '''This changes a passed list into this function'''
#    mylist = mylist+[1,2,3,4]
#    print("\nValues inside the function : ", mylist)
#    return mylist

# # panggil def fungsi
# mylist = [10,20,30]
# print("\nValues outside the function - before : ", mylist)
# # ini hasil dari mylist yang udah diolah pake fungsi "changeme"
# # kenapa bisa, krn python baca perline, mylist yg awal di tiban sm yg ini
# mylist = changeme( mylist )
# print("\nValues outside the function - after  : ", mylist)

# # contoh 2
# # kalo yang ini ke overwrite
# # Function definition is here
# def changeme( mylist ):
#    '''This changes a passed list into this function'''
#    mylist = [1, 2, 3, 4] # This would assign new reference in mylist
#    print("Values inside the function  : ", mylist)

# # Now you can call changeme function
# mylist = [10, 20, 30]
# changeme( mylist )
# print("Values outside the function : ", mylist)

# # required argument

# # persyaratan yang ini didalemnya harus ada string
# # Function definition is here
# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)
 
# # Now you can call printme function
# printme("Hello")

# # # ini bakal error karena didalem printme nggak ada string
# # printme()

# # contoh 2 buat bikin luas
# # persyaratannya harus ada length sama width
# # Function definition is here
# def calculate_rect(length, width):
#   '''This function is used to calculate area of rectangle'''
#   print('Area : ', length*width)

# # Define parameters
# length = 100
# width = 20

# # Call calculate_rect
# calculate_rect(length, width)

# # # ini error karena cuman ada length aja
# # calculate_rect(length)

# # keyword input

# # Function definition is here
# def printme( str_input ):
#    '''This prints a passed string into this function'''
#    print(str_input)

# # Now you can call printme function
# printme(str_input = "Hacktiv8")

# # contoh 2
# # Function definition is here
# def printinfo( name, age ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age. : ", age)

# # Now you can call printinfo function
# # kalo ini sesuai outputnya karena dia di declare untuk masuk kemananya
# # walaupun urutannya nggak sesuai
# printinfo( age=4, name="a" )
# # disini hasilnya nggak sesuai karena pyt bacanya berdasarkan urutan (1 , 2, ..., n)
# printinfo( 4, "a" )
# # ini error karena kurang positional argumentnya
# printinfo( name="a" )

# # default argument

# # Function definition is here
# def printinfo( name, age = 26 ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")

# # ini error karena yang sebelumnya pake "=", pyt expect kalo selanjutnya pake "=" juga (name = x)
# def printinfo( age = 26, name ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")

# # contoh 2
# # ini baru nggak error
# def printinfo( age = 26, name = "xantos" ):
#    '''This prints a passed info into this function'''
#    print("Name : ", name)
#    print("Age  : ", age)
#    print("")

# # tambahan aja, ini kalo ikutin format urutan
# printinfo( "hackt", 14 )
# # Now you can call printinfo function
# printinfo( age=50, name="hacktiv8" )
# # ini kenapa nggak error, soalnya di positionalnya udah ada argument dasarnya (age = 26)
# printinfo( name="hacktiv" )
# # ini buat manggil contoh 2
# # ini bisa karena udah di declare dua2nya di contoh 2
# printinfo()

# # variable length argument

# # dia gunain "*" supaya bisa baca banyak data karena itu jadinya buat tuple
# # Function definition is here
# def printinfo( arg1, *vartuple ):
# # def printinfo(arg1, arg2, arg3, arg4):
#     '''This prints a variable passed arguments'''
#     print('arg1     : ', arg1)
#     print('vartuple : ', vartuple)
   
# # ini buat print masing2 isi vartuple
# # fyi, var itu bisa di ganti apa aja, cuman buat penamaan dari variable (bisa "x", "dono", dst)
#     for var in vartuple:
#         print('isi vartuple : ', var)
          
#     print()

# # Now you can call printinfo function
# printinfo( 10 )
# # ini yang bakal jadi vartuple, soalnya lebih dari 1 argument (60, ....)
# # kenapa 70 nya nggak ikut? soalnya dia masuk arg1, vartuple itu ibarat arg2, arg3, arg4, .....,argN
# # cuman hasilnya dibungkus sama "()" karena jadi tuple
# printinfo( 70, 60, 50, "a" )
# printinfo( 20, 10, 30, "b" )
# printinfo( "c" )
# # note tambahan, perhatiin indent

# # kalo tadi pake "*", sekarang pake "**"
# # bedanya kalo * jadi tuple, kalo ** jadi dictionary
# def print_bought_items(name, **bought_items):
#   '''Create a function to print which items somebody bought'''
#   print('Name : ', name)
 
#   for key, value in bought_items.items():
#     print('key   : ', key)
#     print('value : ', value)
 
#   print('')
 
# print_bought_items("Ani", first="egg", second="sugar", third="salt", fourth="baking powder")
# print_bought_items("Ali", first="thread", second="hoop", third="neddle")
# print_bought_items("Cici", fruit="Apple", milk='oatmilk')


# # Anonymous Functions

# # ini bedanya sama yang normal, kalo biasanya pake "def", kalo ini pake "lambda" buat bikinnya
# # Function definition is here
# # ":" itu pembatas yang positional argument
# sum = lambda arg1, arg2: arg1 + arg2
# multiply = lambda arg1, arg2: arg1 * arg2

# # itu sama aja kaya gini kalo pake def
# # def sum(arg1, arg2):
# #     return arg1+arg2

# # Now you can call sum as a function
# print("Value of total : ", sum( 10, 20 ))
# print("Value of total : ", sum( 20, 20 ))
# print()
# # ini tambahan aja
# print("Value of total : ", multiply( 10, 20 ))
# print("Value of total : ", multiply( 20, 20 ))

# # return Statement

# # Function definition is here
# from unittest import result


# def sum(arg1, arg2):
#     # Add both the parameters and return them."
#     total = arg1 + arg2
#     total2 = total + arg1
#     # return total
#     # return total2
#     return total, total2

# # Now you can call sum function
# # kalo mau satuan yang return di atas di uncomment yg d pake, coomment yang nggak
# # soalnya hasil ini sama result sama
# total = sum(10, 20)
# print("Result function : ", total)
# print()
# # ini kalo mau return 2<
# result = sum(10, 20)
# print("Result function : ", result)
# print()
# x,y = sum(10, 20)
# print("Result function : ", x, y)

# # scope variable

# # Declare a global variable
# total = 0

# # Create sum function
# def sum( arg1, arg2 ):
#    total = arg1 + arg2; 
#    print("Inside the function local total   : ", total)

# # Call a function
# sum( 10, 20 )
# print("Outside the function global total : ", total)

# # contoh 2
# # Declare a global variable
# total = 0

# # Create sum function
# def sum( arg1, arg2 ):
#    total = arg1 + arg2; 
#    print("Inside the function local total   : ", total)
#    return total

# # Call a function
# print("Outside the function global total - before : ", total)
# total = sum( 10, 20 )
# print("Outside the function global total - after  : ", total)

# # docstring

# # docstring itu ibarat comment kayanya(?)
# # cara buatnya pake 3 (') atau (")
# # Example of docstring in a function
# def sum_number(num1, num2):
#   '''
#   This function is used to sum of 2 variables.
#   :param num1: Input number 1 | int or float
#   :param num2: Input number 2 | int or float
  
#   :return: num3: Sum of number | int or float
#   '''

#   num3 = num1 + num2
#   return num3

# print("ini hasil function: ")
# print(sum_number(1, 23))
# print()

# # ini buat manggil docstring (_doc_)
# print("ini docstringnya: ")
# print(sum_number.__doc__)