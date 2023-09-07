import matplotlib.pyplot as plt

def inputData():
    #input and sanitize text data
    if not file:
        print('Enter text:')
        text = input('>')
        
    else:
        print('Enter file name')
        filename = input('>')
        myfile = open(filename)
        text = myfile.read()
        myfile.close()
    
    text = ''.join(text.split()).lower()
    if file:
        myfile = open(filename,'w')
        myfile.write(text)
        myfile.close()
    return text

def initLetters(): 
    #initialize the letters dictionary
    letters = {}
    for letter in alphabet: #each letter is added as we want to see all on graph
        letters[letter] = 0
    
    return letters

def charFreq(text,onlyAlpha): #finds and adds to a dictionary of each char in text
    letters = initLetters()
    #loop through the text, increasing value each time
    if onlyAlpha:
        for char in text:
            if char in alphabet:
                letters[char] += 1
    else:
        for char in text:
            letters[char] = letters.get(char,0) + 1
    print(letters)
    return letters
    
def dictToList(lettersDic):
    #adding the letter frequencies to a sorted list
    frequencies = []
    for k,v in lettersDic.items():
        frequencies.append((v,k))
        
    frequencies.sort(reverse = True) #sorted list of tuples for each letter

    return frequencies

def plotEnglishFreq(xvalues):
    #english frequency letter order and their fequencies
    letters = list('ETAONIHSRLDUCMWYFGPBVKJXQZ'.lower())
    freq = '12.02 9.10 8.12 7.68 7.31 6.95 6.28 6.02 5.92 4.32 3.98 2.88 2.71 2.61 2.30 2.11 2.09 2.03 1.82 1.49 1.11 0.69 0.17 0.11 0.10 0.07'.split()
    freq = '12.60 9.37 8.34 7.70 6.80 6.71 6.11 6.11 5.68 4.24 4.14 2.85 2.73 2.53 2.34 2.04 2.03 1.92 1.66 1.54 1.06 0.87 0.23 0.20 0.09 0.06'.split()
    freq = [float(x) for x in freq]

    #adding all of these to a dictionary
    data = {}
    for i in range (26):
        data[letters[i]] = freq[i]

    #the letters are ordered in order of the xvalues
    orderedFreq = []
    for i in xvalues:
        if i not in data:
            orderedFreq.append(0)
        else:
            orderedFreq.append(data[i])

    #these values are plotted onto the graph
    plt.plot(xvalues,orderedFreq,color = 'red')
    
alphabet = list('abcdefghijklmnopqrstuvwxyz')
onlyLetters = True #do you want the plot to have only letters are all char?
percentage = True #viewing frequencies as percentage or as absolute count
single = False #viewing for a single text or keeping on inputting text (multiple text)
file = False #enter file name

while True:
    text = inputData() #input text
        
    if text == 'done': break #break if done
    else:
        plt.clf() #clear the graph
        freqDict = charFreq(text,onlyLetters) #get the frquencies as a dictionary
        frequencies = dictToList(freqDict) #convert to list
        xval = [x[1] for x in frequencies] #the xvalues are swapped as the tuple is value key
        yval = [x[0] for x in frequencies]
        
        if not percentage: #if the user wants count
            plt.ylabel('Frequency as Count')
            plt.bar(xval,yval) #the normal data is plotted
            plt.legend(['Your text'])

        else: #if the user wants percentage
            plt.ylabel('Frequency as Percentage')
            total = sum(yval) 
            yval = [round(x*100/total,2) for x in yval] #the percentage for each is calculated

            plotEnglishFreq(xval) #the english frequencies are plotted
            plt.bar(xval,yval) #our data is plotted
            plt.legend(['English','Your text']) 
            
        plt.xlabel('Character') 
        plt.title('Frequency Analysis')
        
        if single: #if the user wants a single graph
            plt.show() #show the graph until user closes
            break
        else:
            plt.pause(3)# wait 3 seconds then allow user to reenter
            
