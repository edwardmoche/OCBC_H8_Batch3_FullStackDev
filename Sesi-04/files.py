# open file

# file = open('Hack8_Sample_Text.txt')
# file.close()

# try:
#     f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
#     # perform file operations
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print('test run')
#     # f.close()
    
# # error not found
# try:
#     f = open("Hack8_Sample_Text_a.txt", encoding = 'utf-8')
#     # perform file operations
# except FileNotFoundError:
#     print('File not found')
# finally:
#     print('test run')
#     # f.close()

# # write

# # note templateny pake sample.txt aja, soalny dia sistemny overwrite
# with open("sample.txt",'w',encoding = 'utf-8') as f:
#    f.write("my first file\n")
#    f.write("This file\n\n")
#    f.write("contains three lines\n")
#    f.write("Edward")

# read

# note, dibikin di satu folder yang di read
f = open("sample.txt",'r',encoding = 'utf-8')

# # ini kalo di run di terminal 
# # dia cuma nampilin 4 huruf, termasuk special char
# f.read(4)
# # kalo ini read semua
# f.read()

# # kalo mau run file pake ini
# # konsepnya sama kaya yang terminal
# print(f.read(4))
# print(f.read(4))
# print(f.read())

# # seek buat naro posisi cursor sekarang
# # kalo di terminal, abis baca semua harus d fseek lagi 
# f.seek(0)   # bring file cursor to initial position
# # ini buat read per baris, karena kl pake yang atas masih ada input kaya "\n"
# for line in f:
#   print(line, end = '')

# f.seek(0)
# # kalo ini dia baca hanya 1 baris/line
# f.readline()

# bisa juga buat read pake ini
with open('sample.txt', 'r') as reader:
     # Read & print the entire file
     print(reader.read())