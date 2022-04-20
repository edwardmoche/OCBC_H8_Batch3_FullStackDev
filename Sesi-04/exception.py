# Exception 

# try:
#     f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#     # perform file operations
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print('test run')
#     # f.close()

# x = 10
# if x > 5:
#     raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# # ini run di terminal
# # ini tetep bakal error, soalny kalo mau jalan yang windows diganti win (tergantung platform pc)
# import sys
# assert ('linux' in sys.platform), "This code runs on Linux only."
# assert ('windows' in sys.platform), "This code runs on Windows only."
# # ini g bakal ada error kalo ada yang bawah
# assert ('win' in sys.platform), "This code runs on Windows only."

# # try except

# # run ini dulu
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# # kalo nggak bisa baru bawah jalan
# except:
#     print('Could not open file.log')

# import sys
# # hasilnya yang assert linuxnya jalan
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except:
#     print('skipp')
#     pass

# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
#     print('The os_interaction() function was not executed')

# Here’s another example where you open a file and use a built-in exception:

# ini manual
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')

# # ini built-in
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# # ini yang di run cuma asserterror, soalnya os_interaction dulu yang ke trigger, urutan baca "os > open file" jadinya yang di run exceptnya yang assert
# try:
#     os_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('os_interaction() function was not executed')


# # else cause

# # kalo pake yang ini masih trigger yang linux
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')
    
# contoh 1
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     print('Executing the else clause.')

# # contoh 2
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)

# # contoh 3
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('sample.txt') as file:
#             read_data = file.read()
#             print(read_data)
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)

# cleaning setelah finally

# ini error kaya biasa
# import sys
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     assert ('win' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

import sys
def os_interaction():
    # assert ('linux' in sys.platform), "Function can only run on Linux systems."
    # assert ('windows' in sys.platform), "This code runs on Windows only."
    assert ('win' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

# ini error di file.log
# try:
#     os_interaction()
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('Cleaning up, irrespective of any exceptions.')

# ini jalan semua
try:
    os_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('sample.txt') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')