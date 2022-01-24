import math         #math.ceil used in transposition
import numpy        #used for matrix values (can remove this)
#import secrets      #used for generating random numbers

alpha = 'abcdefghijklmnopqrstuvwxyz'
#automatic copying:r.clipboard_clear() , r.clipboard_append('i can has clipboardz?')

#Text Manipulation

def convertCase(text, upper): #converts input text to all upper or lowercase
    if upper:
        return text.upper()
        #changes letters to uppercase, ignores numbers/symbols
    else:
        return text.lower()


def addSpaces(text, n): #adds spaces at every n blocks
    text = text.replace(' ','') #all of the current spaces are removed
    
    if n == 0: #if value for n not entered, all spaces are removed
        return text
    
    new = ''
    for i in range (0, len(text)): #loops through whole text
        new = new + text[i] #adds letter to the new variable

        if (i+1) % n == 0: #if next item is a multiple of n, add space
            new = new + ' '
    return new.rstrip()

def validateAddSpaces(text, n): #validates the inputs to the addSpaces() function
    
    if not n.isdigit() or len(text) == 0: #isdigit checks whether a string is an "integer"
        return False #boolean returned to show whether the inputs are valid
    
    else:
        return True 


#Ciphers
#all ciphers input in this format: Boolean: encrypt, string: key, string: text

def alphabetSub(encrypt,key,text,orig='abcdefghijklmnopqrstuvwxyz'):
    #the orig optional parameter will allow to specify extra symbols such as punctation

    key = key.upper()  #text and keys converted to upper case
    orig = orig.upper()
    text = text.upper()
    
    if encrypt: #dictionary if encrypting
        mappings = dict(zip(list(orig),list(key)))
    else:       #dictionary if decrypting
        mappings = dict(zip(list(key),list(orig)))

    newText = ''
    for i in text:              #for each character in the text
        if i not in mappings:   #if it is not part of the key
            newText += i        #it is not encrypted
        else:
            newText += mappings[i]
            #the encrypted version from the hash table retrieved

    return newText

def validateAlphabetKey(alphabet,orig='abcdefghijklmnopqrstuvwxyz'):
    if len(alphabet) != len(orig): #the alphabet lengths must match to be valid
        return False
    return True

    
def keywordSub(encrypt, keyword, text, alphabet="abcdefghijklmnopqrstuvwxyz"): #optional alphabet can be used

#generating key
    keyword = keyword.lower()
    keyword = keyword.replace(' ','')
    key = ''

    #Refactored Approach
    seen = {} #dictionary used to store whether a character is already seen or not
    
    #adding letters in the keyword to the key
    for i in keyword+alphabet: #the keyword is added to the start of the key
        if i not in seen: #ensures no duplicate letters in key
            key += i
            seen[i] = True

##  #Old approach - which is discarded as approach 1 is more efficient
##    #adding letters in the keyword to the key
##    for i in keyword: #the keyword is added to the start of the key
##        if i not in key: #ensures no duplicate letters in key
##            key += i
##            
##    #adding rest of the letters
##    for i in alphabet:  #for each letter in the alphabet
##        if i not in keyword: 
##            key += i    #it is added to the key if not in the keyword

    #print(key)
    #performing the substitution using the alphabetSub module       
    newText = alphabetSub(encrypt,key, text)

    return newText


def caesar (encrypt,shift,text, alphabet="abcdefghijklmnopqrstuvwxyz"): #key is a number
    shift = shift % len(alphabet) #lengths greater than the length of alphabet are handled

    #generating alphabet key
    key = ''
    for i in range (0, len(alphabet)): #for each letter in the alphabet
        key += alphabet[(i+shift)%len(alphabet)] #the shifted version is added to the key

    #print(key)
    newText = alphabetSub(encrypt,key,text) #substitution is performed
        
    return newText

def crackCaesar(text, alphabet="abcdefghijklmnopqrstuvwxyz"): #goes through all possible caesar shifts
    possibilities = []
    
    for shift in range (1,len(alphabet)): #for each shift value (except 0)
        current = caesar(False, shift, text[:10], alphabet)
        #the caesar decryption is performed only on the first 10 characters of the text

        possibilities.append(current)

    #print(possibilities)
    for i in range (0,len(possibilities)):
        #each of the possibilities are output, including the shift value
        print ('Key ' + str(i+1)+ ': ' + possibilities[i])

    return possibilities

