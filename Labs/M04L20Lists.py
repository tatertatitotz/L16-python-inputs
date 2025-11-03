#list of items accessing
itemList = ["hi", "hello", "bye"]
print(itemList[1]) # = itemList[-2]

#will only print "hello", hi = 0, hello = 1, bye = 2
itemList = ["hi", "hello", "bye", "goodbye", "meow"]
print(itemList[2:4]) #prints items 2 and 3, stops at the 4th item.


#changing
itemList = ["hi", "hello", "bye", "goodbye", "meow"]
itemList[2] = "blue"
#replaces "bye" with "blue"
print(itemList)

itemList = ["hi", "hello", "bye", "goodbye", "meow"]
#replaces “hello” with both “blue” and “yellow” because the item list between list item 1 and 2 is hello.
itemList[1:2] = ["blue", "yellow"]
print(itemList)
#replaces multiple items with one item

itemList = ["hi", "hello", "bye", "goodbye", "meow"]
itemList[1:3] = "blue"
print(itemList)
#replaces hello and bye with blue


#adding
itemList = ["hi","goodbye", "meow"]
#.append() adds an item to the list at the END
itemList.append("blue")
print(itemList)

itemList = ["hi","goodbye", "meow"]
#.insert() adds an item to the assigned number position in the list WORKS WITH NEGATIVE NUMBERS TOO!
itemList.insert(1, "blue")
#adds blue after hi as the new 1.
print(itemList)

#removing
itemList = ["hi", "goodbye", "meow"]
#.remove() removes a specific item
itemList.remove("hi")
print(itemList)

itemList = ["hi", "goodbye", "meow"]
#.pop() removes an item based on its position in the list
itemList.pop(1)
print(itemList)

itemList = ["hi", "goodbye", "meow"]
#del can delete one or more items in the list based on number
del itemList[1:3]
#print out only hi
print(itemList)

itemList = ["hi", "goodbye", "meow"]
#clear does not take arguments.
itemList.clear()
#guts everything inside the list
print(itemList)