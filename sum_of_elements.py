#sum of elements
def sum_of_elements(numbers, exclude_negative = False):
    a = 0
    if exclude_negative:
        for num in numbers:
            if num >= 0:
                a += num
                print ("")
        return a
    else:
        return sum(numbers)


n = input('enter a list of numbers    ')

numbers_list = n.split()
numbers = []
for i in numbers_list:
    num = int(i)
    numbers.append(num)
#print(numbers) 

question = input('Do you want to exclude negative numbers? Say "Yes" or "No"')
if question == 'Yes':
    exclude_negative = True
else:
    exclude_negative = False

print(sum_of_elements(numbers, exclude_negative))
    