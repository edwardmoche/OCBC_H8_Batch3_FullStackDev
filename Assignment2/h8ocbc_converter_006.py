def suhu(kelvin):
    # ini merupakan docstring, hanya untuk memastikan saja apakah function yang dijalankan pada saat di run benar
    '''a'''
    # untuk menampilkan printout "konversi suhu:"
    print("Konversi suhu: ")
    # ini adalah script untuk menampilkan suhu yang di input
    print('Kelvin               :', kelvin, "K")
    # ini script untuk mengkonversi kelvin ke celcius
    celcius = kelvin - 273
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('kelvin ke celcius    :', celcius, "C")
    # ini script untuk mengkonversi kelvin ke farenheit
    farenheit = (kelvin-273) * (9/5) + 32 
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('kelvin ke farenheit  :', farenheit, "F")
    # ini adalah script untuk memanggil fungsi confirm
    return confirm()
    

def suhu2(celcius):
    # ini merupakan docstring, hanya untuk memastikan saja apakah function yang dijalankan pada saat di run benar
    '''b'''
    print("Konversi suhu: ")
    # ini adalah script untuk menampilkan suhu yang di input
    print('Celcius              :', celcius, "C")
    kelvin = celcius + 273
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('celcius ke kelvin    :', kelvin, "K")
    farenheit = celcius * (9/5) + 32 
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('celcius ke farenheit :', farenheit, "F")
    # ini adalah script untuk memanggil fungsi confirmv
    return confirm()

def suhu3(farenheit):
    # ini merupakan docstring, hanya untuk memastikan saja apakah function yang dijalankan pada saat di run benar
    '''c'''
    print("Konversi suhu: ")
    # ini adalah script untuk menampilkan suhu yang di input
    print('farenheit            :', farenheit, "F")
    celcius = (farenheit-32) * (5/9)
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('farenheit ke celcius :', celcius, "C")
    kelvin = (farenheit-32) * (5/9) + 273 
    # ini adalah script untuk menampilkan suhu yang di konversi
    print('farenheit ke kelvin  :', kelvin, "K")
    # ini adalah script untuk memanggil fungsi confirm
    return confirm()
    
# ini adalah fungsi untuk pengecekan apakah pengguna masih ingin menggunakan aplikasi/tidak
def confirm():
    # pembuatan variable untuk percabangan if
    konfirmasi = input("apakah anda ingin melakukan koversi yang lain (y/n)? ")
    # jika ini maka akan dibawa kembali ke fungsi opsi
    if konfirmasi == "y":
        print()
        return opsi()
    # jika tidak program akan di terminate
    elif konfirmasi == "n":
        print()
        print("Sampai Jumpa!")
        exit()
    # jika yang di input tidak sesuai, maka akan diminta untuk penginputan ulang
    else:
        print("maaf konversi tersebut tidak ada, silahkan pilih lagi!")
        return confirm()



def opsi():
    # pembuatan variable untuk percabangan if
    # jika memilih 1-3 maka akan dibawa ke fungsinya masing-masing
    perintah = input("Tekan angka untuk memilih : ")
    if perintah == "1":
        print(suhu(int(input("Masukan suhu kelvin : "))))
        print()
        # ini hanya untuk konfirmasi saja
        print("ini docstringnya: ")
        print(suhu.__doc__)
    elif perintah == "2":
        print(suhu2(int(input("Masukan suhu celcius : "))))
        print()
        # ini hanya untuk konfirmasi saja
        print("ini docstringnya: ")
        print(suhu2.__doc__)
    elif perintah == "3":
        print(suhu3(int(input("Masukan suhu farenheit : "))))
        print()
        # ini hanya untuk konfirmasi saja
        print("ini docstringnya: ")
        print(suhu3.__doc__)
    # jika user menggunakan ini maka aplikasi akan di terminate
    elif perintah == "4":
        print()
        print("Sampai Jumpa!")
        exit()
    else:
    # jika yang di input tidak sesuai, maka akan diminta untuk penginputan ulang
        print("maaf inputan anda salah, silahkan ulangi kembali lagi!")
        print()
        return opsi()

# ini merupakan tampilan awal dari program
print("Konversi Suhu")
print("pilih konversi yang anda inginkan!")
print("1. kelvin")
print("2. celcius")
print("3. farenheit")
print("4. keluar")
# ini merupakan script untuk memanggil fungsi opsi
opsi()