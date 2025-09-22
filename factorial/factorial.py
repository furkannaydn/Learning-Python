def calculatorfactorial(num):
    if num==0:
        return 1
    else:
        return num*calculatorfactorial(num-1)
num=int(input("Enter a number: "))
print(calculatorfactorial(num))   