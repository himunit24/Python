def freq(t1) :
    i,j=0,0
    for i in range(len(t1)) :
        count=1
        for j in range(i+1,len(t1)) :
            if t1[i]==t1[j] : 
                count+=1 
        print(t1[i],count)
        
freq((6 ,10 ,20 ,10 ,30, 20, 10))         