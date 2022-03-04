print('Please enter the numbers for the multiplication: ')
n1, n2= input().split()
n1=int(n1)
n2=int(n2)
base=n2
number=n1
if(n1 < n2): 
    base, number=number,base
binaryTable=list(bin(base))[2:]
result=0
i=0
while i < len(binaryTable):
    result+=number*int(binaryTable[i])*(2**(len(binaryTable)-i-1))
    i+=1
print(result)
    

    

