# n = input("Enter the numbers: ")
#
# list = n.split()
#
# sum = 0
#
# for num in list:
#     sum = sum + int(num)
#
#     print(sum)

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a text of numbers:  ")  #My name is Khalid123

for x in text:
    x = x.lower()

    if x >= 'a' and x <= 'z':
        numOfLetters = numOfLetters + 1

    elif x >= '0' and x <= '9':
        numOfDigits = numOfDigits + 1

    elif x == ' ':
        numOfWords = numOfWords + 1

print("Number of Letters = ",numOfLetters)
print("Number Of Digits = ",numOfDigits)
print("Number of words = ",numOfWords)




