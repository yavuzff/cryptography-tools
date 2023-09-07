
def atbash(encrypt,text, alphabet = 'abcdefghijklmnopqrstuvwxyz'):
    key = alphabet[::-1] #reverses the alphabet

    newText = alphabetSub(encrypt,key,text,alphabet) #substitution performed with reversed alphabet
    return newText

def affine(encrypt,text,a,b, alphabet = 'abcdefghijklmnopqrstuvwxyz'):#inputting key
    newalphabet = ''
    for i in range(0,len(alphabet)):
        index= (a*i+b)% len(alphabet) #the index of the letter is calculated using a and b
        newalphabet += alphabet[index] #new letter added to the substitution alphabet

    print(newalphabet)
    
    newText = alphabetSub(encrypt,newalphabet,text)

    return newText

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
