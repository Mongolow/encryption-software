import random
# -*- coding: utf-8 -*-
class Cipher:
    def __init__(self):
        pass
    def encrypt(self,filename):
        #file bytes read 
        with open(filename,'rb') as file:
            file_content = file.read()
        #key generation
        key = []
        for x in range(0,20):
            key.append(random.randint(1,10))
        #file encrypt
        counter = 0
        encrypted = bytearray()
        for char in file_content:
            char = char + key[counter]
            encrypted.append(char % 256)
            counter += 1
            if counter > len(key) - 1:
                counter = 0
        #changing file
        with open(filename,'wb') as file:
            file.write(encrypted)
        #massage
        print('file encrypted')
        key_ = ''
        for x in key:
            key_ = key_ + '-' + str(x)
        print(f'key = {key_[1:len(key_)]}')
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
            char = char - int(key[counter])
            decrypted.append(char % 256)
            counter += 1
            if counter > len(key) - 1:
                counter = 0
        #changing file
        with open(filename,'wb') as file:
            file.write(decrypted)
        print('file decrypted')





x = Cipher()
#x.encrypt('Zrzut ekranu 2025-12-23 202732.png')
x.decrypt('Zrzut ekranu 2025-12-23 202732.png','1-8-6-1-5-9-6-9-8-8-9-7-8-3-7-9-5-3-9-8')


