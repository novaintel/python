#1+1 = 2
#1+2 = 3
#2+3 = 5
#3+5 = 8

count = 0
previousSum = 0
sum = 1

totalSum = 0

while sum < 4000000:
    count = previousSum
    previousSum = sum
    sum = count + previousSum
    if sum % 2 == 0:
        print(str(sum))
        totalSum += sum
    #print(str(sum))
print("The total sum is: " + str(totalSum))