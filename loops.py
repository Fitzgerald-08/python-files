def main():
    name = get_name()
    placing_order()


def get_name():
    fname = input("What's your name? ")
    if fname == "Ben" or fname == "Patricia":
        evil_status = input("Are you evil? ")
        if evil_status == "Yes":
            print("YOU SHALL NOT PASS!!")
            exit()
        else:
            print("Welcome, please come on in")
    


def placing_order():
    while True:
        order = input("What would you like to order? "
                      "\n"
                      "Latte: $4\n"
                      "Espresso: $4.75\n"
                      "Americano: $5.50\n"
                      "Cappuccino: $6\n"
                      "Black Coffee: $6\n").title().strip()
        
        if order == "Latte":
            quantity = int(input("How many would you like to order? "))
            print("Perfect, your order has been placed, and it comes to a total of " + str(quantity * 4))
            break
        elif order == "Espresso":
            quantity = int(input("How many would you like to order? "))
            print("Perfect, your order has been placed, and it comes to a total of " + str(quantity * 4.75))
            break
        elif order == "Americano":
            quantity = int(input("How many would you like to order? "))
            print("Perfect, your order has been placed, and it comes to a total of " + str(quantity * 5.50))
            break
        elif order == "Cappuccino" or order == "Black Coffee":
            quantity = int(input("How many would you like to order? "))
            print("Perfect, your order has been placed, and it comes to a total of " + str(quantity * 6))
            break
        else:
            print("Sorry, i couldn't understand what you said, you either mistyped a word or we do not serve " + "'" + order + "'" + " here.")
            continue


main()