#Monastyrskiy Maxim


#Login authenticator
######### LOGIN=maxim, PASSWORD=admin01 #########
def authen():
    print()
    print("-----------------------------------------")
    print("LOGIN")
    print()
    while True:
        login = input("Please enter the username: ")
        password = input("Please enter the password: ")
        with open("userdata.txt", "r") as file:
            for line in file:
                #checking the userdata.txt file to see if any of the input made by the user matches the data in the txt file
                login_type = line.strip("\n").split(",")[0]
                data_login = line.strip("\n").split(",")[1]
                data_password = line.strip("\n").split(",")[2]
                if login == data_login and password == data_password:
                    print("Login successful.")
                    return login_type    
            else:
                print("Invalid login or wrong password.")
                print() 


#Inventory system functions
def INSERT_NEW_ITEM():
    print()
    print("-----------------------------------------")
    print("INVENTORY UPDATER")
    print()
    print("1 - Add one item")
    print("2 - Add multiple items")
    print("0 - Go back to main menu")
    print()
    print("-----------------------------------------")
    while True:
        insertchoice = input("Please choose an option : ")
        #Checking if the user entered spesific task
        if insertchoice in ("1","2","0"):
            break
        else:
            print("Please choose either 1 or 2, if you want to go back to main page press 9")

    if insertchoice == "1":
        print("-----------------------------------------")
        print("ADDING ONE ITEM")
        print()
        print("Please enter the following of the item")
        print()
        while True:
            code = input("Code : ")
            #Checking if the length of the code is 5 and to check if the codes are already used
            if len(code) == 5 and is_code_used(code):
                break
            else:
                print("The code of the item should be 5 digits or code has been used")
        while True:
            description = input("Description : ")
            #Checking if the user entered something
            if description != "":
                break
            else:
                print("please enter the name of the item")
        while True:
            category = input("Category : ")
            #Checking if the user entered something
            if category != "":
                break
            else:
                print("please enter the category of the item")
        while True:
            unit = input("Unit : ")
            #Checking if the user entered the right input
            if unit in ("box","pieces","pack","bottle"):
                break
            else:
                print("Unit should be in the following : box, pieces, pack, bottle")
        while True:
            price = input("Price : ")
            #Checking if the user entered with 2 demial places
            formatprice = str(price).strip()
            if formatprice.count(".") == 1 and len(formatprice.split(".")[-1]) == 2:
                break
            else:
                print("please enter the price using the format of .00")
        while True:
            quantity = input("Quantity : ")
            #Checking if the user entered a number
            if quantity.isdigit():
                break
            else:
                print("Quantity should be a number")
        while True:
            minimum = input("Minimum : ")
            #Checking if the user entered a number
            if minimum.isdigit():
                break
            else:
                print("Minimum should be a number")
        #Finally the whole thing will be appended to the txt file
        with open("inventory.txt","a") as file :
            file.write(f"\n{code},{description},{category},{unit},{price},{quantity},{minimum}")
        
        print()
        print(code+","+description+","+category+","+unit+","+price+","+quantity+","+minimum+" has been added to the database")
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")

    #This will allow the user to enter many items in one go
    elif insertchoice =="2":
        print()
        while True:
            amountofitem = input("Please enter how many items you would like to add : ")
            #checking if its a number
            if amountofitem.isdigit():
                break
            else:
                print("Please enter a number : ")
        amountofitem = int(amountofitem)
        #making a loop for amount of items to be created
        for i in range (1, amountofitem+1):
            while True:
                code = input("Code : ")
                #Checking if the length of the code is 5 and to check if the codes are already used
                if len(code) == 5 and is_code_used(code):
                    break
                else:
                    print("The code of the item should be 5 digits or code has been used")
            while True:
                description = input("Description : ")
                #Checking if the user entered something
                if description != "":
                    break
                else:
                    print("please enter the name of the item")
            while True:
                category = input("Category : ")
                #Checking if the user entered something
                if category != "":
                    break
                else:
                    print("please enter the category of the item")
            while True:
                unit = input("Unit : ")
                #Checking if the user entered the right input
                if unit in ("box","pieces","pack"):
                    break
                else:
                    print("Unit should be in the following : box, pieces, pack")
            while True:
                price = input("Price : ")
                #Checking if the user entered with 2 demial places
                formatprice = str(price).strip()
                if formatprice.count(".") == 1 and len(formatprice.split(".")[-1]) == 2:
                    break
                else:
                    print("please enter the price using the format of .00")
            while True:
                quantity = input("Quantity : ")
                #Checking if the user entered a number
                if quantity.isdigit():
                    break
                else:
                    print("Quantity should be a number")
            while True:
                minimum = input("Minimum : ")
                #Checking if the user entered a number
                if minimum.isdigit():
                    break
                else:
                    print("Minimum should be a number")
            #Finally the whole thing will be appended to the txt file
            with open("inventory.txt","a") as file :
                file.write(f"\n{code},{description},{category},{unit},{price},{quantity},{minimum}")
            
        print()
        print("The "+str(amountofitem)+" items has been added to the database")
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")   

    #Back to main menu    
    elif insertchoice =="0":
        main()


