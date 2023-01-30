# Dictionaries

# Dictionaries use key/value pairs
# Key = reference to a particular object (columns/categories)
# Value = data storage mechanism you want to use

# Creating a dictionary
# student_1 = {
#     "name": "Susan",
#     "stream": "DevOps",
#     "completed_lessons": 4,
#     "completed_lesson_names": ["variables", "data_types", "set_up"]
# }
#
# # Access data within a dictionary
#
# print(student_1["stream"]) # DevOps
#
# # Access an element within a dictionary
#
# print(student_1["completed_lesson_names"][0]) # Name of the key from where you want a value, and the index of the value
#
# # Changing a value in a dictionary
#
# student_1["completed_lessons"] = 3 # or "three" if it was a string
# print(student_1["completed_lessons"])
#
#
# # Removing items from a dictionary
#
# student_1["completed_lesson_names"].remove("data_types")
# print(student_1["completed_lesson_names"])
#
#
# # Dictionary methods
#
# # Keys
# print(student_1.keys()) # prints the keys in a dictionary
#
# # Get the value of a key back
# print(student_1.get("name"))
#
# # Get the values of a dictionary
# print(student_1.values())
#
# print(student_1.items()) # Outputs array of tuples with key and value pairs in dictionary
#
# Practice:
# Employee_1 = {
#     "name": "Christine Johnson",
#     "age": "32",
#     "length_of_employment(years)": 2.5,
#     "hourly_rate(£)": 13.50,
#     "department(s)": ["FOH", "BOH"],
#     "student": True
# }
#
# print(Employee_1)

#

