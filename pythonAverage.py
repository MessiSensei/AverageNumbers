# ask the user three times for each number
print(" ask the user three times for each number\n")
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
average = (a+b+c)/3
print(average)

#using Map and split
print("Using Map and split \n")
a, b, c = map(int, input("Enter 3 numbers (separated by commas): ").split(','))

#input("Enter 3 numbers (separated by commas): ").split(',')) === > #this will result in ['3', '4', '5'].
#Mapping to Integers:map(int, ...) applies the int function to each element of the list created by split().
# This converts the list of string representations of numbers into a list of integers. For example, map(int, ['3', '4', '5']) results in [3, 4, 5].
#Unpacking Values: a, b, c = ... 
average = (a+b+c)/3
print(average)

# another way to do this 
# Initialize an empty list and use a loop to append numbers
print("Using Loop \n")
numbers = []
for i in range(3):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
a, b, c = numbers
average = (a+b+c)/3
print(average,"\n")


#List Comprehension
# user for input and use list comprehension to convert to integers
print("List Comprehension\n")
numbers = [int(x) for x in input("Enter 3 numbers (separated by commas): ").split(',')]
a, b, c = numbers[0], numbers[1], numbers[2]
average = (a+b+c)/3
print(f"{average:.2f} \n")
