#Vigenere

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
