function is a block of code that performs a specific task and can be reused throughout a program
Functions help to organize code, make it more readable, and reduce redundancy.
They can take inputs (parameters), perform operations, and return outputs (results). 
In Python, functions are defined using the `def` keyword followed by the function name
and parentheses.

def avg():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    average=(a+b+c)/3
    print(average)

avg()
print("thank you")
avg()
print("thank you")
avg()
print("thank you")
avg()
avg()
avg()
avg()
avg()


function with parameters
def hello(name, ending):
    print("Hello " + name + "!")
    print(ending)
hello("Alice", "Have a great day!")
hello("Bob", "See you later!")
hello("Charlie", "Goodbye!")

def hello(name, ending):
    print("Hello " + name + "!")
    print(ending)
    return "Function completed!"
a=hello("Alice", "Have a great day!")
print(a)




function using recursion:
n=int(input("Enter a number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(n))




def fabonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_number)
        return fib_sequence


n = int(input("Enter the number of terms for Fibonacci sequence: "))
print(fabonacci(n))

def fabonacci(n):
    a=0
    b=1
    for i in range(n):
        sequence.append(a)
        a=b
        b=a+b
        return sequence
n = int(input("Enter the number of terms for Fibonacci sequence: "))
print(fabonacci(n))
