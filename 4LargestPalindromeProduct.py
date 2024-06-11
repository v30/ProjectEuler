# what is a palindrome? A number which reads the same from both directions eg: 900009

# we need to find the largest palindrome made of 3 digit numbers

num1 = 999
num2 = 999
test = 0
listResult = []


# function to reverse a string
def reverse(x):
    return x[::-1]


for x in range(num1, 0, -1):
    for y in range(num2, 0, -1):
        test = x * y
        strResult = str(test)
        # compare the result with the reverse result to see if it reads the same from both directions
        if strResult == reverse(strResult):
            # if it reads the same add to a list as integer for sorting
            listResult.append(int(strResult))

# sort the list in reverse order to put the largest first
listResult.sort(reverse=True)
print(f'{listResult}')
