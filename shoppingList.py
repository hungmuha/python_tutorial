#make a list to hold onto our items
shopping_list = []
#print out instructions on how to use th app
print("what should we pick up at the store?")
print("Enter'DONE' to stop adding items")

while True: 
    #ask for new items
    new_item = input("> ")
    #be able to quit the app
    if new_item == "DONE":
        break
#add new itms to our list
    shopping_list.append(new_item)

     
#print out the list
print("Here's your list")

for items in shopping_list:
	   print(items)