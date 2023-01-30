# Lists

# Lists in Python are called Arrays in other languages.
# They are all about data management.

# Here is our first list:

shopping_list = ["milk", "eggs", "bread", "fruits", "cheese"]
#
# print(type(shopping_list)) # <class 'list'>
# print(shopping_list) # Print the data in raw version, not as a list
#
# print(shopping_list[0]) # milk(the first data added to the list)
# print(shopping_list[3]) # fruits
# print(shopping_list[-1]) # cheese
# print(shopping_list[0:3])


# We can change a specific part of our list by re-writing a value in the list

# shopping_list[0] = "sugar"
# print(shopping_list[0]) # Sugar (milk will be overwritten by sugar)


# Lists methods

# Adding to a list
shopping_list.append("vegetables")
# print(shopping_list)
# print(shopping_list[5]) # vegetables
# print(len(shopping_list)) # Check the length of a variable


# Removing from a list
# shopping_list.remove("bread")
# print(shopping_list)
# print(len(shopping_list))


# Removing the last entry in the list without specifying it
# shopping_list.pop()
# print(len(shopping_list))
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)


# Mixed data type lists
mixture = [1, 2, 3.5, "one", "two", "three", "four"]
print(mixture)


# List slicing
# print(mixture[1:3]) # the indexes of the items we want to separate
# print(mixture[-2::]) # reverses the order
# print(mixture[::2]) # bounces over the amount of indexes specified


# Tuples

# Exactly the same as lists, except they are immutable(cannot be changed/edited).
# Tuples are useful for elements you want to make sure are not going to change.

# essentials = ("bread", "eggs", "milk")
# print(essentials)
# print(essentials.count("bread"))
# essentials.remove("bread") # Tuples do not have built-in methods and neither item assignments





