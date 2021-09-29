import numpy

def hill(encrypt,matrix,text,alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' ):
    m= numpy.array([[matrix[0][0],matrix[0][1]],[matrix[1][0],matrix[1][1]]]) % 26

    if isValid(m[0][0],m[0][1],m[1][0],m[1][1],len(alphabet)):
        encrypted = cipher(encrypt,m,text,alphabet)
        print(encrypted)
    


def cipher(encrypt, keymatrix, text, alphabet):
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

    if not encrypt:     #if decrypting
        #matrix = numpy.linalg.inv(keymatrix) % len(alphabet) #matrix is set to the inverse of the key
        #print(matrix)
        
        matrix[0][0],matrix[1][1] = keymatrix[1][1],keymatrix[0][0] #the a and d values are swapped
        matrix[0][1],matrix[1][0] = -matrix[0][1], -matrix[1][0] #the b and c values are negated
        matrix = matrix % len(alphabet) #matrix converted back to modulo alphabetlength
        
        determinant = keymatrix[0][0] * keymatrix[1][1] - keymatrix[0][1] * keymatrix[1][0]
        determinant = determinant % len(alphabet) #determinant calculated modulo 26
    
        matrix = matrix*modularInverse(determinant,len(alphabet))
        #the inverse matrix is formed by the modular inverse multiplied by the adjugate matrix

        
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

#returns modular inverse of a number
def muodularInverse(a,n): #n is length of alphabet
    for i in range (1,n+1):
        value = (((i*n)+1)/a)
        if value.is_integer():
            return int(value)


def isValid(a,b,c,d,alphabetLength): #checks if a matrix is invertible modulo n
    matrix = numpy.array([[a,b],
                          [c,d]]) #this is the form of the matrix
    determinant = a*d - b*c #the determinant is calculated
    nums = primeFactors(alphabetLength)

    #An nxn matrix A is invertible modulo m if and only if det A != 0 for
    #every prime divisor p of m
    
    #checking if determinant is relatively prime with alphabet length
    for i in nums:
        if determinant % i == 0:
            print('Matrix not valid:',determinant,i)
            return False
    
    return True

def primeFactors(n): #finds the prime factors of n
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


