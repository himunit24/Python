def remove_from_list(l1,key) :
    i=0
    while i<len(l1) :
        if l1[i]==key :
            l1.remove(key)
        i+=1
    print(l1)
remove_from_list([1,5,3,5,6,6,4,4,6,44],44)