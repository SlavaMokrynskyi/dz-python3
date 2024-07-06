def showText():
    print('''\033[90m"Don't compare yourself with anyone in this world…\n\033[91mif \033[97myou \033[91mdo so\033[97m, you are insulting yourself.\033[90m"\n\033[97mBill Gates"''')
    
showText()

def showEven(start, end):
    for i in range(start, end):
        if i %2 == 0:
            print(i)

showEven(1, 100)

def showSquare(length, symbol, isFilled):
    how_much_space = length - 2
    space = length - 1
    if isFilled == True:
        for i in range(length):
            print(symbol*length)
    elif isFilled == False:
        print(symbol*length)
        for i in range(how_much_space):
            print(symbol," " * space,symbol)
        print(symbol*length)

showSquare(5, "% ", True)



def findMin(num1,num2,num3,num4):
    if num1 < num2 and num1 < num3 and num1 < num4:
        return num1
    if num2 < num1 and num2 < num3 and num2 < num4:
        return num2
    if num3 < num2 and num3 < num1 and num3 < num4:
        return num3
    if num4 < num1 and num4 < num2 and num4 < num3:
        return num4
    
print(findMin(1,3,5,-19))

def findProduct(start,end):
    product = 1
    if start > end:
        for i in range(end,start):
            product *= i

    else:
        for i in range(start, end):
            product *= i
    return product

print(findProduct(5,1))

def findLen(num):
    nums = str(num)
    length = len(nums)
    return(length)

print(findLen(1230))

def isPalindrome(num):
    num = str(num)
    nums = []
    length = len(num)
    half = length / 2
    str_1 = ""
    str_2 = ""
    for i in num:
        nums.append(i)
    for i in range(half):
        str_1 = str_1 + nums[i]
    for i in range(half,length):
        str_2 = str_2 + nums[i]
    return str_1 == str_2[::-1]

print(isPalindrome(12344321))

