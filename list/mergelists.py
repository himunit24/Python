def merglist(l1,l2) :
    i,j=0,0
    merge=[]
    while i < len(l1) and j<len(l2):
        merge.append(l1[i])
        i+=1
        merge.append(l2[j])
        j+=1
    if len(l1)>len(l2) :
        for a in range(len(l2),len(l1) ) :
            merge.append(l1[a])
    else :
        for a in range(len(l1),len(l2)) :
            merge.append(l2[a])

    print(merge)

merglist([1,2],[4,5,6])