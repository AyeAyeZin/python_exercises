i=0
numbers=[]
while i<6:
    print(f"At the top i is {i}")
    numbers.apend(i)
    i=i+i
    print("Numbers now:",numbers)
    print(f"At the bottom i is {i}")
print("The numbers:")
for num in numbers:
    print(num)

