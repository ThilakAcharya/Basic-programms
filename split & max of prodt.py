def Split(x,a):
    while(a):
        res = 1
        if (a & 1):
            res = res * x
        x = x*x
        a>>=1
    return res
def breakinteage(N):
    if N == 2:
        return
    elif N == 3:
        return
    maxprod = 0
    
