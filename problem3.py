# n=int(input("enter a number "))
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
#     print(sum)


n = int(input("enter a number"))
product=1
for i in range(1,n+1):
    product=product*i
    print(f"the factorial of a {n} is {product}")