def fibonacci(num):
    if num==1 or num==2: #these are our base cases
        return 1
    elif num==0: #Fn of zero is zero
        return 0
    else: #to compute Fn, you add Fn-1 and Fn-2
        fn1= fibonacci(num-1) #use a recursive algorithm to get Fn-1 and Fn-2
        fn2=fibonacci(num-2)
        Fn=fn1+fn2 #add the resulting values together and return the result
        return Fn
    
#print(fibonacci(5)) driver code, making sure the function works

userNum=input("Please enter an integer ")
while userNum.isdigit()==False: #use the isdigit method to make sure an integer number was input
    userNum=input("Invalid input, please try again ")
print("The value at that position in the Fibonacci sequence is", fibonacci(int(userNum)))

