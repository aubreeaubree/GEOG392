#part 1 
def multpy(list1):
    multAll = 1
    for i in list1:
        multAll *= i
    return(multAll)
       
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096] 
print("For part 1, the result of the multiplication is", multpy(part1))

#part2
def addAll(list2):
    addUp = 0
    for i in list2:
        addUp += i
    return(addUp)

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
print("For part 2, the sum of all the numbers in the list is", addAll(part2))

#part3
def addEven(list3):
    evensToBeAdded = 0
    for i in list3:
        if i % 2 == 0:
            evensToBeAdded += i
    return evensToBeAdded

part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21] 
print("For part 3, the sum of the even numbers is", addEven(part3))