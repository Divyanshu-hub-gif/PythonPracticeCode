# global keyword is used to modify the global variables

x=10
def sum(a,b):
    print("Hi i am summing ")
    c=a+b
    global z #please modify this global z
    z=0 #this will modify the global variable z and create a local variable inside the fucntion
    return c

z=3
print(sum(12,12))
print(z)