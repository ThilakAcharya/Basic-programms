#Checking the number whether it  is poer of 2 or not
def powerof2(num):
    temp = num
    lst = []
    while num != 1:
        num = int(num/2)
        print(num)
        if num == 3:
            break
        else:
            lst.append(num)
            continue
    l = len(lst)
    if temp == 2**l:
        print("power of 2")
    else:
        print("not power of 2")
num = int(input("number: "))
powerof2(num)

#printing all the number which is the power of 2 under the specified range
m = True
while m:
    print(" enter the value n to execute\n to exit press e or E")
    n = int(input("n: "))
    if n == 0:
        print("enter valid number")

    elif n > 1:
        lst = []
        for num in range(2,n+1):
            #print("\n number1 :" + str(num))
            temp = num
            #print("\n temp :" + str(temp))
            while num%2 == 0:
                num = int(num/2)
                #print("\n number 2: " + str(num))
                if num == 1:
                    if num == 3:
                        break
                    else:
                        lst.append(temp)
                        continue
        print(lst)
