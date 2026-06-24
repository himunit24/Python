x=int(input("Enter your number : "))
if x>90 and x<=100 :
    print("Grade-A")
elif x>80 and x<=90 :
    print("Grade-B")
elif x>70 and x<=80 :
    print("Grade-C")
elif x>60 and x<=70 :
    print("Grade-D")
elif x>50 and x<=60:
    print("Grade-E")
else : 
    print("Grade-F")

print()
print()
print("Even") if x/2.0==0 else print("Odd")