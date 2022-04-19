# # if
# x = 0
# y = 5

# if x < y:                            # Truthy
#     print('yes 1')

# if y < x:                            # Falsy
#     print('yes 2')

# if x:                                # Falsy
#     print('yes 3')

# if y:                                # Truthy
#     print('yes 4')

# if 'aul' in 'grault':                # Truthy
#     print('yes 5')

# if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
#     print('yes 6')

# # true
# weather = 'nice'
# # false
# weather = 'not so nice'

# if weather == 'nice':
#     print('Mow the lawn')
#     print('Weed the garden')
#     print('Walks the dog')
# print('some following statement ....')

# if 'foo' in ['bar', 'baz', 'qux']:
#     print('Expression was true')
#     print('Executing statement in suite')
#     print('...')
#     print('Done.')
    
# print('After conditional')

# # Does line execute?                        Yes    No
# #                                           ---    --
# if 'foo' in ['foo', 'bar', 'baz']:        #  x
#     print('Outer condition is true')      #  x

#     if 10 > 20:                           #  x
#         print('Inner condition 1')        #        x

#     print('Between inner conditions')     #  x

#     if 10 < 20:                           #  x
#         print('Inner condition 2')        #  x

#     print('End of outer condition')       #  x
# print('After outer condition') 

# if-else

# x = 20
# x = 120

# if x < 50:
#     print('(first suite)')
#     print('x is small')
# else:
#     print('(second suite)')
#     print('x is large')

# hargaBuku = 20000
# hargaMajalah = 5000
# uang = 2000

# if uang > hargaBuku:
#     print("beli buku")
# else:
#     print("uang tidak cukup")

# if-elif-else

# hargaBuku = 20000
# hargaMajalah = 5000 - 4000
# uang = 2000

# if uang > hargaBuku:
#     print("beli buku")
# elif uang > hargaMajalah:
#     print("beli majalah")
# else:
#     print("uang tidak cukup")

# name = 'Hacktiv8'
# if name == 'Fred':
#     print('Hello Fred')
# elif name == 'Xander':
#     print('Hello Xander')
# elif name == 'Hacktiv8':
#     print('Hello Hacktiv8')
# elif name == 'Arnold':
#     print('Hello Arnold')
# else:
#     print("I don't know who you are!")

# # ini yg di exe yang atas, soalny udah true, meski yg trakhir jg true
# var = 13
# if 'a' in 'bar':
#     print('foo')
# elif 1/0:
#     print("This won't happen")
# elif var:
#     print("This won't either")

# # di bikin 1 line, ini preferensi aja mau 1 line atau kaya biasa
# weather = "nice"
# if weather == 'nice': print('Mow the lawn'); print('Weed the garden'); print('Walks the dog')

# if 'f' in 'foo': print('1'); print('2'); print('3')

# x = 21

# if x == 1: print('foo'); print('bar'); print('baz')
# elif x == 2: print('qux'); print('quux')
# else: print('corge'); print('grault')

# x = 20
# x = 120

# if x < 50: print('(first suite)'); print('x is small')
# else: print('(second suite)'); print('x is large')

# loop

# <expr1> if <conditional_expr> else <expr2>
# yang di run if dulu, kalo hasil if true run expr1, kl false expr2

# raining = True
# # raining = False
# print("Let's go to the", 'beach' if not raining else 'library')

# age = 12
# s = 'teen' if age < 21 else 'adult'
# print(s)

# run di cmd
# 'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

# # ini buat sementara kalo masih belum ada isi dari scriptny, bisa di bypass pake "pass"
# if True:
#     pass
# print('foo')