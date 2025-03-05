#Problem 1
#1. pwd
#2. ls
#3. cd .. into cd brianna_repo
#4. git pull brianna_repo judy_decal
#5. cat homework.py
#6. nano homework.py
#7. git add, git commit -m "message here", git push origin master
#8. She didn't pull from the github and she should do that first and then resubmit.
#9. cd ~/Recent

#Problem 2
#2.1
def checkDataType(input):
    s = type(input)
    a = str(s)
    a = a.replace("class", "")
    a = a.replace("<", "")
    a = a.replace(">", "")
    return a
print(checkDataType(5))

#2.2
def EvenOrOdd(x):
    if x % 2 == 0:
        print('even')
    else:
        print('odd')

EvenOrOdd(36)
EvenOrOdd(3)

#Problem 3
nums = [1,2,3,4,5]
def SumWithLoop(nums):
    sum2 = 0
    for val in nums:
        sum2 += val
    return sum2
print(SumWithLoop(nums))

#Problem 4
#4.1
list = ['a', 'b', 'c']
def duplicateList(list):
    duplicate = []
    for item in list:
        duplicate.extend([item, item])
    return(duplicate)

print(duplicateList(list))

#4.2
num = 5
def Square(num):
    return num **2

print(Square(num))