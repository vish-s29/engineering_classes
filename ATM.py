#atm stimulator checking balance,withdrawing cash,depositing cash,changing the pin
def main():
    while True:
        print("Hi! welcome to ATM \nwhat would u like to do?")
        print("1.check balance")
        print("2.withdrawing cash")
        print("3.depositing cash")
        print("4.changing the pin")
        print("5.exit")

        c=input("Pls enter ur choice from the above options:")
        if c=='1':
            print(check())
        elif c=='2':
            print(withdraw())
        elif c=='3':
           print(deposit())
        elif c=='4':
         print(change_pin())
        elif c=='5':
             print(ext())
             break
user={
    'pin':"123",
    'balance':1000
 }


y=input("enter pin to go ahead!")
while y!=user['pin']:
    y=input("pls enter correct pin")

def check():
    while True:
        return("the balance amount is:",user['balance'])

def withdraw():
    while True:
        x=int(input("how much cash do u want to withdraw?"))
        if x<=user['balance']:
           user['balance'] = user['balance'] - x
           return("Amount withdrawn:",x,"remaining balance",user['balance'])
        else:
            return ("Insufficient balance")

def deposit():
    while True:
        x=int(input("how much cash do u want to deposit?"))
        if x<=user['balance']:
            user['balance'] = user['balance'] + x
        return("Amount deposited:",x,"remaining balance",user['balance'])

def change_pin():
    user['pin']
    y=input("enter original pin")
    while y!=user['pin']:
        y=input("pls enter correct pin")
    z=int(input("enter the new pincode:"))
    return ("your pincode has changed",z)



def ext():
    return("Thankyou!visit again")

main()


def fun():
     list1 =input("enter list")
     list1 = list1.split(',')
     list1 = [int(i)for i in list1]
     print(list1)
     target =int(input("enter target:"))
     store=[]
     for i in list1:
         store.append(i)
         y= sum(store)
         x= list1[1:len(list1)]
         z=sum(x)
         if y == target:
               print(y,store)
         if z == target:
              print(z,x)
    
fun()
    
   
list1=[1,2,3,4]
store=[]
for i in list1:
    store.append(i)

for j in range(len(store)):
    if store[3]>store[2]:
       store[3],store[2] = store[2],store[3]
       print(i)
      # c=j+1
for c in store:
    x=i
    if store[2]>store[1]:
     store[2],store[1] = store[1],store[2]
     print(j)

##using dictionaries
def fact(n):
    store=[]
    f=1
    for i in range(1,n+1):
       store.append(i)
    for i in store:
        f=f*i
    return f 

def main():
    x=input("enter a list")
    x=x.split(",")
    x=[int(i)for i in x]
    print(x)
    for num in x:
        y=fact(num)
        print(y)

main()

def fact(n):
    result = 1     
    while n >0:         
        result *= n      
        n-=1              
    return result  
y=fact(3)
print(y)

#for multiplying by defining the function and executing after the function
def click(num):
    c = ""
    for i in range(11):
        #c += f"{num} * {i} = {num * i}\n"
    #return c
       c += f"{num * i}\n"
    return(c)
    
y=click(2)
print(y)