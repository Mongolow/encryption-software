import zlib
import secrets
def open_file(filename):
    with open(filename,'rb') as file:
        file_content = file.read()
    return file_content
def write_file(filename,content):
    with open(filename,'wb') as file:
        file.write(content)
def encrypt_decrypt_bytearray(data, key, mode):
    counter = 0
    result = bytearray()
    for char in data:
        if mode == 'encrypt':
            if counter % 2 == 0:
                char = char + key[counter]
            else:
                char = char - key[counter]
                if char < 0:
                    char = char + 256
        elif mode == 'decrypt':
            if counter % 2 == 0:
                char = char - key[counter]
                if char < 0:
                    char = char + 256
            else:
                char = char + key[counter]
        result.append(char % 256)
        counter += 1
        if counter > len(key) - 1:
            counter = 0
    return result
def key_generation():
    key = []
    for x in range(0,20):
        key.append(secrets.randbelow(255) + 1)
    return key
class Cipher:
    def __init__(self):
        pass
    def encrypt(self,filename):
        #file bytes read 
        file_content = open_file(filename)
        #file compress
        file_content = zlib.compress(file_content)
        #key generation
        key = key_generation()
        #file encrypt
        encrypted = encrypt_decrypt_bytearray(file_content, key, 'encrypt')
        #changing file
        write_file(filename,encrypted)
        #massage
        print('\nfile encrypted')
        key_ = ''
        for x in key:
            key_ = key_ + '-' + str(x)
        print(f'key = {key_[1:len(key_)]}')
        return key_[1:len(key_)]
    def decrypt(self,filename,key):
        #file read
        file_content = open_file(filename)
        #key read
        key = str(key).split(sep= '-')
        key_ = []
        for x in key:
            key_.append(int(x))
        #file decrypt
        decrypted = encrypt_decrypt_bytearray(file_content, key_, 'decrypt')
        #file decompress
        decrypted = zlib.decompress(decrypted)
        #changing file
        write_file(filename,decrypted)
        #massage
        print('\nfile decrypted')
    def encrypt_with_copy(self,filename):
        file_content = open_file(filename)
        #making backup copy
        write_file(f'copy_of_{filename}',file_content)
        #file compress
        file_content = zlib.compress(file_content)
        #key generation
        key = key_generation()
        #file encrypt
        encrypted = encrypt_decrypt_bytearray(file_content, key, 'encrypt')
        #changing file
        write_file(filename,encrypted)
        #massage
        print('\nfile encrypted')
        key_ = ''
        for x in key:
            key_ = key_ + '-' + str(x)
        print(f'key = {key_[1:len(key_)]}')
        return key_[1:len(key_)]