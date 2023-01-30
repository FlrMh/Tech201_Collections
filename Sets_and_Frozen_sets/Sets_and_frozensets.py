# Sets and Frozen sets

# Lists and sets are very similar
# Sets are unordered (items do not have an index)

# Create a set
car_parts = {"wheels", "doors", "exhaust_pipe"}
# print(car_parts)

# Remove parts of a set
car_parts.discard("doors")
# print(car_parts)

# Add parts to a set
car_parts.add("windows")
print(car_parts)


# Frozen sets
# EFrozen sets are immutable(cannot be changed or manipulated. Still random, unordered, and un-indexed.

x = frozenset([1, 2, 3, 4, "Five", "Six"])
print(x)


