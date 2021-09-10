

def caesar (encrypt,shift,text, alphabet="abcdefghijklmnopqrstuvwxyz"): #key is a number
    shift = shift % len(alphabet) #lengths greater than the length of alphabet are handled

    #generating alphabet key
    key = ''
    for i in range (0, len(alphabet)): #for each letter in the alphabet
        key += alphabet[(i+shift)%len(alphabet)] #the shifted version is added to the key

    print(key)
    newText = alphabetSub(encrypt,key,text) #substitution is performed
        
    return newText

def caesarBrute(text, alphabet="abcdefghijklmnopqrstuvwxyz"): #goes through all possible caesar shifts
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
