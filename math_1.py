#VIDEO #1

#print('This is once again an attempt to become a Software Developer, hopefully it will not end in failure')

#print('''First, i need to grasp the basics of this language and little by little,
#try to get deper into more complex concepts''')

#print('I will repeat 20 times to my self the following line but i will probably need more\n' +
#      'I CAN DO THIS!!\n' * 20)

#print('''As you can see i already put into practice what i have learned in a youtube video, i will come back, create
#another file and practice more''')


#VIDEO #2

#print("The following function takes input from the user, and it can be stored to do something with it")

#name = input("What is your name?\n")

#print("Hello " + name + ", i hope your road to becoming a Software Developer works out well, really well...")


#VIDEO #3

user = "Fitzgerald"
age = 21
actual_age = 21.80

math = 5 * 7 ** 2

results = age + actual_age + math


#CHALLENGE #1

customer_name = input("What's your name? ")

if customer_name == "Ben" or customer_name == "Patricia":
    evil_status = input("Are you evil? ")
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and good_deeds < 4:
        print("You are not welcome here Evil " + customer_name + "!! Get out of here")
        exit()
    else:
        print("Hello " + customer_name + ", thank you so much for coming in today!!")

coffee_price = 8

menu = input(customer_name + ", What would you like to order\n" +
             "Latte, Americano, Cappuccino, Espresso (They all cost $8)\n")

quantity = input("How many would you like to order? ")

total = int(quantity) * coffee_price

print("Thank you, the total is: $" + str(total) + ", you'll have your " + quantity + " " + menu + "s ready for you in a moment")


#VIDEO #4

