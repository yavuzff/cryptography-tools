
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
