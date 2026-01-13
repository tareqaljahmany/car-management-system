def check_value_price():
    while True :
        try :
            price = float(input("\nENTER PRICE CAR :"))
            return price
        except ValueError:
            print("\nPLEAES ENTER NUMBER ❌\n")
def check_value_model( ):
    while True :
        try :
            model = int(input("\nENTER MODEL CAR : "))
            return model
        except ValueError:
            print("\nPLEAES ENTER NUMBER ❌\n")