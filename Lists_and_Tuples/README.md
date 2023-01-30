# ***Lists and Tuples***
An introduction to Lists and Tuples in Python.

## ***1. Lists []*** ##

In Python, a **List** is a *collection* which is **ordered and mutable**, which also **allows duplicate members**.
It is a collection of data which supports in data management. 

#### How do we create a list in Python? ####

- First, we need a name for our list. For this example, let`s create a Shopping list!
```bash
shopping_list1 = ["cookies", "ice cream", "chocolate", "fruits"]
```
- Great! Now, if you want to see your list, just print the list you just created!
```bash
print(shopping_list1)
```
- You should be able to successfully see your list by running the command above. 
- Now, let`s verify if we created the right type of collection. Simply do that by running:
```bash
print(type(shopping_list1))  
```
- It should print ```<class 'list'>```
- If you got that, happy days! You have just created your first list!




#### What can we do with a List?


Before getting into that, let`s look at Lists a little closer, shall we?
*Each element* of the list has a **specific order**. We can access each list element by the ***index number***. The first element of the list has a base index i.e. 0. 

Now, how can we use that in a List?

- Print specific items from our list! Let`s do it together:
```bash
print(shopping_list1[0]) # this will print "cookies" (the first item added to the list)
print(shopping_list1[3]) # this will print "chocolate" (the 3rd item added to the list)
print(shopping_list1[-1]) # this will print "fruits" (as when using "-", Python is taking items in order from right to left)
print(shopping_list1[0:3]) # this will print "cookies", "ice cream", "chocolate" (as when using ":" we request the print of a range of items, mentioning the starting point and end point through the items` indexes).
 ```
That`s easy, right? How about we look at some more things!

- We can change a specific part of our list by re-writing a value in the list:
```bash
shopping_list1[0] = "orange_juice"
print(shopping_list1[0]) # this will print "orange juice" because we changed the value of the item with the index 0 with "orange juice"
```

There are plenty more things we can do with a List. Let`s get into that next. 

#### Lists Methods


1. Adding elements to a list: 
```bash
shopping_list1.append("coffee") # this will add a new item to the list, at the end of the list.
print(shopping_list1) # this should print the updated list.
```
2. Checking the length of a list (re. number of values added):
```bash
print(len(shopping_list1)) # if we take into account our initial list, this will print 4. 
```
3. Removing elements from a list:
```bash
shopping_list1.remove("coffee") # this will remove the item from the list
print(shopping_list1) # this should print the updated list.
```
4. Removing the last entry from the list without having to specify it:
```bash
shopping_list1.pop() # this will remove the last item of the list, without us having to specify the index number or the value of that item
print(shopping_list1) # this should print the updated list.
```
5. Making a shallow copy of the list: ```copy()```
6. Removing all items from a list: ```clear()```
7. Inserting a given element at a given index in a list: ```index()```
8. Sorting a list in ascending, descending, or user-definer oder: ```sort()```

!!! One thing to keep in mind is, although we created a list that has only one type of data (in our shopping_list1 case, strings), we can have lists that store *mixed data types*.
 
Let`s showcase this by creating a Mixed data types list called ***Mixture*** 
```bash
mixture = [1, 2, 3, 4, "five", "six, "seven] # this is a mixed data type list as it stores both strings and integers.
```


#### Lists use-cases

Python list has a great significance in data storage and can be used in multiple cases:

1. When you have **various elements** of **different data types**, you can store them in a list and can access these elements by simply referring to their indices.
2. A list can also be **resized**. Hence, a list is useful when you are not certain about the number of elements.
3. Lists are highly preferable when a **small amount of data** is required to be stored, since the built-in functions of the list are quite convenient for data manipulation.



## ***2. Tuples ()***

Python **Tuple** is a *collection* of objects separated by commas. In some ways, a tuple is *similar to a list* in terms of indexing and repetition, but a tuple is **immutable**, unlike lists which are mutable.

- The orders of the items in a tuple have a certain order that won`t change.
- They are unchangeable as collections, which means you cannot add and remove items, or alter the tuple after it has been created.
- It can store any type of data, or even a mixture of different data types. 

#### Tuples use-cases:
At first sight, it might seem that lists can always replace tuples. But tuples are extremely useful data structures

1. Using a tuple instead of a list can give the programmer and the interpreter a *hint* that the **data should not be changed**.
 
2. Tuples are commonly used as the *equivalent of a dictionary without keys* to store data. For Example,
```bash
[('Swordfish', 'Dominic Sena', 2001), ('Snowden', ' Oliver Stone', 2016), ('Taxi Driver', 'Martin Scorsese', 1976)]
```
Above example contains tuples inside list which has a list of movies.
 
3. *Reading data is simpler* when tuples are stored inside a list. For example,
```bash
[(2,4), (5,7), (3,8), (5,9)]
is easier to read than
[[2,4], [5,7], [3,8], [5,9]]
```