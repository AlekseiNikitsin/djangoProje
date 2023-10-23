numbers = [1,10,20,30]
counter = 0
for number in numbers:
    if (number % 10) == 1:
        counter +=1
print('Колличество четных чисел :', counter)