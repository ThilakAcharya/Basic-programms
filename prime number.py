while True:
    num = int(input("enter the number: "))
    i = 1
    if num > 0:
        for j in range(2,num):
            if num % j == 0:
                i = 0
                
        if i == 1:
            print(str(num) + " is  prime")
        else:
            print(str(num) + " is not prime")
