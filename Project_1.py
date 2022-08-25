def my_function(a, b,):
    sum=a+b
    return sum
def return_max_numbers(a,b ):
    max=0
    if a>b:
        max=a
    else:
        max=b
    return max




a=input("enter number a ")
b=input("enter number b ")
a= int(a)
b= int(b)
#r=my_function(a,b)
#r=return_max_numbers(a,b)
#print(r)

op = input("what do you want to do ? sum or max ; for sum enter sum , for max enter max ")
if op == "sum":
    r=my_function(a,b)
    print(f"sum = {r}")
elif op == "max":
    r=return_max_numbers(a,b)
    print(f"max ={r}")
else :
    print("wrong operation")







