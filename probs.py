def main():
    # prob1()
    # prob2()
    #prob3()
    prob4()





#Create a function in your program that counts from 0 to [NUMBER]
#
# def prob1():
#
#     counttothis(5)
#
# def counttothis(x):
#     for num in range(0, x):
#         print(num)


#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
#
# def prob2():
#
#     askUser = input("Where do you like to eat?")
#
#     while askUser.lower() != "q":
#          askUser = input("Where else do you like to eat?")
#
#




#Create 4 functions called add, subtract, multiply, and divide.
#Create them to allow a user to perform the name of the function
# to the two numbers and return the result.


# def prob3():
#
#     num1 = int(input("Enter first number"))
#     num2 = int(input("Enter another number"))
#     print(addThis(num1, num2))
#     print(subtractThis(num1, num2))
#     print(multiply(num1, num2))
#     print(divide(num1, num2))
#
# def addThis(num1, num2):
#     return num1 + num2
#
#
#
# def subtractThis(num1, num2):
#     return num1 - num2
#
#
# def multiply(num1, num2):
#     return num1*num2
#
#
# def divide(num1, num2):
#     return num1/num2




#Create a function that will ask the user for a number.
# Use the function to get two numbers,
# then pass the two numbers to a function and ask a user
# if they want to add, subtract, multiple, or divide them.
# Return a string that prints the two numbers, which operation it did,
# and the result.



def prob4():

    askNum1 = int(input("Enter the first number"))
    askNum2 = int(input("Enter the second number"))

    print(dothisMath(askNum1, askNum2))

def dothisMath(x, y):

    askQuest = input("Do you want to add, subtract, multiply, or divide?")

    if(askQuest == "add"):
       return (x, y, "added", "is", (x + y ))
    elif(askQuest == "subtract"):
        return (x, y, "subtracted", "is", (x - y ))
    elif(askQuest == "multiply"):
        return (x, y, "multiplied", "is", (x*y))
    elif(askQuest == "divide"):
        return (x, y, "divided", "is", (x/y ))


    else:
        print("Error")





















if __name__ == '__main__':
    main()