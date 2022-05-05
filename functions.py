import datetime
#This function displays a welcome message
def welcome():
    print("--------------------------------------------------------------------------")
    print("|\t\t\t\t\t\t\t\t\t |")
    print("| \t\t\tWelcome to Bike Management\t\t\t |")
    print("|\t\t\t\t\t\t\t\t\t |")
    print("--------------------------------------------------------------------------\n\n")


#this function will check if stock is already there and will return another name for stock
def getStockName():
    id = '1'
    loop = True
    while loop:
        name = 'Stock '+id+'.txt'
        try:
            f = open(name)
        except IOError:
            return name
            loop = False
        else:
            id = str(int(id) + 1)
            f.close()



#this function will check if invoice is already there and will return another name for invoice
def getInvoiceName():
    id = '1'
    loop = True
    while loop:
        name = 'Invoice '+id+'.txt'
        try:
            f = open(name)
        except IOError:
            return name
            loop = False
        else:
            id = str(int(id) + 1)
            f.close()

def getTime():
    current_time = datetime.datetime.now()
    now = str(current_time.year)+"/"+str(current_time.month)+"/"+str(current_time.day)+" : "+str(current_time.hour)+":"+str(current_time.minute)
    return now

#This function takes input price from user and checks if it's a valid price or not
def validPrice(text):
    price = input(text)
    try:
        price = int(price.replace('$',''))
    except:
        print('\nPrice can only contain numbers and $ (dollar) sign. Please try again!\n')
        price = validPrice(text).replace('$','')
    return '$'+str(price)


#This function will return 2d list for the csv file
def csv2list():
    with open('Bikes.csv', 'r') as f3:
        results = []
        for line in f3:
            words = line.split(',')
            results.append((words[0:]))
    return results


#this function will return the id of last bike added.
def getLastId():
    lastId = csv2list()[-1][0]
    return int(lastId)

#This function displays options, validate it and take the user to corrosponding function
def options():

    #Display all available options
    print("\nPress any of following number to select an option")
    print("1. Display Bikes")
    print("2. Add new Bike")
    print("3. Update Bikes")
    print("4. Order Bikes")
    print("5. Purchase Bikes")
    print("7. Show Purchase Invoice")
    print("8. Show Stock Invoice")
    print("9. Show Bikes in Sorted Order")
    print("10. Exit the Program\n")

    option = 0
    #Take an option from user until it's a valid option
    while not option in range(1,11):
        try:
            option = int(input("Enter your choice: "))
        except:
            print("\n\nPlease enter a valid number between 1-10:\n")



    #Check if the option is valid
    if option > 10 or option < 1:
        print("\nInvalid Option! Select only number listed below")
        options()
    elif(option == 1):
        displayBike()
    elif(option == 2):
        addBike()
    elif(option == 3):
        updateBike()
    elif(option == 4):
        addStock()
    elif(option == 5):
        purchaseBike()
    elif(option == 6):
        purchaseBike()
    elif(option == 7):
        showInvoice()
    elif(option == 8):
        showStock()
    elif(option == 9):
        sortBike()
    elif(option == 10):
        print("Good bye!")
        quit()


#This function will list all bikes from CSV
def showBike():
    results = csv2list()

    for v in results:
        id, name, brand, color, quantity, power, price = v
        print ("{:<5} {:<25} {:<50} {:<20} {:<10} {:<10} {:<10}".format('| '+id, '|  '+name, '|  '+brand, '|  '+color,'| '+quantity,'|  '+power,'|  '+price.replace('\n','')))
        print('+-----+-------------------------+--------------------------------------------------+--------------------+----------+----------+----------+')



#This function will display all the bikes from the CSV file
def displayBike():
    print("\n\n------------------")
    print("| Display  Bikes |")
    print("------------------\n")
    showBike()
    print('\n')
    options()

#This function will add new bike to CSV file
def addBike():
    print("\n\n----------------")
    print("- Add new Bike -")
    print("----------------\n\n")

    bikeId = getLastId() + 1
    bikeName = input("Enter the name of the bike: ")
    bikeBrand = input("Enter the brand of the bike: ")
    bikeColor = input("Enter the color of the bike: ")
    bikeQuantity = 0
    while not bikeQuantity > 0:
        try:
            bikeQuantity = int(input("Enter the quantity of the bike: "))
        except:
            print("\nPlease enter a valid number greater than 0\n")
    bikePower = input("Enter the engine power of the bike: ")
    bikePrice = validPrice("Enter the price of the bike: ")

    def add(id,name,brand,color,quantity,power,price):
        print("\n\nYou're trying to add new bike with following details:\nName: ",name,"\nBrand: ",brand,"\nColor: ",color,"\nQuantity: ",quantity,"\nEngine Power: ",power,"\nPrice: ",price)

        confirm = -1
        while not confirm in range(0,2):
            try:
                confirm = int(input("\nDo you wish to continue? Press 1 to confirm 0 to cancel: "))
            except:
                print("\nPlease enter 1 to confirm and 0 to cancel.")

        if confirm == 1:
            #Add to bike code Here
            data = str(str(id)+','+name+','+brand+','+color+','+str(quantity)+','+power+','+price+'\n')
            #print(data)
            with open('Bikes.csv', 'a') as f:
                f.write(data)

                #print('Coming soon')
            print('Your data have been saved\n\n')
            options()

        elif confirm == 0:
            print('Nothing has been saved\n\n')
            options()

        else:
            print('\nInvalid option, Please try again')


    print(add(bikeId,bikeName,bikeBrand,bikeColor,bikeQuantity,bikePower,bikePrice))

    options()


