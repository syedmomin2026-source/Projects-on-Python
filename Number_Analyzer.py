print("This is a program to analyze the number")

n = int(input("Enter the number:"))

print("What do you want to analyze?")
print("even or odd / positive, negative or zero / prime or composite number")

k = input("Enter your option: ")
l = ["even or odd", "positive, negative or zero", "prime or composite number"]

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
            s = 
            for i in range(1, n + 1):
                if n%i == 1:
                    print("composite number")
                    break
                elif n%i == 0:
                    print("prime number")