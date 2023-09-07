#One Time Pad
import secrets      #used for generating random numbers

def OTPEncrypt(text): #input is text to enrypt,
                      #random key of the same length is generated 
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
    #print('Output:',' '.join(output))

    output = 'Text: '+ ' '.join(binary) + '\n' +'Key: ' +' '.join(key)+'\n'+'Output: '+' '.join(output)
    print (output)


def OTPDecrypt(binaryText,key): #decrypts by performing XOR on the two binary strings
    output = XOR(binaryText.split(),key.split()) #the two are xored

    outputText = ''
    for byte in output:
        number = int(byte,2) #the byte is converted to an integer
        outputText += chr(number) #the ascii value is converted to character

    return outputText

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
