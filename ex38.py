ten_things="Apples Oranges Crows Tekephone Light sugar"
print("Wait there are not 10 things in that list. Let's fix that.")
stuff=ten_things.split(' ')
more_stuff=["Days", "Night", "Song", "Frisbee",
        "Corn", "Banana", "Girl", "Boy"]
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(nest_one)
    print(f"there are {len(stuff)} items now.")
print("Ther we go: ",stuff)
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
