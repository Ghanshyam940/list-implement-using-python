def f_to_c(f):
    c = (f - 32) * 5/9
    return c
f=int(input("Enter temperature in Fahrenheit: "))
print(f"{f} Fahrenheit is equal to {f_to_c(f)} Celsius.")



def c_to_f(c):
    f = (c * 9/5) + 32
    return f
c=int(input("Enter temperature in Celsius: "))
print(f"{c} Celsius is equal to {c_to_f(c)} Fahrenheit.")