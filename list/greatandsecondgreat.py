def maximumm(l1) :
    max=float("-inf")
    secmax=float("-inf")
    for i in l1 :
        if i>max :
            secmax=max
            max=i
        elif i>secmax and i!=max :
            secmax=i
    print(max,secmax)
maximumm([10,10,5])
            