def UPDATE_ITEM():
    print("-----------------------------------------")
    print()
    print("UPDATE AN ITEM")
    print() 
    while True:
        code = input("Please enter the code : ")
        #Checking if the length of the code is 5 and to check if the code exist
        if len(code) == 5 and not is_code_used(code):
            print()
            print("1 - Code")
            print("2 - Descrpition")
            print("3 - Category")
            print("4 - Unit")
            print("5 - Price")
            print("6 - Quantity")
            print("7 - Min Quantity")
            print()
            break
        elif code == "":
            main()
        else:
            print("Code does not exist, Please re-enter")
    while True:
        choose_edit = input("Please enter what to be edited : ")
        if choose_edit in ("1","2","3","4","5","6","7"):
            Edit(code,choose_edit)
            break
        elif choose_edit == "":
            main()
        else:
            print("Please choose the given option")
    while True:
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu != "0":
            print("Thank you have a good day!")
            break
        else:
            main()


def DELETE_ITEM():
    print("-----------------------------------------")
    print()
    print("DELETE AN ITEM")
    print() 
    while True:
        code = input("Please enter the code : ")
        #Checking if the length of the code is 5 and to check if the code exist
        if len(code) == 5 and not is_code_used(code):
            break
        elif code == "":
            main()
        else:
            print("Code does not exist, Please re-enter")
    while True:
        Remove(code)
        break
    backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
    if backtomainmenu == "0":
        main()
    else:
        print("Thank you have a good day!")


def STOCK_TAKING():
    print("-----------------------------------------")
    print()
    print("STOCK TAKING")
    print()
    while True:
        code = input("Please enter the code : ")
        if not is_code_used(code):
            break
        else: 
            print("Sorry code doesn't exist")
    #reused the search item by taking the search by code, since the code was searched by range, i had to re-adjust as shown
    while True:
        input_code1 = code
        input_code2 = code
        Code(input_code1,input_code2)
        break
    while True:
        print("1 - Confirm")
        print("2 - Change the quantity")
        stock_choice = input("Please choose an option : ")
        if stock_choice == "1":
            backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
            if backtomainmenu != "0":
                print("Thank you have a good day!")
                break
            else:
                main()
        elif stock_choice == "2":
            
            with open("inventory.txt","r") as file:
                lines = file.readlines()
            #This len(lines) checks how many lines are there in the txt file
            for i in range(len(lines)):
                inventory_code,inventory_name,inventory_category,inventory_unit,inventory_price,inventory_quantity,inventory_min_quantity = lines[i].strip("\n").split(",")
                if inventory_code == code:
                    while True:
                        edit_quantity = input("Please enter new quantity : ")
                        if edit_quantity.isdigit():
                            break
                        else:
                            print("Please enter a number")

                    new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{inventory_unit},{inventory_price},{edit_quantity},{inventory_min_quantity}\n"
                    lines[i] = new_code_line
                    break
            with open("inventory.txt","w") as file :
                file.writelines(lines)
    
            print("Item update successful")
            print()
    
            backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
            if backtomainmenu == "0":
                main()
            else:
                print("Thank you have a good day!")
                break
        else:
            main()


