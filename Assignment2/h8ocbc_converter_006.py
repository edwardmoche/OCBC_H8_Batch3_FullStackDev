def suhu(kelvin):
    '''a'''
    print("Konversi suhu: ")
    print('Kelvin               :', kelvin, "K")
    celcius = kelvin - 273
    print('kelvin ke celcius    :', celcius, "C")
    farenheit = (kelvin-273) * (9/5) + 32 
    print('kelvin ke farenheit  :', farenheit, "F")
    return confirm()
    

def suhu2(celcius):
    '''b'''
    print("Konversi suhu: ")
    print('Celcius              :', celcius, "C")
    kelvin = celcius + 273
    print('celcius ke kelvin    :', kelvin, "K")
    farenheit = celcius * (9/5) + 32 
    print('celcius ke farenheit :', farenheit, "F")
    return confirm()

def suhu3(farenheit):
    '''c'''
    print("Konversi suhu: ")
    print('farenheit            :', farenheit, "F")
    celcius = (farenheit-32) * (5/9)
    print('farenheit ke celcius :', celcius, "C")
    kelvin = (farenheit-32) * (5/9) + 273 
    print('farenheit ke kelvin  :', kelvin, "K")
    return confirm()
    

def confirm():
    konfirmasi = input("apakah anda ingin melakukan koversi yang lain (y/n)? ")
    if konfirmasi == "y":
        print()
        return opsi()
    elif konfirmasi == "n":
        print()
        print("Sampai Jumpa!")
        exit()
    else:
        print("maaf konversi tersebut tidak ada, silahkan pilih lagi!")
        return confirm()



def opsi():
    perintah = input("Tekan angka untuk memilih : ")
    if perintah == "1":
        print(suhu(int(input("Masukan suhu kelvin : "))))
        print()
        
        print("ini docstringnya: ")
        print(suhu.__doc__)
    elif perintah == "2":
        print(suhu2(int(input("Masukan suhu celcius : "))))
        print()

        print("ini docstringnya: ")
        print(suhu2.__doc__)
    elif perintah == "3":
        print(suhu3(int(input("Masukan suhu farenheit : "))))
        print()

        print("ini docstringnya: ")
        print(suhu3.__doc__)
    elif perintah == "4":
        print()
        print("Sampai Jumpa!")
        exit()
    else:
        print("maaf inputan anda salah, silahkan ulangi kembali lagi!")
        print()
        return opsi()

print("Konversi Suhu")
print("pilih konversi yang anda inginkan!")
print("1. kelvin")
print("2. celcius")
print("3. farenheit")
print("4. keluar")
opsi()