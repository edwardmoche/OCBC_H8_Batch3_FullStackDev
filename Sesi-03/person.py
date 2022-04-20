name = 'zack'
devices = ['laptop', 'smartphone', 'tablet']

def display(arg):
    print(f'arg = {arg}')

# ini biar waktu di run biasa tampil, tapi kalo di run dari cmd nggak keluar
# karena kl run cmd dia pengen di jadiin module
if (__name__ == '__main__'):
    print('Executing as standalone script')
    print(name)
    print(devices)
    print(display('Good Morning'))