def VIEW_REPLENISH_LIST():
    print("-----------------------------------------")
    print()
    print("STOCK THAT NEEEDS REPLENISHMENT")
    print()
    while True:
        with open("inventory.txt","r") as file:
            for line in file:
                inventory_code = line.strip("\n").split(",")[0]
                inventory_name = line.strip("\n").split(",")[1]
                inventory_category = line.strip("\n").split(",")[2]
                inventory_unit = line.strip("\n").split(",")[3]
                inventory_price = line.strip("\n").split(",")[4]
                inventory_quantity = line.strip("\n").split(",")[5]
                inventory_min_quantity = line.strip("\n").split(",")[6]
                
                if int(inventory_quantity) < int(inventory_min_quantity) :
                    print()
                    print("Code     Description     Category     Unit     Price     Quantity      Minimum quantity")
                    print()
                    combined_item = (inventory_code+"     "+inventory_name+"       "+inventory_category+"     "+inventory_unit+"       "+inventory_price+"\t     "+inventory_quantity+"     \t     "+inventory_min_quantity)
                    print(combined_item)
                    print()
            break
    while True:
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")
            break


def STOCK_REPLENISHMENT():
    print("-----------------------------------------")
    print()
    print("STOCK REPLENISHMENT")
    print()
    while True:
        code = input("Please enter the code : ")
        if not is_code_used(code):
            break
        else: 
            print("Sorry code doesn't exist")
    #reused the search item by taking the search by code, because the code was searched by range i had to re-adjust as shown
    while True:
        input_code1 = code
        input_code2 = code
        Code(input_code1,input_code2)
        break
    while True:
        print("1 - Confirm")
        print("2 - Add purchased amount")
        stock_choice = input("Please choose an option : ")
        if stock_choice == "1":
            backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
            if backtomainmenu != "0":
                print("Thank you have a good day!")
                break
            else:
                main()
            break
        elif stock_choice == "2":
            
            with open("inventory.txt","r") as file:
                lines = file.readlines()
            #This len(lines) checks how many lines are there in the txt file
            for i in range(len(lines)):
                inventory_code,inventory_name,inventory_category,inventory_unit,inventory_price,inventory_quantity,inventory_min_quantity = lines[i].strip("\n").split(",")
                if inventory_code ==  code:
                    while True:
                        edit_quantity = input("Please how many items have been purchased : ")
                        if edit_quantity.isdigit():
                            break
                        else:
                            print("Please enter a number")

                    new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{inventory_unit},{inventory_price},{(int(edit_quantity) + int(inventory_quantity))},{inventory_min_quantity}\n"
                    lines[i] = new_code_line
                    break
            with open("inventory.txt","w") as file :
                file.writelines(lines)
    
            print("Item update successful")
            print()
    
            backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
            if backtomainmenu == "0":
                main()
            else:
                print("Thank you have a good day!")
                break
        else:
            main()


def SEARCH_ITEM():
    print()
    print("-----------------------------------------")
    print("SEARCH THE INVENTORY")
    print()
    print("1 - By description")
    print("2 - Range of the code")
    print("3 - By category")
    print("4 - Range of the price")
    print("0 - Go back to main menu")
    print()
    print("-----------------------------------------")

    while True:
        searchchoice = input("Please choose an option : ")
        #Checking if the user entered spesific task
        if searchchoice in ("1","2","3","4","0"):
            break
        else:
            print("Please choose either 1 or 2 or 3 or 4, if you want to go back to main page press 0")
    
    if searchchoice == "1":
        print()
        while True:
            input_name = input("Please enter the description : ")
            if Items(input_name):
                break
            elif input_name =="":
                main()
            else:
                print("Sorry there is no item matching that description")
        print()
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")

    if searchchoice == "2":
        print()
        while True:
            input_code1 = input("Please enter the lower range of the code : ")
            input_code2 = input("Please enter the higher range of the code : ")
            if Code(input_code1,input_code2):
                break
            if input_code1 == "" or input_code2 =="":
                main()
            else:
                print()
                print("Sorry there is no item matching that description or the lower number can be higher than the higher number")
                print()
        print()
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")

    if searchchoice == "3":
        print()
        while True:
            input_category = input("Please enter the category : ")
            if Category(input_category):
                break
            elif input_category == "":
                main()
            else:
                print("Sorry there is no item matching that category")
        print()
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")

    if searchchoice == "4":
        print()
        while True:
            input_price1 = input("Please enter the lower range of the price : ")
            input_price2 = input("Please enter the higher range of the price : ")
            if Price(input_price1,input_price2):
                break
            if input_price1 == "" or input_price2 =="":
                main()
            else:
                print()
                print("Sorry there is no item matching that description or the lower number can be higher than the higher number")
                print()
        print()
        print()
        #Give the user an option to go back to main menu or exit
        backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
        if backtomainmenu == "0":
            main()
        else:
            print("Thank you have a good day!")
        
    if searchchoice == "2":
        pass
    if searchchoice == "3":
        pass
    if searchchoice == "4":
        pass
    if searchchoice == "0":
        main()


