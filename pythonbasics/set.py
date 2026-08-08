s1={1,5,8,9}  #hm jis order me element ko store kr rhe hai jaroori ni ki element usi order me store hoga lekin ek
              #baar jis order me ho gya to usi order me rahega
s2={2,2,2,8,8,8,10,93,3,20,9} #hai lekin sotre unique element hi hoga
s3={} #empty set dictionary ban jata hai 
s4=set()
# s5=set(10,20,30) #error dega kyunki set me aise ek hi value pass krskte hai aur same list me hi hoga,,,kul milakr iterable hi 
s5=set(range(10))#put kr skte hai
print(type(s4))  
print(type(s3))
print(s1)
print(s2)
print(s5)


##python program to remove duplicate elemets in list
l1=[10,10,20,30,40,50,20,30,50]
l1=set(l1)
print(l1)

l10=list(set(int(x) for x in input("Enter number separated by comma").split(",")))
print(sorted(l10))

#concatenation and repetetion operator are not allowed in set

#set comprehension
s=input("Enter String : ")
s10={e for e in s if e in "aeiou"}
print(s10)