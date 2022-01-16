a = True
while a == True:
    status = input("to exit enter exit: ")
    if status.lower() == "exit":
        a = False
    year = int(input("Year: "))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            print("not leap year")
        else:
            print("leap year")
