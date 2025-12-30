import zlib
import secrets
class Cipher:
    def __init__(self):
        pass
    def encrypt(self,filename):
        #file bytes read 
        with open(filename,'rb') as file:
            file_content = file.read()
        #file compress
        file_content = zlib.compress(file_content)
        #key generation
        key = []
        for x in range(0,20):
            key.append(secrets.randbelow(255) + 1)
        #file encrypt
        counter = 0
        encrypted = bytearray()
        for char in file_content:
            if counter % 2 == 0:
                char = char + key[counter]
            else:
                char = char - key[counter]
                if char < 0:
                    char = char + 256
            encrypted.append(char % 256)
            counter += 1
            if counter > len(key) - 1:
                counter = 0
        #changing file
        with open(filename,'wb') as file:
            file.write(encrypted)
        #massage
        print('\nfile encrypted')
        key_ = ''
        for x in key:
            key_ = key_ + '-' + str(x)
        print(f'key = {key_[1:len(key_)]}')
        return key_[1:len(key_)]
    def decrypt(self,filename,key):
        #file read
        with open(filename,'rb') as file:
            file_content = file.read()
        #key read
        key = str(key).split(sep= '-')
        #file decrypt
        counter = 0
        decrypted = bytearray()
        for char in file_content:
            if counter % 2 == 0:
                char = char - int(key[counter])
                if char < 0:
                    char = char + 256
            else:
                char = char + int(key[counter])
            decrypted.append(char % 256)
            counter += 1
            if counter > len(key) - 1:
                counter = 0
        #file decompress
        decrypted = zlib.decompress(decrypted)
        #changing file
        with open(filename,'wb') as file:
            file.write(decrypted)
        print('\nfile decrypted')
    def encrypt_with_copy(self,filename):
        with open(filename,'rb') as file:
            file_content = file.read()
        #making backup copy
        with open(f'backup_{filename}','wb') as file:
            file.write(file_content)
        #file compress
        file_content = zlib.compress(file_content)
        #key generation
        key = []
        for x in range(0,20):
            key.append(secrets.randbelow(255) + 1)
        #file encrypt
        counter = 0
        encrypted = bytearray()
        for char in file_content:
            if counter % 2 == 0:
                char = char + key[counter]
            else:
                char = char - key[counter]
                if char < 0:
                    char = char + 256
            encrypted.append(char % 256)
            counter += 1
            if counter > len(key) - 1:
                counter = 0
        #changing file
        with open(filename,'wb') as file:
            file.write(encrypted)
        #massage
        print('\nfile encrypted')
        key_ = ''
        for x in key:
            key_ = key_ + '-' + str(x)
        print(f'key = {key_[1:len(key_)]}')
        return key_[1:len(key_)]