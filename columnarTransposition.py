import math


def columnarTransposition(encrypt,key,text):
    text = text.lower().replace(' ','') #text and key sanitised
    key = key.lower().replace(' ','')
    keylist = [ord(i) for i in key] #key converted to its ascii values
    table = generateTable(key,text) #the transposition table is generated
    
    if encrypt:
        filledTable = writeRows(text,table) #for encryption, table filled in rows
        return readColumns(keylist,filledTable)

    else:
        filledTable = writeColumns(text,keylist,table) #table filled in columns using the key
        return readRows(filledTable) #the table is read in rows


def generateTable(key,text):
    columnlength = math.ceil(len(text) / len(key))
    #ensures columnlength*keylength is >= to text length
    extraspaces = (len(key) - (len(text) % len(key))) % len(key)
    #the amount of extra spaces is calculated
    
    table = [['' for i in range (columnlength)] for i in range (len(key))]

    for i in range (extraspaces):
        #the empty spaces at the end of the columns are replaced with placeholder values
        table[len(table)-1-i][columnlength-1] = 'X'

    return table

    
#used for columnar encrypt  
def writeRows(text,table):
    #write to table in rows
    current = 0 #stores index of item in current row 
    index = 0 #stores index of current row
    
    for i in text:
        table[current][index] = i #the next availaible space in table is filled with the character
        current += 1
        
        if current == len(table): #if end of row is reached
            current = 0 #the item is set back to the start
            index += 1  #index incremented to point to next row
            
    return table

def readColumns(order,table): #table read in order of the key
    text = ''

    while min(order) != float('inf'): #loops until all characters of the key are visited
        current = min(order) #the lowest value of the key is extracted
        
        for i in range(0,len(order)): #all of the key is looped in case there are multiple lowest val
            if order[i] == current: #if this item is the lowest item
                
                for item in table[i]: #each character in the column is read
                    if item != 'X': #except it is a placeholder
                        text += item
                        
                order[i] = float('inf') #this part of the key is marked visited
                
    return text



#used for columnar decrypt          
def writeColumns(text,order,table): #table is written in columns depending on the key
    #write to table in columns
    currentLetter = 0 #stores index of the letter to be stored in the table 

    while min(order) != float('inf'): #loops until all of the key is used
        current = min(order)
        
        for i in range (0,len(order)):
            if order[i] == current: #for each of the lowest items
                index = 0           #holds the index of the current item in the column
                column = i          #holds index of the current column in table
                
                while index<len(table[column]) and table[column][index] != 'X':
                    #loops until end of table or placeholder value is reached
                    
                    table[column][index] = text[currentLetter] #each spot is set to the current letter
                    currentLetter += 1 
                    index += 1              #incremented to point to next spot
                    order[i] = float('inf') #key marked as visited
                    
    return table

def readRows(table): #reading the table by rows
    text = ''
    
    for i in range (0,len(table[0])):   #for each row
        for j in range (0,len(table)):  #for each column
            
            if table[j][i] != 'X':      #if item is not placeholder
                text += table[j][i]  #it is added to the decrypted text
                
    return text
  
