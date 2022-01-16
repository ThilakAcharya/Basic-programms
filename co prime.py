num = int(input("enter ther num: "))
elem = list(map(int,input("enter elements of array: ").strip().split()))
for i in elem:
    for j in elem:
        if i != j:
            first = i
            second = j
            def are_coprime(a,b):
                hcf = 1

                for i in range(1, a+1):
                    if a%i==0 and b%i==0:
                        hcf = i

                return hcf == 1

            if are_coprime(first, second):
                print('%d and %d are CO-PRIME' %(first, second))
            else:
                print('%d and %d are NOT CO-PRIME' %(first, second))
