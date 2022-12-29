# make a list to hold onto our item
Shopping_List = []

# print out instructions on how use app
print("What Should We Pick Up at The Store? ")
print("Enter 'Down' to stop adding items")

# ask for new item
while True:
    new_item = input("> ")
    # able quit app
    if new_item == "Down":
        break
# add new item to our list
    Shopping_List.append(new_item)


# print list
print("Here's Your List:")
for item in Shopping_List:
    print(item)





