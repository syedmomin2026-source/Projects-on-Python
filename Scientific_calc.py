'''PROJECT 01'''

print("This is a scientific calculator for any two numbers")
print("Choose the operation: addition / subtraction / multiplication / division / power / remainder")
k = input("Choose which operation do you want to use:")

if k != "addition" and k != "subtraction" and k != "multiplication" and k != "division" and k != "power" and k != "remainder":
    print("You have opted the wrong operation, try by running the code again")

else:
    print("you have choosen", k)
    print("Choose any two numbers:")
    a = float(input ("1st number:"))
    b = float(input("2nd number:"))

    def add(a, b):
        c = a + b
        return c
    
    def sub(a, b):
        c = a - b
        return c

    def mul(a, b):
        c = a*b
        return c

    def div(a, b):
        if b == 0:
            c = "Not difined"
        else:
            c = a/b
        return c

    def power(a, b):
        c = a**b
        return c

    def remainder(a, b):
        if b == 0:
            c = "Not Defined"
            return c
        else:
            c = a%b
            return c

    if k == "addition":
        j = add(a, b)

    elif k == "subtraction":
        j = sub(a, b)

    elif k == "multiplication":
        j = mul(a, b)

    elif k == "division":
        j = div(a, b)

    elif k == "power":
        j = power(a, b)

    elif k == "remainder":
        j = remainder(a, b)

    print("the", k, "of two numbers:", j)