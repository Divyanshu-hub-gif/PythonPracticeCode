age = int(input("enter you age: "))

if(age>18):
    print("You can drive")
elif(age==18):
    print("Lets schdule an interview")
elif(age==0):
    print("You were new born")
else:
    print("Sorry you cannot drive")