from validators import *
class Car:
    def __init__(self , car_name , car_price , car_type , car_model):
        self.car_name = car_name
        self.car_price = car_price
        self.car_type = car_type
        self.car_model = car_model
    def __str__(self):
        return f"NAME CAR : {self.car_name}\nPRICE CAR : {self.car_price}$\nTYPE CAR : {self.car_type}\nMODEL CAR : {self.car_model}\n"

list_car = []
def add_car():

    print("\nOK\n")
    name = input("ENTER NAME CAR :")
    price = check_value_price()
    typee = input("\nENTER TYPE CAR : ")
    model = check_value_model()
    print("\nCOMPLETE ADD ✅\n")
    list_car.append(Car(name , price , typee , model))


def view_cars():
    if list_car:
        for i,j in enumerate(list_car):
            print(f"\n>>>>>>> {i+1} <<<<<<<")
            print(j)



def modify_car():
    view_cars()
    while True:
        try:
            number_car = int(input("\nPLEASE ENTER CAR NUMBER : "))
        except ValueError:
            print("PLEASE ENTER A NUMBER ❌")
            continue
        if number_car < 1 or number_car > len(list_car):
            print("CAR NOT FOUND ❌ ")
            continue
        else:
            while True :
                modifying = input("WHAT DO YOU WANT MODIFYING ( NAME , PRICE , TYPE , MODEL ) : ").lower()
                if modifying == "name":
                    new_name = input("\nENTER NEW NAME : ")
                    list_car[number_car-1].car_name = new_name
                    print("\nCOMPLETE MODIFYING NAME ✅\n")
                    break
                elif modifying =="price":
                    new_price = check_value_price()
                    list_car[number_car-1].car_price = new_price
                    print("\nCOMPLETE MODIFYING PRICE ✅\n")
                    break
                elif modifying == "type":
                    new_type = input("ENTER NEW TYPE : ")
                    list_car[number_car-1].car_type = new_type
                    print("\nCOMPLETE MODIFYING TYPE ✅\n")
                    break
                elif modifying == "model":
                    new_model = check_value_model()
                    list_car[number_car-1].car_model = new_model
                    print("\nCOMPLETE MODIFYING MODEL ✅\n")
                    break
                else:
                    print("\nPLEASE ENTER ---->> ( NAME , PRICE , TYPE , MODEL ) \n")
            break


def start():
    while True:
        try:
            services = int(input("SELECT THE SERVICE NUMBER :\n1- ADD CAR\n2- MODIFYING CAR INFORMATION\n3- VIEW ALL CARS\n4- EXIST\n>>"))
        except ValueError:
            print("\nPLEASE ENTER A NUMBER ❌\n")
            continue
        if services == 1:
            add_car()
        elif services == 2 or services == 3:
            if list_car:
                if services == 2:
                    modify_car()
                elif services== 3 :
                    view_cars()
            else:
                print("\nNO CARS AVAILABLE ❌\n")
        elif services == 4 :
            print("\nTHANK YOU FOR USING MY APP 🌟\n")
            break
        else:
            print("\nINVALID SERVICE NUMBER ❌\n")

start()