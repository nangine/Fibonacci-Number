

def fib(s):
    if s <= 0:
        return ["Should be positive number"]
    if s == 1:
        return[0]
    der=[0,1]
    if s == 2 :
        return der
    for i in range (2,s):
        der.append(der[i-1]+der[i-2])
    return der
            
opt="y"
while opt=="y":
    s=int(input("Insert term = "))
    print ("Fibonacci Series = ",list(fib(s)))
    opt = input ("Continue ? y/t -> ")
    print ()
    
print ("***selesai***")
