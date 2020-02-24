#------------------------------------------#
# Title: Assignment05.py
# Desc: Script for Assignment 05 with Modication learned
# Change Log: (Who, When, What)
# Cyuen, 2020-Feb-23, Created File
# Cyuen, 2020-Feb-23, Replaced with Dictionary
# Cyuen, 2020-Feb-23, Add the Delete Selection
# Cyuen, 2020-Feb-24, Moditfied the Delete Selection 
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow ={}
#lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
l_data = False

# Get user Input
print()
print('Welcome to Carol\'s CD Collections\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 5. Exit the program if the user chooses so
        print('Thanks for Visiting, Good-Bye!')
        break
    
    if strChoice == 'l':
        print('Loading Data from File: ')
        print()
        lstTbl.clear() 
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID':int(lstRow[0]),'Artist': lstRow[1],'Title': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        # TODO Add the functionality of loading existing data
        
    elif strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 2. Add data to the table (2d-list) each time the user wants to add data
        print('Add CD: ')
        strID = input('Enter an ID: ')
        strArtist = input('Enter the Artist\'s Name: ')
        strTitle = input('Enter the CD\'s Title: ')
        intID = int(strID)
        dicRow = {'id':intID, 'artist': strArtist, 'title': strTitle}
        lstTbl.append(dicRow)
        print('\n', dicRow)
        
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, Artist, CD Title')
        for row in lstTbl:
            print(*row.values(), sep = ', ')    
        print()
            
    elif strChoice == 'd':
        # TODO Add functionality of deleting an entry
        print('Deleting an previous entry: ')
        term = int(input('What CD ID would you like to Delete? '))
        if term in row.values():
            del lstTbl[lstTbl.index(row)]
            print('ID has been deleted')
            print()
        else:
            print('Does not Exist, please select a different ID')
            print()
            
    elif strChoice == 's':
        # 4. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()   
    
    else:
        print('Please choose either l, a, i, d, s or x!')

