from main import load_key
from cryptography.fernet import Fernet
import os


f = Fernet(load_key())

def authorization(username_input, password_input, fernet_obj):
    if not os.path.exists('passwords.txt'):
        return False
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = fernet_obj.decrypt(passw.encode()).decode()
            if username_input == user and password_input == decrypted_password:
                return True
    return False

while True:
    username = input("Введите логин: ")
    password = input("Введите пароль: ")

    if authorization(username, password, f):
        print("Вы авторизованы")
        break
    else:
        print("Такого пользователя нет")
