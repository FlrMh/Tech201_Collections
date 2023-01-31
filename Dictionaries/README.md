# ***Dictionaries {}***

An introduction to Dictionaries in Python.

**Dictionaries** are used to store data values in *key:value* pairs. They are collections which are *ordered*, *changeable* and *do not allow duplicates*.
- **Key** = reference to a particular object (columns/categories)
- **Value** = data storage mechanism you want to use.

#### How to create a Dictionary ####
For this example we will create a dictionary named *student_1*:
```bash
student_1 = {
   "name": "Susan",
     "stream": "DevOps",
     "completed_lessons": 4,
     "completed_lesson_names": ["variables", "data_types", "set_up"]
 }
```

#### What can we do with a Dictionary? ####

1. Access data within a dictionary
```bash
print(student_1["stream"]) # this will print "DevOps" as that is the value we have for the "stream" key.
```

2. Access an element within a dictionary
```bash
print(student_1["completed_lesson_names"][0]) # this will print "variables", as we specified the name of the key from where we want a value, and the index of the value
```
3. Changing a value in a dictionary
```bash
student_1["completed_lessons"] = 3 # or "three" if it was a string
print(student_1["completed_lessons"]) # this will print 3 as we have just changed the value for that specific key.
```
4. Removing items from a dictionary
```bash
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"]) # this will print ["variables", "set_up"] as we just removed the "data_types" value.
```
5. Adding a new key:value pair to your dictionary:
```bash
student_1["birthdate"] = "1997/12/23"
print(student_1) # this will print the new dictionary with the newly added key and its value.
```

#### Dictionaries Methods ####

1. Keys
```bash
print(student_1.keys()) # prints the keys in a dictionary.
```
2. Get the value of a key back
``` bash
print(student_1.get("name")) # this will print "Susan" as this is the value we attributted to the "name" key.
```

3. Get the values of a dictionary
```bash 
print(student_1.values()) # this will print all the values for all the keys in the dictionary.
```
4. Showing the dictionary data elements as a list of tuple pairs
```bash 
print(student_1.items()) # Outputs an array of tuples with key and value pairs in dictionary
```

#### Dictionaries use cases:

1. You want to ***store objects and data using names***, not just positions or index numbers. If you want to store elements so that you can retrieve them by their index number, use a list.
2. You need to ***find data and objects quickly by name***. Dictionaries are optimized so that lookups for keys are almost always in constant time, regardless of the dictionary size. 
3. The ***order of elements isn't as important as their presence***. Again, if the ordering of the elements matters more than whether or not a given element exists in the collection, use a list.

