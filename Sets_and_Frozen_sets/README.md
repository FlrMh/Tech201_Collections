# ***Sets and Frozen Sets***

An introduction to Sets and Frozen Sets in Python,

## ***1. Sets {}***

A **Set** and a List can be quite similar at a first glance. However, a **Set** is an *unordered collection*  that is *mutable* (add/remove items) and has *no duplicate elements*. 

Let`s create a Set together! For this example, we will create a Set called painting_essentials: 
```bash
painting_essentials = {"brushes", "paint", "canvas"}
print(painting_essentials) 
```
As with Lists, we can do few different things with Sets as well. Only, remember: **Set items are unchangeable**, so we *cannot change the items* once the Set is created! We can simply *add or remove* items!/ 
1. Add new items:
```bash
painting_essentials.add("water") 
print(painting_essentials)
```
2. Removing items:
```bash
painting_essentials.remove("water")
print(painting_essentials) 
```

## ***2. Frozen Sets ()***

**Frozen sets** are collections that are *immutable* (like tuples), *un-ordered* and *un-indexed* (like sets), and cannot have duplicate items.
Creating a Frozen set:
```bash
x = (1, 2, 3, "four", "five", "six")
```