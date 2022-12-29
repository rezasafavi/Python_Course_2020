# code refactoring

# have a Help Command
def Show_Help():
    print("What Should We Pick Up at The Store? ")
    print("Enter 'Down' to stop adding items")
    print("Enter 'Show' to Show Item List")
    print("Enter 'Help' to Show Help Commands")

# have a Show Command
def Show_List():
    print("Here's Your List:")
    for item in Shopping_List:
        print(item)

# Have a adding List Item
def add_to_list(new_item):
    Shopping_List.append(new_item)
    print("Added {}.list now has {} items".format(new_item,len(Shopping_List)))



# make a list to hold onto our item
Shopping_List = []

Show_Help()

# ask for new item
while True:
    new_item = input("> ")
    # able quit app
    if new_item == "Down":
        break
    elif new_item== "Help":
        Show_Help()
        continue
    elif new_item == "Show":
        Show_List()
        continue
    add_to_list(new_item)


Show_List()


