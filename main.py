from tinydb import TinyDB, Query
db = TinyDB('main.json')
User = Query()
def activite():
    global activites
    activites = input("""
    Hi. These are the activities that are available.
    a Add someone
    b See everyone    
    c Remove someone


        """)

activite()
dictionary = {"firstName":"Nesh","secondName":"Mothema","age":11}

if activites == "a" or activites == "Add someone" or activites == "a Add someone":
    def adding_person():
        name1 = input("Enter your first name:  ")
        name2 = input("Enter your second name:  ")
        age = input("Enter your age:  ")
        
adding_person()
elif activites == "b" or activites == "See everyone" or activites == "b See everyone":
    def reading_file():
        results = db.search(User.firstName)
        results2 = db.search(User.secondName)
        results3 = db.search(User.age)
        print(results, results2, results3)
        activite()
    reading_file()
elif activites == "c" or activites == "Remove someone" or activites == "c Remove someone":
    def removing_someone():
        removename1 = input("Enter the first name of the person to be removed:  ")
        removename2 = input("Enter the second name of the person to be removed:  ")
        removeage = input("Enter the age of the person to be removed:  ")
        db.remove(User.firstName == removename1)       
        db.remove(User.secondName == removename2)       
        db.remove(User.age == removeage)       
        activite()
    removing_someone()
else:
    print("You have inputed the wrong input. Please try again")
    activite()