#--init--()
class test :
    x=5
    y=6
    def __init__(self) :
        self.a=4          #without self a is local variable but with self.a it becomes instance object variable
        print(a)
t1=test()  #init automatically call ho gya jiske andar t1 pass hua
t2=test()
