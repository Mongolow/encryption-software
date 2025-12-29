import cipher as c
import zlib
x = c.Cipher()
while True:
    print('\nSelect option (type number)')
    print('------------------')
    what_number = input('1. encrypt file\n2. decrypt file\n3. quit\n')
    if what_number == '1':
        if_backup = input('Do you want to make backup copy? (Y/N) ')
        if if_backup == 'Y' or if_backup == 'y':
            filename = input('Type filename: ')
            try:
                x.encrypt_with_copy(filename)
            except FileNotFoundError:
                print('\nFile not found, try again\n')
            except Exception as e:
                print(f'\nAn error occurred: {e}\n')
        if if_backup == 'N' or if_backup == 'n':
            filename = input('Type filename: ')
            try:
                x.encrypt(filename)
            except FileNotFoundError:
                print('\nFile not found, try again\n')
            except Exception as e:
                print(f'\nAn error occurred: {e}\n')
    if what_number == '2':
        filename = input('Type filename: ')
        key = input('Type key: ')
        try:
            x.decrypt(filename,key)
        except ValueError:
            print('\nWrong key format, try again\n')
        except FileNotFoundError:
            print('\nFile not found, try again\n')
        except zlib.error:
            print('\nWrong key or file is not encrypted, try again\n')
        except Exception as e:
            print(f'\nAn error occurred: {e}\n')
    if what_number == '3':
        break