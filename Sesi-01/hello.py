print('hello world')
print("")
# print(123 + 1)
# print(type(123 + 1))

# # pake \ biar ga di detect sm pyt
# print ("test (\") kalo nggak pake (\) di sebelumnya nanti error ")

# a = 200

# print(a)

# # bisa assign brp var

# a = b = c = 100

# print (a, b, c)

# # var bisa tiban2an, di yang di tampilin yang plg baru

# var = 21.14
# print(var)
# print(type(var))
# print()

# var = "lah kok ganti type data"
# print(var)
# print(type(var))

# name = "Hacktiv8"
# Age = 54
# has_laptops = True
# print(name, Age, has_laptops)
# has_5laptops = False
# print(has_5laptops)

# # penamaan nggak boleh angka duluan
# 9_kepala_naga = True


# # bisa campur sari juga

# a = 10
# b = 20
# print (a + b - 5)

# a = 7
# b = 2

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b) # pembulatan
# print(a % b) # sisa pembagian
# print(a ** b)

# # manipulasi string

# s = "foo"
# t = "bar"
# u = "baz"


# print(s+t)
# print(s+t+u)

# print(s * 3) # ini foo dipanggil 3x

# # ini ngecek kalo ada tulisan "foo" nggak
# print (s in "good food for us") # "foo"d
# print (s in "good dood for us") # ini nggak ada

# # case conversion
# a = "teStINg tEsTEr"

# #beda title sama cap kl title di smua kata, cap cuman awal
# print(a.title())
# print(a.capitalize())
# print()
# # ini capslock/nggak
# print(a.upper())
# print(a.lower())
# print()
# # ini nuker caps
# print(a)
# print(a.swapcase())

# # list mirip kaya array biasa
# a = ['foo', 'bar', 'baz', 'qux']

# print(a)
# print(type(a))
# # bedanya isinya bisa campursari
# a = [1 , 'bar', 22.5, 'qux', False]
# print(a)

# # bisa bandingin 2 list

# a = ['foo', 'bar', 'baz', 'qux']
# b = ['bar', 'foo', 'qux', 'baz']

# print(a==b)

# # cara akses/index
# a = ['foo', 'bar', 'baz', 'qux']

# print(a)
# # ini kaya array biasa, paling kiri 0
# print(a[0])
# print(a[2])
# # kalo "-" bacanya dari kanan trs mulai dr -1
# print(a[-1])

# # slicing
# a = ['foo', 'bar', 'baz', 'qux', 'yon', 'duu', 'haa', 'ase']

# print(a)
# print(a[2:5])

# a = ['foo', 'bar', 'baz', 'qux', 'yon', 'duu', 'haa', 'ase']
# print(a)
# # tambah data
# print(a + ['uhu', 'ehe'])
# print(a)
# # 
# print (a * 2)
# print(a)

# # modify data
# a = ['foo', 'bar', 'baz', 'qux', 'yon', 'duu', 'haa', 'ase']
# print(a)
# # ngecek panjang, min, max
# print(len(a))
# print(min(a))
# print(max(a))

# a[2] = 10
# a[-1] = 20
# print (a)

# # tiban beruntun
# a = ['foo', 'bar', 'baz', 'qux', 'yon', 'duu', 'haa', 'ase']
# print(a)
# print(a[1:4])
# # tiban
# a[1:4] = [1, 2.2, 3, 4]
# print(a)

# # tuple
# t = ('foo', 'bar', 'baz', 'qux', 'yon', 'duu', 'haa', 'ase')
# print(t)
# print(t[0])
# print(t[-1])
# print(type(t))

# # packing & unpacking
# (s1, s2, s3, s4) = ('foo', 'bar', 'baz', 'qux')
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print()

# # bisa juga kaya gini
# t1 = ('foo', 'bar', 'baz', 'qux')
# (s1, s2, s3, s4) = t1
# print(s1)
# print(s2)
# print(s3)
# print(s4)

# # immutable tuple
# # error
# t4 = ('foo', 'bar', 'baz', 'qux')
# t4[0] = 'foo' * 2 

# # bisa
# t4 = ('foo', 'bar', 'baz', 'qux')
# t4 = ('aa' 'bb', 'cc')
# print(t4)

# person1_age = 42
# person2_age = 16
# person3_age = 71
# print(person1_age, person2_age, person3_age)

# # dar
# # someone_is_of_working_age = (person1_age >= 18 and person1_age <= 65) or (person2_age >= 18 and person2_age <= 65) or (person3_age >= 18 and person3_age <= 65)
# someone_is_of_working_age = (
#     (person1_age >= 18 and person1_age <= 65)       # True
#     or (person2_age >= 18 and person2_age <= 65)    # False
#     or (person3_age >= 18 and person3_age <= 65)    # False
# ) # True or .. false or .. false
 
# print(someone_is_of_working_age)



# # dictionary (nanti liat di gdoc aja mager nambah manual)
# mlb_team = {
#     'Colorado': 'Rockies',
#     'Boston': 'Red Sox',
#     'Minnesota': 'Twins'
# }

# print(mlb_team)
# print(type(mlb_team))
# # print spesifik
# print(mlb_team['Minnesota'])
# print(mlb_team['Boston'])
# # tambah dict
# mlb_team['Kansas City'] = 'Royals'
# print(mlb_team)
# # edit 
# mlb_team
# # del
# mlb_team

# # buat lib dari kosong
# person = {}
# type(person)

# person['fname'] = 'Hack'
# person['lname'] = 'Inalum'
# person['age'] = 25
# person['spouse'] = 'Edna'
# person['children'] = ['Ralph', 'Betty', 'June']
# person['pets'] = {'dog': 'Fido', 'cat': 'Tom'}

# print(person)
# print()
# print(person['fname'])
# print()
# print(person['age'])
# print()
# print(person['children'])
# print()
# print(person['pets']['cat'])

# kalo script pajang karena pyt bacany per line, pake "()" nanti bisa kebawahs