"""
Soumen Nath
ICS4U
SoumenNath_Name.py
Description: This program keeps track of the inventory for a car delearship in a csv file.
The user can enter, edit and view information in the inventory. The user is also able to purchase a vehilce.
"""
#import the following modules
import os; import os.path; import csv
#Variable to contain all the headers of the csv file
headers = ['Dealer Inventory Number', 'Auto VIN', 'Make', 'Model', 'Exterior Colour', 'Interior Colour', 'Transmission Type', 'Retail Price']
#menu function
def menu():
    selection = 0
    #Allow the user to choose from the following selection
    print('\t\t\t\t\t--------------------------------------------\n\t\t\t\t\tWelcome to Dealership Car Inventory Program\n\t\t\t\t\t--------------------------------------------\nPlease select an option:\nEnter new car into inventory\t\t\t1\nDisplay car inventory\t\t\t\t2\nSearch for vehicle (by inventory number)\t3\nPurchase a vehicle\t\t\t\t4\nEdit information for a car\t\t\t5\nExit the program\t\t\t\t6')
    while True:
        try:
            selection = int(input('Please enter your selection: '))
        except ValueError:
            print('Error!'); continue
        if selection<1 or selection>6:
            print('Error!'); continue
        else:
            break
    #Call on the following functions based on user input
    if selection ==1:
        os.system('cls'); enterCar()
    elif selection ==2:
        os.system('cls'); displayIn()
    elif selection ==3:
        os.system('cls'); searchV()
    elif selection ==4:
        os.system('cls'); buyVehicle()
    elif selection ==5:
        os.system('cls'); edit()
    #Exit the program if option 6 is chosen
    elif selection ==6:
        os.system('cls'); input('Thank you for using this program!'); os.system('cls'); exit()
#function to check if an acceptable colour was entered when asked
def colour(num):
    lColours = ['red', 'blue', 'yellow', 'black', 'white', 'gray']; cChecker = False
    while cChecker == False:
        if num == 1:
            entry = input('Please enter the exterior colour (press help to view list of acceptable colours): ')
        elif num == 2:
            entry = input('Please enter the interior colour (press help to view list of acceptable colours): ')
        if entry.lower() == 'help':
            print('\nList of acceptable colours: ')
            for row in lColours:
                print(row)
        for row in lColours:
            if entry.lower() == row:
                return entry.lower()
                cChecker = True
#Function to enter infomation for a new car
def enterCar():
    print('*Enter New Vehicle Into Inventory*\n')
    #open the file in append mode and write to it as if it is a dictionary
    with open('carInventory.csv', 'a', newline='') as csvFile:
            writeCSV= csv.DictWriter(csvFile, fieldnames=headers)
            #Ask for user input
            while True:
                try:
                    DIN = int(input('Please enter the Dealer Inventory Number: '))
                except ValueError:
                    print('Error!'); continue
                if DIN<1000 or DIN>9999:
                    print('Error!'); continue
                else:
                    break
            VIN = input('Please enter Auto VIN: ')
            while len(VIN) != 5:
                VIN = input('Error! Plase enter a VIN that is 5 digits and composed of text and numbers: ')
            make = input('Please enter Make: ')
            model = input('Please enter Model: ')
            exColour = colour(1)
            inColour = colour(2)
            tType = input('Please enter the transmission type (A/M): ')
            while tType.upper() != 'A' and tType.upper() != 'M':
                tType = input('Please enter the transmission type (A/M): ')
            while True:
                try:
                    rPrice = int(input('Please enter the retail price: '))
                except ValueError:
                    print('Error!'); continue
                if rPrice<0:
                    print('Error!'); continue
                else:
                    break
            writeCSV.writerow({'Dealer Inventory Number': str(DIN), 'Auto VIN': str(VIN), 'Make': make, 'Model': model, 'Exterior Colour': exColour, 'Interior Colour': inColour, 'Transmission Type': tType.upper(), 'Retail Price': '$'+str(rPrice)})
    input('Please press enter'); os.system('cls'); menu()
#function to display the entire inventory
def displayIn():
    print('\n*Car Inventory Display*\n')
    with open('carInventory.csv', 'r') as csvFile:
        readCSV = csv.DictReader(csvFile)
        for row in readCSV:
            print('--------------------------'+'\nDealer Inventory Number:',row['Dealer Inventory Number']+'\nAuto VIN:', row['Auto VIN']+'\nMake:', row['Make']+'\nModel:', row['Model']+'\nExterior Colour:', row['Exterior Colour']+'\nInterior Colour:', row['Interior Colour']+'\nTransmission Type:', row['Transmission Type']+'\nRetail Price:', row['Retail Price'])
            print('--------------------------\n')
    input('Please press enter'); os.system('cls'); menu()
#Function to search for a specific vehicle
def searchV():
    while True:
        try:
            DIN = int(input('Please enter the Dealer Inventory Number: '))
        except ValueError:
            print('Error!'); continue
        if DIN<1000 or DIN>9999:
            print('Error!'); continue
        else:
            break
    #open the file in read mode and check if the vehicle is in the inventory. If it is found then display its information.
    with open('carInventory.csv', 'r') as csvFile:
        readCSV = csv.DictReader(csvFile); checker = False
        for row in readCSV:
            if str(DIN) == row['Dealer Inventory Number']:
                print('\n--------------------------'+'\nDealer Inventory Number:',row['Dealer Inventory Number']+'\nAuto VIN:', row['Auto VIN']+'\nMake:', row['Make']+'\nModel', row['Model']+'\nExterior Colour', row['Exterior Colour']+'\nInterior Colour', 'Interior Colour'+'\nTransmission Type', row['Transmission Type']+'\nRetail Price', row['Retail Price'])
                print('--------------------------\n')
                checker = True
    #display an error message if a vehicle is not in the inventory
    if checker == False:
        print('Error! No results found.')
    input('Please press enter'); os.system('cls'); menu()
