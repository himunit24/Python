d1={1:'A',2:'B',3:'C',4:'D',5:'E'}
d2={} #empty dictionary
d3=dict(r='Ram',s='Shambhu') # we can not do dict(1:'Ram',2:'Shambhu') hm aise dictionary declare krte waqt constant ni likh skte
print(d1)
print(d2)
print(d3)
print(d1[1],d1[2],d1[5]) # 1,2 and 5 are keys we use keys to access
print()
for i in d1 :       # i will print keys
    print(i,":",d1[i])
d1[6]='F'
d1[4]='X'
print(d1)
print("-----------------")
print(d1.keys())
print(d1.values())
print(d1.items())

print("------------")
for i in d1.items() :
    print(i[0],i[1])
print("-----------------------")
print("WE CAN USE THE CONCEPT OF UNPACKING")

for k,d in d1.items() :
    print(k,d)