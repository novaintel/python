result = 0
for i in range (1,1000, 1):
    if(i % 3 == 0 or i % 5 == 0):
        result += i
print(f"The sum of the all multiples of 3 and 5 is: {result}")        