def validateCaesar(shift):
    #must have non-zero length, and must be an integer 
    if len(shift) != 0 and (shift.isdigit() or (shift[0] == '-' and shift[1:].isdigit())):
        return True
    return False

    
def affine(encrypt,text,a,b, alphabet = 'abcdefghijklmnopqrstuvwxyz'):#inputting key
    newalphabet = ''
    for i in range(0,len(alphabet)):
        index= (a*i+b)% len(alphabet) #the index of the letter is calculated using a and b
        newalphabet += alphabet[index] #new letter added to the substitution alphabet

    #print(newalphabet)
    
    newText = alphabetSub(encrypt,newalphabet,text)

    return newText

def validateAffine(a,b):
    if a.isdigit() and b.isdigit() and int(a)>0 and int(b)>0:
    #the inputs must both be integers greater than 0
        return True
    else:
        return False

def atbash(encrypt,text, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    key = alphabet[::-1] #reverses the alphabet

    newText = alphabetSub(encrypt,key,text,alphabet) #substitution performed with reversed alphabet
    return newText

def atbashValidate(alphabet): #there should be no duplicate letters in the alphabet
    if len(set(alphabet)) == len(alphabet): #set has no duplicates
        return True
    else:
        return False
    
##def affineDecode(a,b,message):
##    a_new = multInverse(a,26)
##    newalphabet = ''
##    for i in range (0,26):
##        index = (a_new * (i-b))%26
##        newalphabet += alphabet[index]
##
##    output = ''
##    for i in message:
##        output += newalphabet[alphabet.index(i)]
##    print(output)
##        

#multInverse function used here as well


    
def morse(encrypt,text):
##    morseCode = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
##                    'F':'..-.', 'G':'--.', 'H':'....',
##                    'I':'..', 'J':'.---', 'K':'-.-',
##                    'L':'.-..', 'M':'--', 'N':'-.',
##                    'O':'---', 'P':'.--.', 'Q':'--.-',
##                    'R':'.-.', 'S':'...', 'T':'-',
##                    'U':'..-', 'V':'...-', 'W':'.--',
##                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
##                    '1':'.----', '2':'..---', '3':'...--',
##                    '4':'....-', '5':'.....', '6':'-....',
##                    '7':'--...', '8':'---..', '9':'----.',
##                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
##                    '?':'..--..', '/':'-..-.', '-':'-....-',
##                    '(':'-.--.', ')':'-.--.-'}
    
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '?', '/', '-', '(', ')']
    code = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----', '--..--', '.-.-.-', '..--..', '-..-.', '-....-', '-.--.', '-.--.-']
    #each letter and their morse code
    
    text = text.upper() #text is converted to uppercase
    if encrypt: #dictionary if encrypting
        mappings = dict(zip(list(alphabet),list(code))) #dictionary formed 
        
        new = ''
        for i in text: #for each character in text
            if i not in mappings: #if it is an unknown character
                if i == ' ':
                    new += '/' #if it is a space, | symbol is added to indicate space
                else:
                    new += i #else the letter itself is added
            else:
                new += mappings[i] #if the letter is known, its morse code version is added
            new += ' ' # a space is added after each letter code
            
    else: #decrypting
        mappings = dict(zip(list(code),list(alphabet))) #dictionary formed
        if '|' in text:
            text = text.split('|')  #text is split into words based on the space indicators
        elif '/' in text:           #space indicators are usually / or |
            text = text.split('/')
        else:
            text = [text]
            #text is converted to this format so the iteration works as expected

        new = ''
        for word in text: #for each word in the text
            letters = word.split() #the letters are split
            for i in letters:
                if i not in mappings: #checks whether the code is valid
                    return False #if not decryption is terminated
                else:
                    new += mappings[i] #each letter is decoded
                
            new += ' ' #space added after each word
            
    return new.rstrip()#the extra space at the end is removed