#this function will update any value or any bike
def updateBike():
        print("\n\n---------------")
        print("| Update Bike |")
        print("---------------\n")
        showBike()
        print('\n')

        whichBike = 0
        while not whichBike in range(1,getLastId()+1):
            try:
                whichBike = int(input("Enter the id of bike you want to update: "))
            except:
                print("\nPlease enter a valid number between 1 and " + str(getLastId()))


        print("\nPlease select one of options below:\n1. Update Name\n2. Update Brand\n3. Update Color\n4. Update Quantity\n5. Update Engine Power\n6. Update Price")

        whichData = 0
        while not whichData in range(1,7):
            try:
                whichData = int(input("Enter an option from above: "))
            except:
                print("\nPlease enter a valid option from above\n")

        newValue = input("Enter a new value for the field: ")

        results = csv2list()


        results[whichBike][whichData] = newValue

        with open('Bikes.csv', 'w') as f:
            data = ""
            for i in results:
                for j in i:
                    data += j+","
                data = data[:-1]

            f.write(data)
            print("\nThe selected bike has been updated successfully!\n")

        options()


#This function will purchase a bike, subtract stock of purchased bike, generate note of purchased bike
def purchaseBike():
    print("\n\n----------------------")
    print("|  Purchase  Bikes   |")
    print("----------------------\n")
    name = input("\nEnter the name of the buyer: ")
    address = input("\nEnter the address of the buyer: ")
    contact = input("\nEnter the contact of the buyer: ")
    date = getTime()

    invName = getInvoiceName()
    buyMore = True
    allBike = {}
    while buyMore:
        showBike()

        bike = 0
        while not bike in range(1,getLastId()+1):
            try:
                bike = int(input("\nEnter the id of bike you want to purchase: "))
            except:
                print("\nPlease enter a valid bike id\n")
        bikeQ = 0
        while not bikeQ > 0:
            try:
                bikeQ = int(input("\nEnter the total quantity you want to purchase: "))
            except:
                print("\nPlease enter a valid number for quantity\n")

        if bikeQ > int(csv2list()[bike][4]):
            print("\nSorry, We do not have enough quantity in our stock. Please try with fewer bikes.\n\n")
        else:

            results = csv2list()
            results[bike][4] = str(int(results[bike][4]) - bikeQ)
            with open('Bikes.csv', 'w') as f2:
                data = ""
                for i in results:
                    for j in i:
                        data += str(j)+","
                    data = data[:-1]
                f2.write(data)

            allBike.update({bike:bikeQ})
            print("\nBike added for purchase.")
            print("\nDo you want to purchase more bikes? Press 1 for Yes and 0 for No\n")
            yesno = 3
            while not yesno in range(0,2):
                try:
                    yesno = int(input(": "))
                except:
                    print('\nPlease enter 1 for yes and 0 for no. There\n no other option')
            if yesno == 0:
                buyMore = False

        with open(invName, 'w') as f:
            f.write('Buyer Name: ' + name + '\nBuyer Address: ' + address + '\nBuyer Contact: ' + contact + '\nPurchase Date: ' + date + '\n\n\nBikes Purchased:\n---------------------------------------------------------\n')

        grandTotal = 0
        for i in allBike:
            with open(invName, 'a') as f:
                f.write('Bike Name: ' + results[i][1] + '\nBike Color: ' + results[i][3] + '\nBike Engine Power: ' + results[i][5] + '\nUnit Price: ' + results[i][6] + 'Quantity: ' + str(allBike[i]) + '\nTotal Amount: $' + str(int(results[i][6].replace('$',''))*allBike[i]) + '\n---------------------------------------------------------\n')
            grandTotal = grandTotal + int(results[i][6].replace('$',''))*allBike[i]

        with open(invName, 'a') as f:
            f.write('\nGrand Total: $' + str(grandTotal))

        print('\n\n Your selected bikes were purchased successfully. \n')
        #print(allBike)

    options()


