import math

print("1:plus.\n2:minus\n3:multiply\n4:divide\n5:factorise\n6:square root")
Sign = input("enter sign")

if Sign == "1":
        Num1 = int(input("enter number"))
        Num2 = int(input("enter number"))
        if int(Num1) is not 9 and int(Num2) is not 10:
            Result = int(Num1) + int(Num2)
        if Num1 == 9 and Num2 == 10:
            Result = "21"
if Sign == "2":
        Num1 = int(input("enter number"))
        Num2 = int(input("enter number"))
        Result = int(Num1) - int(Num2)
if Sign == "3":
        Num1 = int(input("enter number"))
        Num2 = int(input("enter number"))
        Result = int(Num1) * int(Num2)
if Sign == "4":
        Num1 = float(input("enter number"))
        Num2 = float(input("enter number"))
        Result = float(Num1) / float(Num2)

if Sign == "5":
    A = float(input("enter a"))
    B = float(input("enter b"))
    C = float(input("enter c"))

    Result1 = (-B + math.sqrt((B * B) - 4 * A * C)) / (2 * A)
    Result2 = (-B - math.sqrt((B * B) - 4 * A * C)) / (2 * A)

if Sign == "6":
    Num1 = float(input("enter number"))
    Result = (math.sqrt(float(Num1)))
\
if Sign == "5":
    print(Result1)
    print(Result2)
if Sign == "1" or Sign == "2" or Sign == "3" or Sign == "4" or Sign == "6":
    print(Result)