x = 10

while x > 1:
    if x == 9:
        x = x-1
        continue
    if x == 3:
        break
    print(x)
    x = x - 1

print("------------------------")

time = 11.5

if 5<= time <=11:
    print("Good Morning")
elif 11< time <=17:
    print("Good Afternoon")
elif 17< time <=23:
    print("Good Evening")
else:
    print("Good Night")

print("--------------------------------")

for i in range(10):
    print(i)

print("----addition of two numbers----")

def addition(a, b):
    return a+b

value = addition(10, 15)
print(value)
