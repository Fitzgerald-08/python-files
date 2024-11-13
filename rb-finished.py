customer_name = input("What's your name? ").strip().title()

if customer_name == "Ben" or customer_name == "Patricia":
    evil_status = input("Are you evil? ")
    if evil_status == "Yes":
        print("Get lost " + customer_name + ", you are not allowed to come in")
        exit()
    else:
        print("Perfect, you may come in")
else:
    print("Please come in, feel like home")

order = input("What would you like to order?"
              "\n"
              "Latte: $3\n"
              "Espresso: $3.50\n"
              "Americano: $4.50\n"
              "Cappuccino: $5\n"
              "Black Coffee: $5:\n").title()

latte = int(3)
espresso = int(3.50)
americano = int(4.50)
cappuccino_and_blackCoffee = int(5)

if order == "Latte":
    quantity = int(input("How many would you like to order? "))
    print("Thanks for your order, it will come to " + str(
        quantity * latte) + " and it will be ready in just a few minutes.")
elif order == "Espresso":
    quantity = int(input("How many would you like to order? "))
    print("Thanks for your order, it will come to " + str(
        quantity * espresso) + " and it will be ready in just a few minutes.")
elif order == "Americano":
    quantity = int(input("How many would you like to order? "))
    print("Thanks for your order, it will come to " + str(
        quantity * americano) + " and it will be ready in just a few minutes.")
elif order == "Cappuccino" or order == "Black Coffee":
    quantity = int(input("How many would you like to order? "))
    print("Thanks for your order, it will come to " + str(
        quantity * cappuccino_and_blackCoffee) + " and it will be ready in just a few minutes.")
else:
    print("Sorry, we either do not serve " + "'" + order + "'" + " or you mistyped your order.")
