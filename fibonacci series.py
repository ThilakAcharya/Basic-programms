def fib(n):
    lst = [0,1]
    for i in range(2,n+1):
        value = lst[-1] + lst[-2]
        lst.append(value)
    return lst
lst = fib(int(input("range: ")))
print(lst)

print("another way of doing this is swapping")

n1 =0
n2 = 1
count = 0
n = int(input("entr last number "))
if n <= 0:
    print("enter proper value")
elif n ==1:
    print(n1,n2)
else:
    while count < n+1:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count+=1
