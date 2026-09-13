Activity = {}

def ViewItem():
    '''Viewing Items in Todo List'''
    if Activity:
        for id, details in Activity.items():
            print(f'''Activity Id:{id} = Name: {details["Name"]},
                                Description: {details["Description"]},
                                Status: {details["Status"]}''')
    else:
        print("There is no Item in List")


def choice():
    print('''
            Enter Your Choice:
    
                1. Add New List Item
    
                2. Edit List Item
    
                3. Delete List Item
        ''')
    

def EnterChoice(n):
    if n==1:
        ViewItem()
        return AddItem()
    elif n==2:
        ViewItem()
        return EditItem()
    elif n==3:
        ViewItem()
        return DeleteItem()
    else:
        print('Invalid Choice')


def AddItem():
    '''Adding Item in Todo List'''
    id = int(input('Enter Activity ID: '))
    name = input('Enter a Activity Name: ')
    description = input('Enter a Detailed Description of Activity: ')
    Status = False

    Activity[id] = { "Name": name,
                    "Description": description,
                     "Status": Status }

    print("New item added Successfully")


def EditItem():
    '''Editing Item in Todo List'''
    print("Editing a already existing Item")

    if not Activity[id]:
        print("There is No Id in List")
    else:
        id = int(input('Enter a ID to Edit: '))
        name = input('Enter a New Name: ')
        description =  input("Enter a New Description: ")
        st=int(input("Enter a 0 if completed else 1: "))
        status = (st == 1)
    
        Activity[id] = {"Name": name, 
                        "Description": description,
                        "Status": status}
    
        print(f"Item{id} Edited Successfully")
    

def DeleteItem():
    '''Deleting Item in Todo List'''
    id = int(input('Enter a ID to Delete: '))

    del Activity[id]

    print("Item Deleted Successfully")

def Main():
    while True:
        MainChoice = int(input("Enter a Choice(1=Continue or 0=exit):"))
        if MainChoice == 1:
            choice()
            n = int(input("Enter a Number: "))
            x = EnterChoice(n)
        else:
            print("Thank You for using this Todo List")
            break


if __name__ == "__main__":
    Main()
    