print("Welcome")
print("Note: You can perform only basic operations only")
x=int(input("Enter the value of X: "))
y=int(input("enter the value of Y: "))

O=int(input("Select option 1 to 5 for below operations \n 1.Addition \n 2.Substraction \n 3.Multiplication \n 4.Division \n and select 0 for all the operations : "))

if (O==0):
    print("\n","Addition :", x+y, "\n" ,"Substraction: ",x-y, "\n","Multiplication: ",x*y,"\n","Division: ",x/y,"\n")
elif (O==1):
    print("Addition of x and y is :", x+y)
elif (O==2):
    print("Substraction of x and y is :", x-y)
elif (O==3):
    print("Multiplication of x and y is :", x*y)
elif (O==4):
    print("Devision of x and y is :", x/y)
else:
    print("Selected a wrong option")
Print("Thank you for using a basic Calculator :)")
