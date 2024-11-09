########## Shopping List ##############

#Task 1

#Add Shopping list
shopping_list = []

# add item function
def add_item():
    global shopping_list
    add_input = input("\nAdd item: ")
    shopping_list.append(add_input)
    print("\nAdded: ", add_input)


#Task 2

# remove item function
def remove_item():
    global shopping_list
    
    while True:
        remove_input = input("\nRemove item: ")
        if remove_input in shopping_list:
            shopping_list.remove(remove_input) 
            break
        
        else: 
            print("Item not there")
            break
        

    
#Task 3

# display items function
def display_items(formatted_items="No Items"):
    print("Shopping List: ")
    global shopping_list
    for item in shopping_list:
        formatted_items = item
    print(formatted_items)

## Start user loop input 
while True:
    start_message = input('''
What would you like to do?
[A] View Shopping List
[B] Add an item
[C] Remove an item
[Q] Quit
''')

    # Choice Conditions
    if start_message.upper() == "Q":
        print("Bye, bye.")
        break
    elif start_message.upper() == "A":
        display_items()
        
    elif start_message.upper() == "B":
        add_item()
        
    elif start_message.upper() == "C":
        remove_item()
        
    else:
        print("###Invalid Input")
        