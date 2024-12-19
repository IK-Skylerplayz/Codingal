def sample2_fun(factorial):
    if factorial ==1:
        return factorial
    else:
        return factorial * sample2_fun (factorial-1)
factorial1=int(input("Enter a number "))
if factorial1 <0:
    print("Sorry the factorial does not exsit for negative numbers")
elif factorial1 ==0:
    print("The factorial of 0 is 1")
else:
  #  print("The factorial of ",factorial1,"is ",sample2_fun(factorial1)) 
    print(f"The factorial of {factorial1} is {sample2_fun(factorial1)}")         
