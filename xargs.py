def add (*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
        print(sum, end = ' ')

add(10, 20)
add(40,50,60)
add(10,40,60,80)