#This function will add stock to
def addStock():
    print("\n\n------------------")
    print("|   Add  Stock   |")
    print("------------------\n")
    name = input("\nEnter the name of the Distributor: ")
    address = input("\nEnter the address of the Distributor: ")
    contact = input("\nEnter the contact of the Distributor: ")
    date = getTime()

    stockName = getStockName()
    addMore = True
    allBike = {}
    while addMore:
        showBike()
        bikeDetails = []
        bike = 0
        while not bike in range(1,getLastId()+1):
            try:
                bike = int(input("\nEnter the id of bike you want to order: "))
            except:
                print("\nPlease enter a valid bike id\n")
        bikeQ = 0
        while not bikeQ > 0:
            try:
                bikeQ = int(input("\nEnter the total quantity you want to order: "))
            except:
                print("\nPlease enter a valid number for quantity\n")
        ship = input("\nEnter the name of the Shipping Company: ")
        shipCost = validPrice("\nEnter the shipping Cost: ")
        bikeDetails = [bikeQ,ship,shipCost.replace('$','')]


        results = csv2list()
        results[bike][4] = str(int(results[bike][4]) + bikeQ)
        with open('Bikes.csv', 'w') as f2:
            data = ""
            for i in results:
                for j in i:
                    data += str(j)+","
                data = data[:-1]
            f2.write(data)

        allBike.update({bike:bikeDetails})
        print("\nBike added to the stock.")
        print("\nDo you want to order more bikes? Press 1 for Yes and 0 for No\n")
        yesno = int(input(": "))
        if yesno == 0:
            addMore = False

        with open(stockName, 'w') as f:
            f.write('Distributor Name: ' + name + '\nDistributor Address: ' + address + '\nDistributor Contact' + contact + '\nTransation Date: ' + date + '\n\n\nBikes Added:\n---------------------------------------------------------\n')

        grandTotal = 0
        for i in allBike:
            with open(stockName, 'a') as f:
                f.write('Bike Name: ' + results[i][1] + '\nBike Color: ' + results[i][3] + '\nBike Engine Power: ' + results[i][5] + '\nUnit Price: ' + results[i][6] + 'Quantity: ' + str(allBike[i][0]) + '\nTotal Amount: $' + str(int(results[i][6].replace('$',''))*allBike[i][0]) + '\nShipping Company' + allBike[i][1] + '\nShipping Cost: $' + allBike[i][2] +  '\n\n---------------------------------------------------------\n\n')
            grandTotal = grandTotal + int(results[i][6].replace('$',''))*allBike[i][0] + int(allBike[i][2])

        with open(stockName, 'a') as f:
            f.write('\nGrand Total: $' + str(grandTotal))

        print('\n\n Your selected bikes were added successfully. \n')
        #print(allBike)

    options()

#This function will display Purchase Invoice
def showInvoice():
    print("\n\n-------------------")
    print("| Show  Invoices  |")
    print("-------------------\n")
    inv = getInvoiceName()
    inv = inv.replace('Invoice ','')
    inv = inv.replace('.txt','')

    inv = int(inv) - 1

    if inv <= 0:
        print('\nSorry, There isn\'t any invoice. Purchase some bike and try again.\n')
    elif inv == 1:
        print("\n\nThere is only one Invoice. Displaying it: \n")
        with open("Invoice 1.txt", "r") as f:
            for line in f:
                print(line.strip())
    else:
        print("Enter invoice Id between 1 and " + str(inv))
        invId = 0
        while not invId in range(1,inv+1):
            try:
                invId = int(input(": "))
            except:
                print("\n\nPlease enter a valid number between 1-"+str(inv))

        file = 'Invoice '+str(invId)+'.txt'
        print('\n\n\n')
        with open(file, "r") as f:
            for line in f:
                print(line.strip())
    print('\n\n\n')
    options()


#This function will display stock Invoice
def showStock():
    print("\n\n------------------")
    print("|  Show  Stocks  |")
    print("------------------\n")
    inv = getStockName()
    inv = inv.replace('Stock ','')
    inv = inv.replace('.txt','')

    inv = int(inv) - 1

    if inv <= 0:
        print('\nSorry, There isn\'t any Stock record. Add some bike and try again.\n')
    elif inv == 1:
        print("\n\nThere is only one Stock Record. Displaying it: \n")
        with open("Stock 1.txt", "r") as f:
            for line in f:
                print(line.strip())
    else:
        print("Enter Stock record Id between 1 and " + str(inv))
        invId = 0
        while not invId in range(1,inv+1):
            try:
                invId = int(input(": "))
            except:
                print("\n\nPlease enter a valid number between 1-"+str(inv))

        file = 'Stock '+str(invId)+'.txt'
        print('\n\n\n')
        with open(file, "r") as f:
            for line in f:
                print(line.strip())
    print('\n\n\n')
    options()

#This function will sort bikes according to user's choice
def sortBike():
    print("\n\n------------------")
    print("|  Sort  Bikes   |")
    print("------------------")
    print("\n\n1. Sort by Bike Name")
    print("\n2. Sort by Bike Company")
    print("\n3. Sort by Bike Color")
    print("\n4. Sort by Bike Quantity")
    print("\n5. Sort by Bike Power")
    print("\n6. Sort by Bike Price")

    sort = 0
    while not sort in range(1,7):
        try:
            sort = int(input("Enter your choice: "))
        except:
            print("\n\nPlease enter a valid number between 1-6:\n")

    results = csv2list()
    results.sort(key=lambda result: result[6])
    for v in results:
        id, name, brand, color, quantity, power, price = v
        print ("{:<4} {:<25} {:<50} {:<20} {:<10} {:<10} {:<10}".format(id, name, brand, color,quantity,power,price))

    options()
