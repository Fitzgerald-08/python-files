customer_name = input("Hi, what's your name? ")

if customer_name == "Ben":
    evil_status = input("Are you the evil Ben? ")
    if evil_status == "Yes":
        print("Sorry, you shall not pass!!")
    elif evil_status == "No":
        order = input("Perfect, you may come on in, What would you like to order? \n"
                      "(1)Latte $8\n"
                      "(2)Espresso $7.50\n"
                      "(3)Americano $8.50\n"
                      "(4)Cappuccino $7\n"
                      "(5)Black Coffee $6.50\n")

    coffee_1 = 8
    coffee_2 = 7.50
    coffee_3 = 8.50
    coffee_4 = 7
    coffee_5 = 6.5

    if order == 1:
        price = coffee_1
    elif order == 2:
        price = coffee_2
    elif order == 3:
        price = coffee_3
    elif order == 4:
        price = coffee_4
    elif order == 5:
        price = coffee_5

        quantity = input("How many would you like? ")

        total = int(quantity) * price

        print("Thank you, the total is" + str(total) + ", your order will be ready in a moment")

else:
    order = input("Welcome " + customer_name + ", what would you like to order? (Select the option)\n"
                                               "(1)Latte $8\n"
                                               "(2)Espresso $7.50\n"
                                               "(3)Americano $8.50\n"
                                               "(4)Cappuccino $7\n"
                                               "(5)Black Coffee $6.50\n")

    price = 5

    quantity = input("How many would you like? ")

    total = int(quantity) * price

    print("Thank you, the total is " + str(total) + ", your order will be ready in a moment")
