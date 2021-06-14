# the print function allows us to preview our work

print("Hello world!")
print("Goodbye world!")
print ("iosvaldo am a software engineer at Apple Inc.")
print(10 * 5/2)

# basic variable and assigning it a value

name = "Alice"
print( "Hello" , name)

#Input function allows us to grab some information from our users

name = input("Hi, what's your name? ")
age = int(input("How old are you? "))

# we are also using conditional if statment

if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)

#Types of Errors in Python
    
# syntax error
# print("Hello world")

# runtime error
# 10 * (2/0)

# semantic error
# name = "Alice"
# print("Hello name")

age = 36
print(age)

#type function tells us what data type is begin used

print(type(age))

email_address = "John.Smith@email.com"
print(email_address)

print(type(email_address))

# mixing the order of the print function builds strength in your programming.

cookies = 'Sugar'
print(cookies)
print(type(cookies))

cookies = 1
print(cookies)
print(type(cookies))

Cookies = 3
print(Cookies)
print(cookies)

first_name = "Jeff"
print(first_name)

first_Name = "Sara"
print(first_name)

#Conditional if-else statments

print("Hi!")
name = input("What's your name? ")
print("It's nice to meet you,", name)
answer = input("Are you enjoying the day? ")
if answer == "Yes":
    print("That's good to hear!")
else:
    print("Oh no! That makes me sad!")

    #Challange 1: carefully look at the code and in tsequential order, write down what you think will print.

    print("Challenge 1:")

# A message for the user
message = "This is going to be tricky ;)"
Message = "Very tricky!"
print(message) # show the message on the screen

# Perform mathematical operations
result = 2**3
print("2**3 =", result)
result = 5 - 3
#print("5 - 3 =", result)

print("Challenge complete!")

#If-Else Statments

plant = "Irises"

if plant == "Cacti":
    print(plant, "don't need a lot of water")
else:
    print(plant, "love water")

print("Thanks!")


#Input function with If-Else statments

favfood = input("What's my favorite food? ")

if favfood == "cookies":
    print("Yep! So amazing!")
else:
    print("Yuck! That’s not it!")

print("Thanks for playing!")


#Prefunction

print("~~~ The Shimmy ~~~")

print("Take one step to the right and stomp.")
print("Take one step to the left and stomp.")
print("Shake those hips!")

print("Take one step to the right and stomp.")
print("Take one step to the left and stomp.")
print("Shake those hips!")

print("Take one step to the right and stomp.")
print("Take one step to the left and stomp.")
print("Shake those hips!")

#Functions are contain all the instructions so we dont have to repeat them, Then we just call the function name as many times as we like. 

print("~~~ The Shimmy ~~~")

def shimmy():
    print("Take one step to the right and stomp.")
    print("Take one step to the left and stomp.")
    print("Shake those hips!")

shimmy()
shimmy()
shimmy()


# Another Function Example, greet your user!.

def say_hello():
    print("Hello, friends!")

say_hello()


#Another If statment program

def wash_car(amount_paid):
    if (amount_paid == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")
   
    if (amount_paid == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry") 

wash_car(12)


#Functions that return a value.

def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance - amount
        return current_balance

balance = withdraw_money(100, 80)

if (balance <= 50):
    print("We need to make a deposit")
else:
     print("Nothing to see here!")


#prints out the name of a favorite city

def favorite_city(name):
  print("One of my favorite cities is", name)

favorite_city("Seattle, Washington")
favorite_city("New York, New York")
favorite_city("Sydney, Australia")
