import cipher as c
x = c.Cipher()
while True:
    print('Select option (type number)')
    print('------------------')
    what_number = input('1. encrypt file\n2. decrypt file\n3. quit\n')
    if what_number == '1':
        if_backup = input('Do you want to make backup copy? (Y/N) ')
        if if_backup == 'Y':
            filename = input('Type filename: ')
            x.encrypt_with_copy(filename)
        if if_backup == 'N':
            filename = input('Type filename: ')
            x.encrypt(filename)
    if what_number == '2':
        filename = input('Type filename: ')
        key = input('Type key: ')
        x.decrypt(filename,key)
    if what_number == '3':
        break

    