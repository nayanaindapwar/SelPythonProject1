greeting = "Good Morning"

if greeting == "Good Morning":
    print("Condition Matches")
    print("Second line of IF")
else:
    print("Condition do not match")
print("If-Else condition code is completed")

a = 4
if a > 2:
    print("Condition Matches: a is greater than 2")
else:
    print("Condition do not match: a is less than 2")

# For Loop
obj = [10, 30, 50, 70, 90]
for i in obj:
    # print(i)
    print(i*2)
# Sum of first five natural numbers 1+2+3+4+5 = 15
addition = 0
for j in range(1, 6): # range(i,j) --> i to j-1
    print(j)
    addition = addition +j
print(addition)

for k in range(1, 10, 2):
    print(k)

for m in range(10):
    print(m)

print("While Loop execution")
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1


# Functions
def greetme(name):
    print("Good Morning "+name)


def addintegers(a, b):
    return a+b


print("Function Output")
greetme("Peter Jacob")
print(addintegers(2,3))







