from csv import DictReader, DictWriter 
from os.path import exists 

def create_file():
    with open("Phone.csv", "w", encoding = "utf-8") as data:
        f_writer = DictWriter(data, fieldnames = ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    print("Введите фамилию контакта:")
    surname = input("> ")
    print("Введите имя контакта:")
    name = input("> ")
    print("Введите телефон контакта:")
    phone = input("> ")
    info = [surname, name, phone]
    return info

def read_file(file_name):
    with open(file_name, encoding = "utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def write_file(file_name, lst):
    with open(file_name, encoding = "utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    obj = {"Фамилия": lst[0], "Имя": lst[1], "Номер": lst[2]}
    res.append(obj)
    with open("Phone.csv", "w", encoding = "utf-8", newline = "") as data:
        f_writer = DictWriter(data, fieldnames = ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)

def changes_info(file_name):
    info = input("Каком контакте заменить фамилию на 'Быстров'? ")
    with open(file_name, encoding = "utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        for el in res:
            if el['Фамилия'] == info:
                el['Фамилия'] = "Быстров"
    with open("Phone.csv", "w", encoding = "utf-8", newline = "") as data:
        f_writer = DictWriter(data, fieldnames = ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)  

def delet_info(file_name):
    info = input("Какой контакт удалить? Напишите фамилию/имя/телефон: ")
    with open(file_name, encoding = "utf-8") as data:
        f_reader = DictReader(data)
        res = list(f_reader)
        for el in res:
            if el['Фамилия'] == info or el['Имя'] == info or el['Номер'] == info: 
                res.remove(el)                                                                                
    with open("Phone.csv", "w", encoding = "utf-8", newline = "") as data:
        f_writer = DictWriter(data, fieldnames = ['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(res)     
                                         

def main():
    while True:
        command = input("Введите команду: ")
        if command == "q":
            break
        elif command == "r":
            if not exists("Phone.csv"):
                break
            print(read_file("Phone.csv"))   
        elif command == "w":
            if not exists("Phone.csv"):
                create_file()
            write_file("Phone.csv", get_info())
        elif command == "c":
            if not exists("Phone.csv"):
                create_file()
            changes_info("Phone.csv")
        elif command == "d":
            delet_info("Phone.csv")
main()