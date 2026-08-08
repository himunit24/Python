def subarray(l1) :
    null_list=[]
    for i in range(len(l1)) :
        null=[]
        for j in range(i+1,len(l1)) :
            null_list.append(l1[i:j+1])
    print(null_list)

subarray([1,2,3])

