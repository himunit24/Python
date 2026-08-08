def unique(l1) :
    check=[]
    for i in l1:
        if i in check :
            continue
        else :
            check.append(i)
    print(check)
unique([1,2,33,33,1,2,2,3])


#### we can also use set for this