# try except else finally and raise are thee exceptionss

a=int(input("Enter a : "))
b=int(input("Enter b : "))

try :
    print(a/b)
except Exception as err :
    print("Error ocurred",err) #or
    print(f"Error ocurred {err}")
else :
    print("There was no error")
finally :
    print("I will execute no matter what !!")
print(a+b)

#for raise we can give manual errors 

try :
    x=int(input("Enter your age :"))
    if x <18 :
        raise Exception("You must be 18 or above 18")
    print("Acess granted")
except  Exception as err :
    print("Error ocurred : ",err)