#Vigenere

#key must only contain letters in alphabet, key must be non-zero length
def vigenere(encrypt, key, text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text.upper() #key and text sanitised
    key = key.upper()
    
    shifts = [] # stores the shift value for each letter of key
    for i in key:
        shifts.append(alphabet.index(i)) #the index of letter in key is added

    new = ''
    currentKey = 0 #stores index of the current letter of key

    for i in text: #loops for each character in text
        if i not in alphabet: #if it is not in the alphabet, it is added without encryption
            new += i
        else:
            if encrypt: index = (alphabet.index(i) + shifts[currentKey]) #index of key added 
            else:       index = (alphabet.index(i) - shifts[currentKey]) #index of key subtracted if decrypting

            index = index % len(alphabet)
            new += alphabet[index]

            currentKey = (currentKey + 1) % len(key) #incremented to point to next letter in key

    return new

def validateVigenere(key):
    if len(key) == 0: #presence check
        return False
    for i in key:
         #checks whether the key consists of only letters
        if i not in 'abcdefghijklmnopqrstuvwxyz':
            return False
    return True

#Hill

#matrix must have an inverse
#text must contain only letters in alphabet

def hill (encrypt, keymatrix, text, alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    text = text.upper() #text is sanitised
    removeLast = False      #indicates whether there is an extra character

    #counting the number of valid characters in the text
    count = 0 
    for i in text:
        if i in alphabet: #only counts chars in the alphabet
            count += 1
            
    if count % 2 == 1:  #if there is an even number of characters
        text = text + 'Z'   #a placeholder z is added
        removeLast = True   #flag set to true

    
    matrix = keymatrix % len(alphabet)
    divisor = 1

    #initially numpy.linalg.inv didnt work as the division resulted in floating point
    #errors, instead the division is not performed until after matrix-vector
    #multiplication takes place. so the inverse process is now done manually
    #instead of using an external library.
    #now uses multiplicative inverse of number instead of 1/determinant
    if not encrypt:     #if decrypting
        #matrix = numpy.linalg.inv(keymatrix) % len(alphabet) #matrix is set to the inverse of the key
        #print(matrix)
        
        matrix[0][0],matrix[1][1] = keymatrix[1][1],keymatrix[0][0] #the a and d values are swapped
        matrix[0][1],matrix[1][0] = -matrix[0][1], -matrix[1][0] #the b and c values are negated
        matrix = matrix % len(alphabet) #matrix converted back to modulo alphabetlength
        
        determinant = keymatrix[0][0] * keymatrix[1][1] - keymatrix[0][1] * keymatrix[1][0]
        determinant = determinant % len(alphabet) #determinant calculated modulo 26
    
        matrix = matrix*multInverse(determinant,len(alphabet))
        #the inverse matrix is formed by the multiplicative inverse multiplied by the adjugate matrix

        
    encrypted = 0 #stores the index of the next char to be encrypted 
    new = '' #stores the output text
    
    while encrypted < len(text): #loops while not all chars are encrypted
        
        pair = ['','']  #stores values for the vector
        index = 0       #stores the index of the first empty position in vector 
        mid = []        #stores the chars that are not in the alphabet that occur between 2 valid chars

        while pair[1] == '' and encrypted < len(text): #loops while the 2 values for the vector are not found

            if text[encrypted] not in alphabet: #if current char is not in alphabet
                if index == 0:
                    new += text[encrypted] #if there is no valid char before it, it is added to text straight away 
                else:   #if vector index 0 is already filled
                    mid.append(text[encrypted])

            else: #if it is a valid character
                pair[index] = text[encrypted] #it is added to the next space in vector
                index += 1

            encrypted += 1

        if pair[0] != '' and pair[1]!='': #if there are values for the vector
            
            vector = numpy.array([[alphabet.index(pair[0])], #vector is formed
                                  [alphabet.index(pair[1])]]) 

            image = ( matrix @ vector ) #% len(alphabet) #matrix multiplication occurs, to produce image of indices
            new += alphabet[image[0][0]%len(alphabet)] #the letter at image index a is added

            for i in mid:
                new += i
                
            new += alphabet[image[1][0]%len(alphabet)] #the letter at image index b is added

            #print(vector,new)

    if removeLast: #if there was an extra z at the end,
        new = new[:-1] #the last character is removed
        
    return new

#returns multiplicative inverse of a number
def multInverse(a,n): #n is the length of alphabet
    for i in range (1,n+1):
        value = (((i*n)+1)/a)
        if value.is_integer():
            return int(value)


def validateHillOld(a,b,c,d): #checks if a matrix is invertible

    #the validateCaesar module is reused by checking if the entries are integers.
    if not (validateCaesar(a) and validateCaesar(b) and validateCaesar(c) and validateCaesar(d)):
        return 'Error: Entries must be integers'
    
    a = int(a) #valid entries, converted to integers
    b = int(b)
    c = int(c)
    d = int(d)
    
    matrix = numpy.array([[a,b],
                          [c,d]]) #this is the form of the matrix

    determinant = a*d - b*c #the determinant is calculated

    if determinant == 0: #if it is 0, there is no inverse matrix
        return 'Error: Matrix is not invertible'
    else:
        return matrix

    
def validateHill(a,b,c,d,alphabetLength): #checks if a matrix is valid and invertible modulo n
    if not (validateCaesar(a) and validateCaesar(b) and validateCaesar(c) and validateCaesar(d)):
        return 'Invalid Matrix: Entries must be integers'
    
    a = int(a) #valid entries, cast to integers
    b = int(b)
    c = int(c)
    d = int(d)

    matrix = numpy.array([[a,b],
                          [c,d]]) #this is the form of the matrix
    determinant = a*d - b*c #the determinant is calculated
    nums = primeFactors(alphabetLength)
    
    #checking if determinant is relatively prime with alphabet length
    for i in nums:
        if determinant % i == 0:
            return 'Invalid Matrix: The determinant of the matrix must be relatively prime with the alphabet length.\nTry 2 3 1 2'
        
    return True

def primeFactors(n):
    i = 2 #first prime is 2
    factors = set()
    while i * i <= n:   #checks every prime factor up the square root of n
        if n % i != 0:  #if it is not divisible by i
            i += 1      #increment i
        else:
            n = n // i  #divide n by i
            factors.add(i) #i is a prime factor
            
    if n > 1: #if left with a prime factor, add it to the set as well
        factors.add(n)
        
    return factors


def testHill(a,b,c,d,text): #used for testing
    validation = validateHill(a,b,c,d,26) #input is validated
    
    if validation == True:
        #the matrix is generated
        m= numpy.array([[int(a),int(b)],[int(c),int(d)]])%26
        encrypted = hill(1,m,text)
        print('Encrypting:', encrypted)
        print('Decrypting:',hill(0,m,encrypted))
        
    else:
        return False



#Columnar Transposition

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
  
def validateTransposition(key, text):
    if len(key.replace(' ','')) == 0 or len(text.replace(' ','')) == 0:
        return False
    return True

#Row Transposition

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


def rowTransposition(encrypt,key,text):
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

    
def testTransposition(key,text):
	print('Encrypting: ',rowTransposition(1,key,text))
	print('Decrypting: ',rowTransposition(0,key,rowTransposition(1,key,text)))

	
#One Time Pad

def generateKey(n): #function to generate a random series of bytes
    keyBytes = []

    for i in range(0,n): #loops for each character
        byte = ''

        for i in range (0,8): #for each bit in the byte
            randomBit = secrets.choice(['0','1']) #0 or 1 is picked randomly
            byte += randomBit
            
        keyBytes.append(byte) #the byte is added to the output
            
    return keyBytes

def XOR(a,b):   #XORs two strings of binary digits
    output = []

    for i in range (0,len(a)): #loops through every byte
        byte1 = a[i]
        byte2 = b[i]
        outputByte = ''
        
        for j in range(0,len(byte1)): #loops through each bit
            bit = int(byte1[j]) ^ int(byte2[j]) #the bits are xored
            outputByte += str(bit)

        output.append(outputByte)

    return output

def OTPEncrypt(text):
    n = len(text)
    
    binary = []
    for i in text: #for each character in text
        #the byte version of the digit is added
        binary.append(format(ord(i),'b').zfill(8)) 
                        
    #binary = ' '.join(byteList)
    key = generateKey(n) #random key is generated
    
    output = XOR(binary,key)
    
    #print('Text:',' '.join(binary))
    #print('Key:',' '.join(key))
    #print('Output: ',' '.join(output))

    return (' '.join(output),key)


def OTPDecrypt(binaryText,key): #decrypts using two binary sequences
    output = XOR(binaryText.split(),key.split()) #the two are xored

    outputText = ''
    for byte in output:
        number = int(byte,2) #the byte is converted to an integer
        outputText += chr(number) #the ascii value is converted to character

    return outputText
    


#Cipher Plug-in

import importlib                       #used to import a file using a string name
#from mycipher import *                 #use this if file name is not string

#myfile = 'mycipher'
#text = 'hello world'
#key = 'fermat'
    
def cipherPlugin(file,encrypt,key,text):
    module = importlib.import_module(file) #the file is imported

    #hasattr checks whether the function exists in the imported file
    if encrypt and hasattr(module,'encrypt'): 
            output = module.encrypt(key,text) #the encrypt function in the file is called
            
    elif not encrypt and hasattr(module,'decrypt'):
        output = module.encrypt(key,text) #the encrypt function in the file is called
        
    else: #if the file doesnt have the required function
        return False

    return output



#Text Analysis:

def validateAnalysedText(text,n='1'):
    if len(text.replace(' ','')) == 0: #checks if the text is valid
        return False
    elif (not n.isdigit()) or int(n)==0: #checks if n is valid
        return False
    else:
        return True

#Frequency Analysis

def charFreq(text,onlyAlpha=True,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'): #finds and adds to a dictionary of each char in text
    letters = {}
    text = text.upper()
    total = 0
    #loop through the text, increasing value each time
    if onlyAlpha:
        for char in text:
            if char in alphabet:
                total += 1
                letters[char] = letters.get(char,0) + 1
    else:
        for char in text:
            total += 1
            letters[char] = letters.get(char,0) + 1

    frequencies = []
    for k,v in letters.items():
        frequencies.append((v,round(v/total*100,2),k))
        
    frequencies.sort(reverse = True) #sorted list of tuples for each letter

    return frequencies

letters = list('ETAONIHSRLDUCMWYFGPBVKJXQZ'.lower())
freq = '12.60 9.37 8.34 7.70 6.80 6.71 6.11 6.11 5.68 4.24 4.14 2.85 2.73 2.53 2.34 2.04 2.03 1.92 1.66 1.54 1.06 0.87 0.23 0.20 0.09 0.06'.split()
english = [float(x) for x in freq]


#N-gram Count

#an n-gram is a block of length n
#this tool counts the number of times each block of n occurs in a text
#e.g. the most common trigram in english is 'the'

def ngramCounter(text,n,overlap=True): #n is block size, overlap boolean stores whether blocks overlap with each other

    ngrams = {} #dictionary stores the number of appearances of each ngram
    text = text.upper().replace(' ','') #text is sanitised, spaces are ignored
    if not overlap:
        blocks = addSpaces(text,n).split() #text is split into blocks of n

        for i in blocks:
            ngrams[i] = ngrams.get(i,0) + 1 #the count of a block is incremented

    else: #there is no overlap
        for i in range(0,len(text)+1-n): # the starting index of each block is iterated
            block = text[i:i+n]
            ngrams[block] = ngrams.get(block,0) + 1

    counts = []
    for k,v in ngrams.items():
        counts.append((v,k)) #the dictionary is converted to a 2d-list to sort
        
    counts.sort(reverse = True) #sorted list of tuples for each letter
    
    return counts #sorted list is returned


#if this file is run directly, the text-based prototype is run
if __name__ == "__main__":
    print("Welcome to the text-based prototype.")
    #menu displays all of the tools
    menu = "1  - Add spaces\n2  - Convert to upper/lowercase\n3  - Frequency Analysis\n4  - N-gram Counter\n5  - Caesar Cipher\n6  - Affine Cipher\n7  - Atbash Cipher\n8  - Morse Code\n9  - Keyword Substitution\n10 - Alphabet Substitution\n11 - Columnar Transposition\n12 - Row Transposition\n13 - Vigenere Cipher\n14 - Hill Cipher\n15 - Quit"
    replay = True #allows user to re-use the tools

    while replay: #loops while the user wants to continue
        choice = ''
        print ("Enter the number for the tool you want to use.\n"+menu)
        choice = input('> ')
        
        #checks if choice is a valid integer
        while (not choice.isdigit()) or int(choice)>15 or int(choice)<1 :
            print("Please enter a number in the range 1-15\n"+menu)
            choice = input('> ')
        choice = int(choice)
            
        if choice == 1: #add spaces
            text = input("Enter text to be manipulated.\n> ")
            n = int(input("Add spaces at every how many characters?\n> "))
            print(addSpaces(text,n))
            
        elif choice == 2: #convert upper/lowercase
            text = input("Enter text to be manipulated.\n> ")
            case = input("Convert to uppercase (u) or lowercase (l)?").strip().lower()[0]
            if case == 'u':
                print(convertCase(text,True))
            else:
                print(convertCase(text,False))

        elif choice == 3: #frequency analysis
            text = input("Enter text to be analysed.\n> ")
            freq = charFreq(text)
            for i in freq: #looping through each character and outputting its frequency
                print(i[2] +" "+ str(i[1]) + "%")

        elif choice == 4: #ngram counter
            text = input("Enter text to be analysed.\n> ")
            n = int(input("Enter the block size (n).\n> "))
            ngrams = ngramCounter(text,n)
            for i in ngrams:
                print(i[1]+" "+str(i[0]))

        elif 5<=choice<=14: #ciphers
            text = input("Enter text to be encrypted/decrypted.\n> ")
            process = input("Do you want to encrypt (e) or decrypt (d)?\n> ")
            if process.lower().strip()[0] == 'e':
                encrypt = True
            else:
                encrypt = False

            if choice == 5: #caesar cipher
                key = int(input("Enter alphabet shift.\n> "))
                print(caesar(encrypt,key,text))
    
            elif choice == 6: #affine cipher
                a = int(input("Enter value of a.\n> "))
                b = int(input("Enter value of b.\n> "))
                print(affine(encrypt,text,a,b))
             
            elif choice == 7: #atbash cipher
                print(atbash(encrypt,text))
                
            elif choice == 8: #morse code
                print(morse(encrypt,text))

            elif choice == 9: #keyword substitution
                key = input("Enter keyword.\n> ")
                print(keywordSub(encrypt,key,text))

            elif choice == 10: #alphabet subsitution
                key = input("Enter the substitution alphabet.\n> ")
                print(alphabetSub(encrypt,key,text))

            elif choice == 11: #columnar tranposition
                key = input("Enter the transposition keyword.\n> ")
                print(columnarTransposition(encrypt,key,text))

            elif choice == 12: #row tranposition
                key = input("Enter the transposition keyword.\n> ")
                print(rowTransposition(encrypt,key,text))
                
            elif choice == 13: #vigenere cipher
                key = input("Enter keyword.\n> ")
                print(vigenere(encrypt,key,text))

            elif choice == 14: #hill cipher
                result = ""
                while result != True: #loops until the input is valid
                    print(result)
                    a = input("Enter the top left entry of key matrix.\n> ")
                    b = input("Enter the top right entry of key matrix.\n> ")
                    c = input("Enter the bottom left entry of key matrix.\n> ")
                    d = input("Enter the bottom right entry of key matrix.\n> ")
                    result = validateHill(a,b,c,d,26) #the input is validated

                keymatrix = numpy.array([[int(a),int(b)],[int(c),int(d)]])
                #matrix must be numpy format
                print(hill(encrypt,keymatrix,text))
        
        replay = False
        if choice != 15:
            choice2 = input("Would you like to continue (c) or quit (q)?\n> ")
            if choice2.lower().strip()[0] != 'q':
                replay = True
            

        



