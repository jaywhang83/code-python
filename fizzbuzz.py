__author__ = 'student'
"""
let the user set the max number that this function iterate
prints "fizzbuzz" if number is multiples of 3 and five.
prints "fizz" if number is multiples of 3
prints "buzz" if number is multiples of 5
"""
def fizzbuzz(arg=100):
    max = arg
    for i in range(1, max):
        if i % 3 == 0 and i % 5 == 0:
            print "fizzbuzz"
        elif i % 3 == 0:
            print "fizz"
        elif i % 5 == 0:
            print "buzz"
        else:
            print i
"""
this function prompts user to enter a number.
then it tells your if the number is multiples of 3, 5, or 3 and five.
If it's not, it displays message that the number is not the multiples of 3, 5 or 3 and 5
"""
def search():
    user_input = int(raw_input("enter a number: ")) # changes the user_input to integer
    if user_input % 3 == 0 and user_input % 5 == 0:
        print str(user_input) + " is multiples of 3 and 5"
    elif user_input % 3 == 0:
        # changes the user_input from integer. Then concatenate with other string to print out. 
        print str(user_input) + " is multiples of 3"
    elif user_input % 5 == 0:
        print str(user_input) + " is multiples of 5"
    elif user_input % 3 !=0 or user_input % 5 != 0 or user_input % 3 == 0 and user_input % 5 == 0:
        print str(user_input) + " is not a multiples of 3, 5 or 3 and 5"

#ask user to set the max range of number to be iterated
def menu():
    ask_max = int(raw_input("Set max number: "))
    fizzbuzz(ask_max)
    # pompts user if they want to continue. If "yes" code runs the loop again. if "no", exits the code.
    while True:
        search()
        ask = raw_input("do you want to continue? ")
        if ask == "no":
            print"goodbye"
            exit()
menu()



