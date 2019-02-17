file = open("skus.txt")
numbers = list()
ing_list = list()
x=0
each=0
i=0

def howmany(list,number):
    count=0
    for each in list:
        if number == each:
            count += 1
    return count

def contains(list,number):
     for each in list:
        if number == each[0]:
            return True
     return False


for line in file:
    numbers.append(file.readline())

while x < len(numbers):
    if contains(ing_list,numbers[x])==False:
        ing_list.append((numbers[x],howmany(numbers,numbers[x])))
    x += 1


#sorw(ing_list)
def getKey(item):
    return item[1]
test = sorted(ing_list, key=getKey,reverse=True)
print(test[1:100])


# print(ing_list[0],howmany(numbers,numbers[0]))
# print(ing_list)

#for line in file:


