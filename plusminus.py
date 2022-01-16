def plusMinus(arr):
    # Write your code here
    zero_count = 0
    pos_count = 0
    neg_count = 0
    for i in arr:
        if i == 0:
            zero_count = zero_count + 1
        elif i < 0:
            neg_count = neg_count + 1
        if i > 0:
            pos_count = pos_count + 1
    print(round(zero_count/len(arr),len(arr)))
    print(round(neg_count/len(arr),len(arr)))
    print(round(pos_count/len(arr),len(arr))) 


if __name__ == '__main__':
    n = int(input("n: ").strip())

    arr = list(map(int, input("elem: ").rstrip().split()))

    plusMinus(arr)
    
    
