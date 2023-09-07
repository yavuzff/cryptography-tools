#Row Transposition

def rowTransposition(encrypt,key,text): #boolean encrypt
    text = text.lower().replace(' ','') #text and key are sanitised
    key = key.lower().replace(' ','')
    keylist = [ord(i) for i in key] #key converted to its ascii values
    
    order = [] #stores the order of row indices 
    while min(keylist) != float('inf'): #loops untill all nums are infinite
        current = min(keylist) #the current minimum of the list is found
        
        for i in range (0,len(keylist)): #list is searched linearly
            if keylist[i] == current: #if num is equal to the min val
                order.append(i) #the index of this num is appended to list 
                keylist[i] = float('inf') #item is set as visited
                
    table = rowTgenerateTable(key,text) #transposition table is generated

    if encrypt:
        filled = rowTfillTable(text,table)
        return rowTreadTable(order,filled)

    else:
        filled = rowTwriteTable(text,order,table)
        return rowTreadColumns(filled)


    
def rowTgenerateTable(key,text):
    columnlength = math.ceil(len(text) / len(key))
    #ensures columnlength*keylength is >= to text length
    extraspaces = (len(key) - (len(text) % len(key))) % len(key)
    #the amount of extra spaces is calculated
    
    table = [['' for i in range (columnlength)] for i in range (len(key))]

    column = len(table)-1 #stores column index
    row = columnlength- 1 #stores row index
    for i in range (extraspaces):
        #the empty spaces at the end of the rows are replaced with placeholder values
        table[column][row] = 'X' #table position is filled with placeholder 
        
        if row == 0: #if the whole column is filled
            column -= 1 #index points to previous column
            row = columnlength - 1 #points to the lowest row
        else:
            row = row - 1 

    return table

def rowTfillTable(text,table): #writing to table in columns
    letter = 0 #stores the current letter index

    for column in table: #loops through each column
        for i in range (0,len(column)): #for each element in the column
            if column[i] != 'X': #if it is not meant to be empty
                column[i] = text[letter] #it is filled with a letter
                letter += 1

    return table

def rowTreadTable(order,table): #reading table in rows
    text = ''

    for i in range (0,len(table[0])): #for each row length
        for index in (order): #loops through in order of key
            if table[index][i] != 'X':
                text += table[index][i] #the item at this index in row is added to text
    return text


#decrypting row transposition
def rowTwriteTable(text,order,table): #writing in rows
    currentLetter = 0

    for i in range (0,len(table[0])): #for each column
        for index in order: #for each row index
            if table[index][i] != 'X':
                table[index][i] = text[currentLetter] #the row is filled 
                currentLetter += 1
    return table

def rowTreadColumns(table): #reading in columns
    text = ''
    for column in table: #for each column
        for i in range (0,len(column)): #for each item in column
            if column[i] != 'X':
                text += column[i] #the symbol is added to the text

    return text

