#Author: Bryan Soares

# Trying to make a simple calculator program 
# I'm still learning the basics of python 

while True:
    first = input("Input the first number ")
    second = input("input the second number ")
    choose = input("Choose the operations: Addition, Multiply, or division ").strip().lower()

    second =  int(second)
    first = int(first)


    while choose not in ("addition", "multiply", "division"):
        print("Choose a valid option")
        choose = input("Addition, Multiply, or divison ").strip().lower()


    if choose == "addition":
        result1 = first + second
        print(f"{first} + {second} = " + f"{int(result1)}")

    elif choose == "multiply":
         result2 = first * second
         print(f"{first} * {second} = " + f"{int(result2)}")
 

    elif choose == "division":
        result3 = first / second
        print(f"{first} * {second} = " + f"{float(result3)}")



    again = input("Do you want to go again (Y/N)").strip().lower()
    if again != "Y":
        print("Closing..")
        break 
    else:
        continue




