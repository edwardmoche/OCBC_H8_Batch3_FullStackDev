# decrement
# n = 5
# while n > 0:
#     n -= 1
#     print(n)

# increment
# i = 1
# while i < 6:
#   print(i)
#   i += 1

# # kalo break program stop
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break # Break Statement
#     print(n)
# print('Loop ended.')

# # kalo continue program skip bagian yang kena
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n)
# print('Loop ended.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
# else:
#     print('Loop done.')

# n = 5
# while n > 0:
#     n -= 1
#     print(n)
#     if n == 2:
#         break
# else:
#     print('Loop done.')



# # infinite loop
# while True:
#     print('foo')

# # nested if
# age = 80
# gender = "F"
# if age < 18:
#     if gender == 'M':
#         print('son')
#     else:
#         print('daughter')
# elif age >= 18 and age < 65:
#     if gender == 'M':
#         print('father')
#     else:
#         print('mother')
# else:
#     if gender == 'M':
#         print('grandfather')
#     else:
#         print('grandmother')

# a = ['foo', 'bar']

# while len(a):
#     print(a.pop(0))
    
#     b = ['baz', 'qux']
    
#     while len(b):
#         print('>', b.pop(0))

# while bisa dibikin 1 line juga

# for

# a = ['foo', 'bar', 'baz']
# for i in a:
#     print(i)

# d = {'foo': 1, 'bar': 2, 'baz': 3}
# for k in d:
#     # print(k)
#     print(d[k])
# print()

# for k in d.values():
#     print(k)
# print()

# for k, v in d.items(): 
#     print(k, ":", v) 

# for n in (0, 1, 2, 3, 4):
#     print(n)
# print()

# # ini bisa di akalin pake range
# # range(panjang index)
# for n in range(5):
#     print(n)

# # ini kalo mau mulai dari index sekian
# for n in range (1, 5):
#     print(n)

# # ini kalo mau nampilin ganjil/genap, angka terakhir itu kaya +
# for n in range (2, 20, 2):
#     print(n)

# # ini kebalikan yang atas kalo mau decrement
# for n in range (20, 2, -2):
#     print(n)

# # ini buat ngecek ada string "b" nggak
# # kalo ini di break
# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         break
#     print(i)
# print()

# # kalo ini cont
# for i in ['foo', 'bar', 'baz', 'qux']:
#     if 'b' in i:
#         continue
#     print(i)

# # done di exe abis list selesai
# for i in ['foo', 'bar', 'baz', 'qux']:
#     print(i)
# else:
#     print('Done.')  # Will execute

# # ini kenapa nggak print done karena loop terminate sama break
# for i in ['foo', 'bar', 'baz', 'qux']:
#   if i == 'bar':
#     break
#   print(i)
# else:
#   print('Done.') 