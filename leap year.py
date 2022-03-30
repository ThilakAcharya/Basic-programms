a = True
while a == True:
    status = input("to exit enter exit: ")
    if status.lower() == "exit":
        a = False
    year = int(input("Year: "))
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print(" leap year{}".format(year))
    else:
        print("not leap year{}".format(year))