#Created an extra function to check if the codes, so they dont duplicate
def is_code_used(code):
    with open("inventory.txt","r") as file:
        for line in file:
            inventory_code = line.split(",")[0]
            #opposite result so it can continue in the while true loop
            if inventory_code == code:
                return False
    return True


#This is used to search the item description in the database
def Items(input_name):
    #used for looping so the program can continue
    found = False
    with open("inventory.txt","r") as file:
        for line in file:
            inventory_code = line.strip("\n").split(",")[0]
            inventory_name = line.strip("\n").split(",")[1]
            inventory_category = line.strip("\n").split(",")[2]
            inventory_unit = line.strip("\n").split(",")[3]
            inventory_price = line.strip("\n").split(",")[4]
            inventory_quantity = line.strip("\n").split(",")[5]
            inventory_min_quantity = line.strip("\n").split(",")[6]
            if inventory_name.lower() == input_name.lower():
                print()
                combined_item = ("code : "+inventory_code+"\nDescription : "+inventory_name+"\nCategory : "+inventory_category+"\nUnit : "+inventory_unit+"\nPrice : "+inventory_price+"\nQuantity : "+inventory_quantity+"\nMinimum quantity : "+inventory_min_quantity)
                print(combined_item)
                print()
                found = True
        #used for looping so the program can continue, if the request was not found then the user has to re-enter the request
        if found :
            return True
        else:
            return False
        
#This is used to search the category in the database        
def Category(input_category):
    #used for looping so the program can continue
    found = False
    with open("inventory.txt","r") as file:
        for line in file:
            inventory_code = line.strip("\n").split(",")[0]
            inventory_name = line.strip("\n").split(",")[1]
            inventory_category = line.strip("\n").split(",")[2]
            inventory_unit = line.strip("\n").split(",")[3]
            inventory_price = line.strip("\n").split(",")[4]
            inventory_quantity = line.strip("\n").split(",")[5]
            inventory_min_quantity = line.strip("\n").split(",")[6]
            if inventory_category.lower() == input_category.lower():
                print()
                combined_item = ("code : "+inventory_code+"\nDescription : "+inventory_name+"\nCategory : "+inventory_category+"\nUnit : "+inventory_unit+"\nPrice : "+inventory_price+"\nQuantity : "+inventory_quantity+"\nMinimum quantity : "+inventory_min_quantity)
                print(combined_item)
                print()
                found = True
        #used for looping so the program can continue, if the request was not found then the user has to re-enter the request
        if found :
            return True
        else:
            return False
        
#Used to find the range of the code       
def Code(input_code1,input_code2):
    #used for looping so the program can continue
    found = False
    with open("inventory.txt","r") as file:
        for line in file:
            inventory_code = line.strip("\n").split(",")[0]
            inventory_name = line.strip("\n").split(",")[1]
            inventory_category = line.strip("\n").split(",")[2]
            inventory_unit = line.strip("\n").split(",")[3]
            inventory_price = line.strip("\n").split(",")[4]
            inventory_quantity = line.strip("\n").split(",")[5]
            inventory_min_quantity = line.strip("\n").split(",")[6]
            if input_code1 <= inventory_code <= input_code2:
                print()
                combined_item = ("code : "+inventory_code+"\nDescription : "+inventory_name+"\nCategory : "+inventory_category+"\nUnit : "+inventory_unit+"\nPrice : "+inventory_price+"\nQuantity : "+inventory_quantity+"\nMinimum quantity : "+inventory_min_quantity)
                print(combined_item)
                print()
                found = True
        #used for looping so the program can continue, if the request was not found then the user has to re-enter the request
        if found :
            return True
        else:
            return False
        
