#example 2 Arrays
my_array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("Original array:", my_array)
print("Length of array:", len(my_array))
print("First element:", my_array[0])
print("Last element:", my_array[-1])    
print("Sliced array:", my_array[1:7])

my_array.append(110)
print("Array after appending 110:", my_array)   

my_array.remove(30)
print("Array after removing 30:", my_array) 

my_array.sort()
print("Sorted array:", my_array)

my_array.reverse()
print("Reversed array:", my_array)

