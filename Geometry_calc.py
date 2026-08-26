print("This is a geometry calculator")
print("Choose 1 for circle, 2 for square, 3 for triangle, 4 for rectangle")
k = int(input("Enter the number:"))

def cr(a):
    if n == "Area":    
        pi = 3.14
        return "Area:", pi*a**2, "meter square"
    elif n == "Perimeter":
        pi = 3.14
        return "Perimeter:", 2*pi*a, "meter"
    
def sq(a):
    if n == "Area":    
        return "Area:", a**2, "meter square"
    elif n == "Perimeter":
        return "Perimeter:", 4*a

def triangle(a, b):
        if n == "Area":
            return "Area:", 1/2 * a * b, "meter square"
        elif n == "Perimeter":
            c = int(input("Enter the third side:"))
            return "Perimeter:", a + b + c

def rec(a, b):
    if n == "Area":
        return "Area:", a*b, "meter square"
    elif n == "Perimeter":
        return 2*(a + b)

s = [1, 2, 3, 4]
l = ["Area", "Perimeter"]

if k not in s:
    print("You chose invalid shape, try by running the code again")

else:
    print("What do you want to calculate?")
    print("Area / Perimeter")
    n = input("Enter the answer: ")
    print("you have choosen", n)
    if n not in l:
        print("you have opted a wrong parameter, try by running the code again")

    else:
        if k == 1:
            a = float(input("Enter the radius of a circle: "))
            print(cr(a))

        elif k == 2:
            a = float(input("Enter the side of a square: "))
            print(sq(a))

        elif k == 3:
                a = float(input("Enter the base: "))
                b = float(input("Enter the height: "))
                print(triangle(a, b))

        elif k == 4:
            a = float(input("Enter the height: "))
            b = float(input("Enter the breadth: "))
            print(rec(a, b))