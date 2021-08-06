import os
import pyAesCrypt as pya
print("Скрипт шифрует файлы")
print("--------------------")
zzz = input("Введите: 1- для шифрования, 2 - для дешифрования: ")
d=input("Введите каталог: ")
password=input("Введите пароль: ")
ff=0
dd=0
def criptik (file_name):
    global password
    buff = 512*1024
    pya.encryptFile(str(file_name), str(file_name) +".aes", password, buff)
    os.remove(file_name)

def decriptik (file_name):
    global password
    buff = 512*1024
    pya.decryptFile(str(file_name), str(os.path.splitext(file_name)[0]), password, buff)
    os.remove(file_name)


if zzz == "1":
    for dirpath, dirnames, filenames in os.walk(d):
        # перебрать каталоги
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
            dd+=1
        # перебрать файлы
        for filename in filenames:
            	print(os.path.join(dirpath, filename))
            	criptik(os.path.join(dirpath, filename))
            	ff+=1

elif zzz == "2":  
    for dirpath, dirnames, filenames in os.walk(d):
        # перебрать каталоги
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
            dd+=1
        # перебрать файлы
        for filename in filenames:
            if "aes" in filename:
                print(os.path.join(dirpath, filename))
                decriptik(os.path.join(dirpath, filename))
                ff+=1


print("DONE")