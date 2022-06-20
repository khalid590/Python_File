# 1 + 2 + 3 + .... + n

# n = int(input("Enter the number: "))
#
# sum = 0
#
# for x in range(1,n+1,1):
#     sum = sum + x
#     print(sum)

# 1^2 + 2^2 + 3^2 + ...... n^2

n = int(input("Enter the number: "))
sum = 0

for x in range(1,n+1,1):
    sum = sum + x*x
    print(sum)
