# List.........................
my_list = [1, 2, 3, "apple", "banana"]
first_item = my_list[0]  # Accessing the first element (1)
last_item = my_list[-1]  # Accessing the last element ("banana")
first_fruit = my_list[0]      # Access the first element (index 0)
second_fruit = my_list[1]     # Access the second element (index 1)
subset = my_list[1:3]         # Get a slice of elements (index 1 to 2)
my_list[1] = "orange"         # Modify an element
my_list.append("grape")      # Add an element to the end
my_list.insert(1, "kiwi")    # Insert an element at a specific index
my_list.remove("cherry")     # Remove an element by value

# Tuple......................
my_tuple = (1, 2, "apple")
first_element = my_tuple[0]  # Access the first element


# Set.......................
unique_numbers = {1, 2, 3, 2, 4, 5, 1}
# Result: {1, 2, 3, 4, 5} set automatical remove duplicate elements
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union = set1 | set2       # Union: {1, 2, 3, 4, 5}
intersection = set1 & set2  # Intersection: {3}
difference = set1 - set2   # Difference: {1, 2}


# Dictionary...............................
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}
name = student["name"]  # Accessing the value associated with the "name" key

