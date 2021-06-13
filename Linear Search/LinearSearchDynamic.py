list = []
num = int(input("Enter the size of List: "))

for n in range(num):
    numbers = int(input("Enter the array of %d element: "%n))
    list.append(numbers)

x = int(input("Enter number to search in the list: "))
i = 0
flag = False

for i in range(len(list)):
    if list[i] == x:
        flag = True
        break
if flag == 1:
    print('{} was found at index {}.'.format(x,i))
else:
    print('{} was not found'.format(x))