#Used to find the range of the price        
def Price(input_price1,input_price2):
    #used for looping so the program can continue
    found = False
    with open("Inventory.txt","r") as file:
        for line in file:
            inventory_code = line.strip("\n").split(",")[0]
            inventory_name = line.strip("\n").split(",")[1]
            inventory_category = line.strip("\n").split(",")[2]
            inventory_unit = line.strip("\n").split(",")[3]
            inventory_price = line.strip("\n").split(",")[4]
            inventory_quantity = line.strip("\n").split(",")[5]
            inventory_min_quantity = line.strip("\n").split(",")[6]
            if int(input_price1) <= int(float(inventory_price)) <= int(input_price2):
                print()
                combined_item = ("code : "+inventory_code+"\nDescription : "+inventory_name+"\nCategory : "+inventory_category+"\nUnit : "+inventory_unit+"\nPrice : "+inventory_price+"\nQuantity : "+inventory_quantity+"\nMinimum quantity : "+inventory_min_quantity)
                print(combined_item)
                print()
                found = True
        #used for looping so the program can continue, if the request was not found then the user has to re-enter the request
        if found :
            return True
        else:
            return False

#Used to remove spesific line when user enters a code
def Remove(code):
    with open("inventory.txt", "r") as file:
        lines = file.readlines()

    #Find the line to be deleted
    delete_line = None
    for i in range(len(lines)):
        #use i to find the which line is the user requesting
        inventory_code = lines[i].strip().split(",")[0]
        if inventory_code == code:
            delete_line = i
            break

    #Finnaly delete the line
    if delete_line is not None:
        del lines[delete_line]
        #replaces it with blank
        with open("inventory.txt", "w") as file:
            file.writelines(lines)
        print()
        print("Action done successfully")
        print()
        print("-----------------------------------------")

#Used to edit the item
def Edit(code,choose_edit):
    with open("inventory.txt","r") as file:
        lines = file.readlines()
    #This len(lines) checks how many lines are there in the txt file
    for i in range(len(lines)):
        inventory_code,inventory_name,inventory_category,inventory_unit,inventory_price,inventory_quantity,inventory_min_quantity = lines[i].strip("\n").split(",")
        if inventory_code ==  code:
            if choose_edit =="1":
                while True:
                    code = input("Please enter new code : ")
                    if is_code_used(code) and len(code) == 5:
                        break
                    else:
                        print("Code is already used or can only be 5 character")

                new_code_line = f"{code},{inventory_name},{inventory_category},{inventory_unit},{inventory_price},{inventory_quantity},{inventory_min_quantity}"
                #lines[i] allows the spesific line to be edited
                lines[i] = new_code_line
                break

            elif choose_edit =="2":
                while True:
                    edit_name = input("Please enter new description : ")
                    if edit_name != "":
                        break
                    else:
                        print("Please enter the description")

                new_code_line = f"{inventory_code},{edit_name},{inventory_category},{inventory_unit},{inventory_price},{inventory_quantity},{inventory_min_quantity}\n"
                lines[i] = new_code_line
                break

            elif choose_edit =="3":
                while True:
                    edit_category = input("Please enter new category : ")
                    if edit_category != "":
                        break
                    else:
                        print("Please enter the category")

                new_code_line = f"{inventory_code},{inventory_name},{edit_category},{inventory_unit},{inventory_price},{inventory_quantity},{inventory_min_quantity}\n"
                lines[i] = new_code_line
                break

            elif choose_edit =="4":
                while True:
                    edit_unit = input("Please enter new unit : ")
                    if edit_unit in ("box","pieces","pack","bottle"):
                        break
                    else:
                        print("Please enter either box, pieces, pack or bottle")

                new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{edit_unit},{inventory_price},{inventory_quantity},{inventory_min_quantity}\n"
                lines[i] = new_code_line
                break

            elif choose_edit =="5":
                while True:
                    edit_price = input("Please enter new price : ")
                    format_edit_price = str(edit_price).strip()
                    if format_edit_price.count(".") == 1 and len(format_edit_price.split(".")[-1]) == 2 :
                        break
                    else:
                        print("Please enter in the format of 00.00")

                new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{inventory_unit},{edit_price},{inventory_quantity},{inventory_min_quantity}\n"
                lines[i] = new_code_line
                break

            elif choose_edit =="6":
                while True:
                    edit_quantity = input("Please enter new quantity : ")
                    if edit_quantity.isdigit():
                        break
                    else:
                        print("Please enter a number")

                new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{inventory_unit},{inventory_price},{edit_quantity},{inventory_min_quantity}\n"
                lines[i] = new_code_line
                break

            elif choose_edit =="7":
                while True:
                    edit_min_quantity = input("Please enter new minimum quantity : ")
                    if edit_min_quantity.isdigit():
                        break
                    else:
                        print("Please enter a number")

                new_code_line = f"{inventory_code},{inventory_name},{inventory_category},{inventory_unit},{inventory_price},{inventory_quantity},{edit_min_quantity}\n"
                lines[i] = new_code_line
                break
            

    with open("inventory.txt","w") as file :
        file.writelines(lines)
    
    print("Item update successful")
    print()

