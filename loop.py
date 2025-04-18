#for loop
"""fruits = ['apple','banana','cherry']
for fruit in fruits:
    print(fruit)"""

#while loop
"""i = 1
while i <=5:
    print(i)
    i += 1"""

#nested loop
"""for i in range(1,4):
    for letter in ['A','B','C']:
        print(f"{i}-{letter}")"""

#break statement
"""for i in range(1,6):
    if i == 3:
        break
    print(i)"""

#coninue statement
"""for i in range(1,6):
    if i == 3:
        continue
    print(i)"""

#range-based for loop
"""for i in range(1,6):
    print(i)"""

#enumerate loop
fruits = ['apple','banana','cherry']
for i,fruits in enumerate(fruits):
    print(f"{i}-{fruits}")