#Function to buy a vehicle
def buyVehicle():
    #variables to keep track of which row to delete
    numRow = 0; delR = 0
    while True:
        try:
            DIN = int(input('Please enter the Dealer Inventory Number of the vehicle you would like to purchase: '))
        except ValueError:
            print('Error!'); continue
        if DIN<1000 or DIN>9999:
            print('Error!'); continue
        else:
            break
    #open the file in read mode and check if the vehicle is in the inventory. If it is found then allow the user to purchase it.
    with open('carInventory.csv', 'r') as csvFile:
        readCSV = csv.DictReader(csvFile); checker = False
        for row in readCSV:
            numRow+=1
            if str(DIN) == row['Dealer Inventory Number']:
                print('\nVehicle: ', row['Make'], row['Model'] + '\nRetail Price:', row['Retail Price'])
                while True:
                    try:
                        cNum = int(input('Please enter your four digit credit card number: '))
                    except ValueError:
                        print('Error!'); continue
                    if cNum<1000 or cNum>9999:
                        print('Error!'); continue
                    else:
                        break
                print('Congratulations! Enjoy your new vehicle!')
                delR = numRow
                checker = True
    #display an error message if a vehicle is not in the inventory
    if checker == False:
        print('Error! No results found.')
    fo = open('carInventory.csv', 'r')
    inventory = fo.readlines()
    fo.close()
    if delR != 0:
        #remove the purchased vehicle from the inventory
        del inventory[delR]
        fo = open('carInventory.csv', 'w')
        fo.writelines(inventory)
        fo.close()
    input('Please press enter'); os.system('cls'); menu()
#function to edit the information of the vehicles
def edit():
    numRow = 0; editR = 0; editItem = 0
    while True:
        try:
            DIN = int(input('Please enter the Dealer Inventory Number of the vehicle you would like to edit: '))
        except ValueError:
            print('Error!'); continue
        if DIN<1000 or DIN>9999:
            print('Error!'); continue
        else:
            break
    #open the file in read mode and check if the vehicle is in the inventory. If it is found then allow the user to edit its information.
    with open('carInventory.csv', 'r') as csvFile:
        readCSV = csv.DictReader(csvFile); checker = False
        print()
        for row in readCSV:
            numRow+=1
            if str(DIN) == row['Dealer Inventory Number']:
                print('\nDealer Inventory Number:',row['Dealer Inventory Number']+' \t\t1'+'\nAuto VIN:', row['Auto VIN']+' \t\t\t2'+'\nMake:', row['Make']+' \t\t\t\t3'+'\nModel:', row['Model']+' \t\t\t\t4')
                print('Exterior Colour:', row['Exterior Colour']+'\t\t\t5'+'\nInterior Colour:', row['Interior Colour']+' \t\t\t6'+'\nTransmission Type:', row['Transmission Type']+' \t\t\t7'+'\nRetail Price:', row['Retail Price']+' \t\t\t8')
                while True:
                    try:
                        editItem = int(input("please enter the number for the item you wish to edit: "))
                    except ValueError:
                        print('Error!'); continue
                    if editItem<1 or editItem>8:
                        print('Error!'); continue
                    else:
                        break
                changeV = input('Please enter the new value: ')
                editR = numRow; checker = True
    #display an error message if a vehicle is not in the inventory
    if checker == False:
        print('Error! No results found.')
    reader = csv.reader(open('carInventory.csv'))
    inventory = list(reader)
    if editR != 0:
        #write the new information into the proper cell in the csv file.
        inventory[editR][editItem-1] = str(changeV)
        with open('carInventory.csv', 'w', newline='') as csvFile:
            Writer = csv.writer(csvFile)
            for cell in inventory:
                Writer.writerow(cell)
    input('Please press enter'); os.system('cls'); menu()
#run the menu function if thecsv file exits. Otherwise create a new csv file in the directory and write the following iformation.
if os.path.exists('carInventory.csv'):
    menu()
elif os.path.exists('carInventory.csv') == False:
    file = open("carInventory.csv", "w", newline='')
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader() #write our header row with the fieldnames
    writer.writerow({'Dealer Inventory Number': 1134, 'Auto VIN': 'HG513', 'Make': 'Acura', 'Model': 'MDX', 'Exterior Colour': 'black', 'Interior Colour': 'gray', 'Transmission Type': 'A', 'Retail Price': '$42930'})
    writer.writerow({'Dealer Inventory Number': 1212, 'Auto VIN': 'GU322', 'Make': 'Yaris', 'Model': '6MT', 'Exterior Colour': 'white', 'Interior Colour': 'black', 'Transmission Type': 'M', 'Retail Price': '$17320'})
    writer.writerow({'Dealer Inventory Number': 1345, 'Auto VIN': 'ISM23', 'Make': 'Toyota', 'Model': 'CVT', 'Exterior Colour': 'white', 'Interior Colour': 'black', 'Transmission Type': 'A', 'Retail Price': '$20255'})
    file.close()
    menu()
