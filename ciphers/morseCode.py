
def morse(encrypt,text):

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

        new = ''
        for word in text: #for each word in the text
            letters = word.split() #the letters are split
            for i in letters:
                new += mappings[i] #each letter is decoded
                
            new += ' ' #space added after each word
            
    return new.rstrip()#the extra space at the end is removed
