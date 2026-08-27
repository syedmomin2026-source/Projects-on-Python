print("This is a program to analyze the number")

n = int(input("Enter the number:"))

print("What do you want to analyze?")
print("even or odd / positive, negative or zero / prime or composite number / no. of digits")

k = input("Enter your option: ")
l = ["even or odd", "positive, negative or zero", "prime or composite number", "no. of digits"]

if k not in l:
    print("You chose the wrong option, try by running the code again")

else:
    if k == "even or odd":
        if n%2 == 0:
            c = "even"
            print(c)
        else:
            c = "odd"
            print(c)
    elif k == "positive, negative or zero":
        if n > 0:
            c = "positive"
            print(c)
        elif n == 0:
            c = "equal to zero"
            print(c)
        else:
            c = "negative"
            print(c)
    elif k == "prime or composite number":
            s = 0
            for i in range(1, n + 1):
                if n%i == 0:
                    s += 1
            if n == 0:
                print("It is neither prime nor composite number")
            elif n < 0:
                print("Invalid number")
            elif s == 2:
                print("prime number")
            else:
                print("composite number")

    elif k == "no. of digits":
        s = str(n)
        if n < 0:
            f = len(s) - 1
            print(f)
        else:
            print(len(s))