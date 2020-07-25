from tinydb import TinyDB
db = TinyDB('tryal.json')
dictionary = {"firstName":"Munene","secondName":"Muondu","age":11}
def adding_person():
    name1 = input("Enter your first name:  ")
    name2 = input("Enter your second name:  ")
    age = input("Enter your age:  ")
    updating_dict = {"firstname":name1,"secondName":name2,"age":age}
    dictionary.update(updating_dict)
    db.insert(dictionary)
adding_person()