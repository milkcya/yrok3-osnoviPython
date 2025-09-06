import os
from cryptography.fernet import Fernet

def write_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)

def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

write_key()

f = Fernet(load_key())

def add():
    name = input("Логин: ")
    password = input("Пароль: ")
    encrypted_password = f.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as file:
        file.write(f"{name}|{encrypted_password}\n")

def view():
    if not os.path.exists('passwords.txt'):
        print("Файл с данными не найден.")
        return
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            decrypted_password = f.decrypt(passw.encode()).decode()
            print(f"Логин: {user} | Пароль: {decrypted_password}")

while True:
    mode = input("1. Посмотреть; 2. Добавить; 3. Выйти: ")
    if mode == "1":
        view()
    elif mode == "2":
        add()
    elif mode == "3":
        break
    else:
        print("Неверный ввод.")