#Used to add users to userdata.txt
def Admin_add_user():
    while True:
        newtype = input("Please enter type of access : ")
        if newtype in ("admin","checker","purchaser"):
            break
        else:
            print("Please enter either admin, checker or purchaser")

    newlogin = input("Please enter new login : ")
    newpassword = input("Please enter new password : ")
    with open("userdata.txt", "a") as file:
        file.write(f"\n{newtype},{newlogin},{newpassword}")
    print("User has been added")
    print()
    print("-----------------------------------------")
    backtomainmenu = input("0 - back to main menu\nAny key to exit : ")
    if backtomainmenu == "0":
        main()
    else:
        print("Thank you have a good day!") 


#The main process
def main():
    if login_type == "admin":
        print("-----------------------------------------")
        print()
        print("welcome to grocery store inventory system")
        print("1 - Insert a new item")
        print("2 - Update item")
        print("3 - Delete item")
        print("4 - Stock taking")
        print("5 - View replenish list")
        print("6 - Stock replenishment")
        print("7 - Search item")
        print("8 - Add user")
        print("9 - To exit")
        print()
        print()
        print("-----------------------------------------")
        
        while True:
            firstinput = input("Please choose an option : ")
            if firstinput == "1":
                INSERT_NEW_ITEM()
                break
            elif firstinput == "2":
                UPDATE_ITEM()
                break
            elif firstinput == "3":
                DELETE_ITEM()
                break
            elif firstinput == "4":
                STOCK_TAKING()
                break
            elif firstinput == "5":
                VIEW_REPLENISH_LIST()
                break
            elif firstinput == "6":
                STOCK_REPLENISHMENT()
                break
            elif firstinput == "7":
                SEARCH_ITEM()
                break
            elif firstinput == "8":
                Admin_add_user()
                break
            elif firstinput == "9":
                print("-----------------------------------------")
                print("Thank you have a good day!")
                print("-----------------------------------------")
                break
            else:
                print("Invalid input")

    elif login_type =="purchaser":
        print("-----------------------------------------")
        print()
        print("welcome to grocery store inventory system")
        print("1 - View replenish list")
        print("2 - Stock replenishment")
        print("3 - Search item")
        print("9 - To exit")
        print()
        print()
        print("-----------------------------------------")

        while True:
            firstinput = input("Please choose an option : ")
            if firstinput == "1":
                VIEW_REPLENISH_LIST()
                break
            elif firstinput == "2":
                STOCK_REPLENISHMENT()
                break
            elif firstinput == "3":
                SEARCH_ITEM()
                break
            elif firstinput == "9":
                print("-----------------------------------------")
                print("Thank you have a good day!")
                print("-----------------------------------------")
                break
            else:
                print("Invalid input")

    elif login_type == "checker":
        print("-----------------------------------------")
        print()
        print("welcome to grocery store inventory system")
        print("1 - Stock taking")
        print("2 - Search item")
        print("9 - To exit")
        print()
        print()
        print("-----------------------------------------") 
        while True:
            firstinput = input("Please choose an option : ")
            if firstinput == "1":
                STOCK_TAKING()
                break
            elif firstinput == "2":
                SEARCH_ITEM()
                break
            elif firstinput == "9":
                print("-----------------------------------------")
                print("Thank you have a good day!")
                print("-----------------------------------------")
                break
            else:
                print("Invalid input")

#Start with the login then when the login process is done we get to keep the user type and continue to the main process
login_type = authen()
main()