#Monoalphabetic substitution

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

#substitution using a keyword
def keywordSub(encrypt, keyword, text, alphabet="abcdefghijklmnopqrstuvwxyz"): #optional alphabet can be used
    #generating key
    keyword = keyword.lower()
    key = ''

    seen = {}
    
    #adding letters in the keyword to the key
    for i in keyword+alphabet: #the keyword is added to the start of the key
        if i not in seen: #ensures no duplicate letters in key
            key += i
            seen[i] = True
