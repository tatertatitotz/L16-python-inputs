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
