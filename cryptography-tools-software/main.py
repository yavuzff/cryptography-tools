#Source code for the interface
import tkinter  #used for GUI
import textwrap #used for tool info label at the bottom
import sys      #used to exit the program if backend file is not found.
import platform         #used to check system os
from tkinter.filedialog import askopenfilename #used to select a file

#importing the backend
try: from backend import *
except: #if the file is not present, program does not run
    print("Please store 'backend.py' in the same folder as this program and re-run.")
    sys.exit()

#checking if graphs can be displayed
try: import matplotlib.pyplot as plt; graph = True #constant used to indicate whether a graph should be plotted
except:
    graph = False #graph shouldnt be plotted
    print("Warning: Download the matplotlib library, if you want graphs to be displayed for the text analysis tools.")

#when this function is called, the previous contents of the interactive frame are cleared   
def clearInteractiveFrame():
    for widget in interactiveFrame.winfo_children(): #loops for each widget in the frame
        widget.destroy()

#function to change the interactive frame to be used for ciphers
def toCipher(cipher):
    #global variables used to access the widgets on the screen
    global textEntry,outputEntry, keyEntry, copyChoice, externalFile 

    topInfoLabel.config(text=textwrap.fill(cipherInfo[cipher][0], width=infoTextWidth),fg='black') #tool name is updated
    toolInfoLabel.config(text=textwrap.fill(cipherInfo[cipher][1], width=infoTextWidth),fg='black')
        
    clearInteractiveFrame() #previous contents of the frame cleared
    
    #the 3 main rows of the interface
    row1Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)
    row2Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)
    row3Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)

    row1Frame.pack(anchor='w')
    row2Frame.pack(anchor='w')
    row3Frame.pack(anchor='w')

    #Row 1
    #text box
    textEntryLabel = tkinter.Label(master = row1Frame, text = "Enter Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    textEntry = tkinter.Text(master = row1Frame, width = 70,height=8,bg="light yellow") #text entry
    textEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)

    textEntryLabel.grid(row=0,column=0,sticky='w')
    textEntry.grid(row=1,column=0)

    rightSideFrame = tkinter.Frame(master=row1Frame, bg=bgcolor)
    if cipher == 'plugin':
        #choose a python file button
        choosePyFileButton = tkinter.Button(master=rightSideFrame,padx=40,pady=8,highlightbackground='light yellow',
                            text = "Select Python File", command = updateExternalFile,height = 3,width = 8)
        choosePyFileButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
        choosePyFileButton.pack()
        
    #radio buttons for encrypt/decrypt
    choiceFrame = tkinter.Frame(master=rightSideFrame,bg=bgcolor,padx=15,pady=10)
    encryptOrDecrypt = tkinter.IntVar()
    encryptOrDecrypt.set(1)

    encryptChoice = tkinter.Radiobutton(master = choiceFrame,bg=bgcolor,text = "Encrypt",variable=encryptOrDecrypt,value=1,width = 15)
    decryptChoice = tkinter.Radiobutton(master = choiceFrame,bg=bgcolor, text = "Decrypt",variable=encryptOrDecrypt,value=0,width = 15)

    encryptChoice.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold')
    decryptChoice.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold')

    choiceFrame.pack()
    encryptChoice.pack()
    decryptChoice.pack()

    rightSideFrame.grid(row=1,column=1)
    
    #Row 2
    #key textbox

    if cipher == "atbash" or cipher == "morse":
        #atbash and morse do not use keys
        keyEntryLabel = tkinter.Label(master = row2Frame, text = "", #no text in the label
                              font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor)
        keyEntry = tkinter.Text(master = row2Frame, width = 50,height=4,bg=bgcolor) #box grayed out
        keyEntry.config(state='disabled',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)  #made read only
        
    else:
        keyEntryLabel = tkinter.Label(master = row2Frame, text = "Enter Key:", #normal key box
                            font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor)

        keyEntry = tkinter.Text(master = row2Frame, width = 50,height=4,bg="light yellow")
        keyEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor) 
       
    keyEntryLabel.grid(row=0,column=0,sticky='w')
    keyEntry.grid(row=1,column=0,sticky='w')


    #encrypt button
    encryptFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=17)
    encryptButton = tkinter.Button(master=encryptFrame,padx=40,pady=8,highlightbackground='light yellow',
                            text = "Process", command = lambda: encrypt(cipher,encryptOrDecrypt),
                                   height = 3,width = 8)
    encryptButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    encryptFrame.grid(row=1,column=1)
    encryptButton.pack()

    #encrypt file button
    encryptFileFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=10)
    encryptFileButton = tkinter.Button(master=encryptFileFrame,padx=40,pady=8,highlightbackground='light yellow',
                            text = "Process File", command = lambda: encrypt(cipher,encryptOrDecrypt,True), height = 3,width = 8)
    encryptFileButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    encryptFileFrame.grid(row=1,column=2)
    encryptFileButton.pack()

    #Row 3 - output row
    
    outputEntryFrame = tkinter.Frame(master=row3Frame, bg=bgcolor,pady=5)
    outputEntryLabel = tkinter.Label(master = outputEntryFrame, text = "Processed Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    outputEntry = tkinter.Text(master = outputEntryFrame, width = 70,height=8,bg="light yellow") #output entry
    outputEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
    
    outputEntryFrame.grid(row=0,column=0)
    outputEntryLabel.grid(row=0,column=0,sticky='w')
    outputEntry.grid(row=1,column=0)

    #automatically copy checkbox
    copyChoice = tkinter.IntVar() #checkbox variable

    copyCheckbox = tkinter.Checkbutton(master=row3Frame,variable=copyChoice, onvalue=1, offvalue=0,
                                  text= "Automatically Copy",bg = bgcolor,pady=5,padx=5)
    copyCheckbox.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold',highlightbackground=bgcolor)
    copyCheckbox.grid(row=0,column=1,sticky='e')

    
#function to change the interactive frame to be used for text manipulation tools
def toTextManipulation(toolName):
    global textEntry, keyEntry, outputEntry, upperOrLower,copyChoice
    
    clearInteractiveFrame()
    topInfoLabel.config(text=textwrap.fill(textManipInfo[toolName][0], width=infoTextWidth),fg='black') #tool name is updated
    toolInfoLabel.config(text=textwrap.fill(textManipInfo[toolName][1],width=infoTextWidth))

    row1Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)
    row2Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)

    row1Frame.pack(anchor='w')
    row2Frame.pack(anchor='w')
    
    #Row 1
    #text box
    #textEntryFrame = tkinter.Frame(master=row1Frame, bg=bgcolor,pady=5)
    textEntryLabel = tkinter.Label(master = row1Frame, text = "Enter Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    textEntry = tkinter.Text(master = row1Frame, width = 70,height=8,bg="light yellow") #text entry
    textEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
    
    textEntryLabel.grid(row=0,column=0,sticky='w')
    textEntry.grid(row=1,column=0)
    #textEntryFrame.grid(row=0,column=0,sticky='w')

    rightsideFrame = tkinter.Frame(master=row1Frame, bg=bgcolor,pady=5,padx=5)
    if toolName == 'addSpaces':
        #key entry box
        keyEntryFame = tkinter.Frame(master=rightsideFrame, bg=bgcolor,pady=5,padx=10)
        keyEntryLabel = tkinter.Label(master = keyEntryFame, text = "Enter Block Size (N):",
                              font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor)
        keyEntry = tkinter.Text(master = keyEntryFame, width = 20,height=2,bg="light yellow") #key entry
        keyEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
        
        keyEntryLabel.grid(row=0,column=0,sticky='w')
        keyEntry.grid(row=1,column=0)
        keyEntryFame.grid(row=0,column=0)

    elif toolName == 'convertCase':
        #radio buttons for upper/lower
        choiceFrame = tkinter.Frame(master=rightsideFrame,bg=bgcolor,padx=29)
        upperOrLower = tkinter.IntVar()
        upperOrLower.set(1)

        upperChoice = tkinter.Radiobutton(master = choiceFrame,bg=bgcolor,text = "Uppercase",variable=upperOrLower,value=1,width = 15)
        lowerChoice = tkinter.Radiobutton(master = choiceFrame,bg=bgcolor, text = "Lowercase",variable=upperOrLower,value=0,width = 15)

        upperChoice.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold')
        lowerChoice.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold')
        
        upperChoice.pack()
        lowerChoice.pack()

        choiceFrame.grid(row=0,column=0)

    #automatically copy checkbox
    copyChoice = tkinter.IntVar() #checkbox variable

    copyCheckbox = tkinter.Checkbutton(master=rightsideFrame,variable=copyChoice, onvalue=1, offvalue=0,
                                   text= "Automatically Copy",bg = bgcolor,pady=15,padx=5)
    copyCheckbox.config(fg='black',font='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold',highlightbackground=bgcolor)
    copyCheckbox.grid(row=1,column=0,sticky='s')

    rightsideFrame.grid(row=1,column=1)

        
    #row 2
    processFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=20)
    
    #process button
    processButton = tkinter.Button(master=processFrame,padx=40,pady=8,highlightbackground='light yellow',
                            text = "Process", command = lambda: callTextManip(toolName),
                                   height = 3,width = 8)
    processButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processButton.pack(pady=5)

    #processFile button
    processFileButton = tkinter.Button(master=processFrame,padx=40,pady=8,highlightbackground='light yellow',
                            text = "Process File", command = lambda: callTextManip(toolName,True),
                                   height = 3,width = 8)
    processFileButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processFileButton.pack(pady=5)                          
    
    processFrame.grid(row=0,column=0,sticky='w')

    #output box
    outputEntryFrame = tkinter.Frame(master=row2Frame, bg=bgcolor,pady=15)
    outputEntryLabel = tkinter.Label(master = outputEntryFrame, text = "Processed Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    outputEntry = tkinter.Text(master = outputEntryFrame, width = 69,height=8,bg="light yellow") #output entry
    outputEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
    
    outputEntryLabel.grid(row=0,column=0,sticky='w')
    outputEntry.grid(row=1,column=0)
    
    outputEntryFrame.grid(row=0,column=1)

    
#function to change the interactive frame to be used for frequncy analysis
def toFrequencyAnalysis():
    global textEntry, userFrame 
    
    clearInteractiveFrame()
    topInfoLabel.config(text=textwrap.fill(textAnalysisInfo['frequency'][0], width=infoTextWidth),fg='black') #tool name is updated
    toolInfoLabel.config(text=textwrap.fill(textAnalysisInfo['frequency'][1],width=infoTextWidth))

    row1Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)
    row2Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)

    row1Frame.pack(anchor='w')
    row2Frame.pack(anchor='w')

    #Row 1
    #text box
    textEntryFrame = tkinter.Frame(master=row1Frame, bg=bgcolor,pady=5)
    textEntryLabel = tkinter.Label(master = textEntryFrame, text = "Enter Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    textEntry = tkinter.Text(master = textEntryFrame, width = 70,height=8,bg="light yellow") #grid entry
    textEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
    
    textEntryLabel.grid(row=0,column=0,sticky='w')
    textEntry.grid(row=1,column=0)
    textEntryFrame.grid(row=0,column=0,sticky='w')

    #Buttons
    processFrame = tkinter.Frame(master=row1Frame,bg=bgcolor,padx=20)

    #used to have vertical space between categories
    spacerAnalysis = tkinter.Label(processFrame,font='TkDefaultFont 20',bg=bgcolor)
    spacerAnalysis.pack()


    #process button
    processButton = tkinter.Button(master=processFrame,padx=40,pady=5,highlightbackground='light yellow',
                            text = "Analyse Text", command = lambda: callTextAnalysis('frequency'),
                                   height = 3,width = 8)
    processButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processButton.pack(pady=5)

    #processFile button
    processFileButton = tkinter.Button(master=processFrame,padx=40,pady=5,highlightbackground='light yellow',
                            text = "Analyse File", command = lambda: callTextAnalysis('frequency',True),
                                   height = 3,width = 8)
    processFileButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processFileButton.pack(pady=5)                          
    
    processFrame.grid(row=0,column=1,sticky='w')


    #Row 2
    englishFreqFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=20)
    #contains the english letter frequencies

    englishFreqLabel = tkinter.Label(master = englishFreqFrame, text = "English Letter Frequencies (%)",
                              font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
    englishFreqLabel.grid(row=0,column=0,sticky='w')

    letterFreqFrame = tkinter.Frame(master=englishFreqFrame,bg=bgcolor,padx=20)

    for i in range(0,len(letters)): #for each letter
        #place its letter and corresponding frequency
        letterLabel = tkinter.Label(master = letterFreqFrame, text = letters[i],
                              font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
        freqLabel = tkinter.Label(master = letterFreqFrame, text = freq[i],
                              font = 'TkDefaultFont '+str(int(rightBaseFont)-2)+' bold', bg=bgcolor)
        letterLabel.grid(row=0,column=i)
        freqLabel.grid(row=1,column=i)

    letterFreqFrame.grid(row=1,column=0)

    englishFreqFrame.pack()

    #used to have vertical space
    spacer = tkinter.Label(row2Frame,font='TkDefaultFont 10',bg=bgcolor)
    spacer.pack()

    #user-text dependent output to be placed intthis frame
    userFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=20)
    userFrame.pack()

#function to change the interactive frame to be used for ngram counter
def toNgramCounter():
    global textEntry, keyEntry, userFrame
    
    clearInteractiveFrame()

    topInfoLabel.config(text=textwrap.fill(textAnalysisInfo['ngramCounter'][0], width=infoTextWidth),fg='black') #tool name is updated
    toolInfoLabel.config(text=textwrap.fill(textAnalysisInfo['ngramCounter'][1],width=infoTextWidth))

    row1Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)
    row2Frame = tkinter.Frame(master=interactiveFrame, bg=bgcolor,pady=2)

    row1Frame.pack(anchor='w')
    row2Frame.pack()

    #Row 1
    #text box
    textEntryFrame = tkinter.Frame(master=row1Frame, bg=bgcolor,pady=5)
    textEntryLabel = tkinter.Label(master = textEntryFrame, text = "Enter Text:",
                          font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor,anchor='w')
    textEntry = tkinter.Text(master = textEntryFrame, width = 56,height=8,bg="light yellow") #grid entry
    textEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
    
    textEntryLabel.grid(row=0,column=0,sticky='w')
    textEntry.grid(row=1,column=0)
    textEntryFrame.grid(row=0,column=0,sticky='w')

    #key entry box
    keyEntryFame = tkinter.Frame(master=row1Frame, bg=bgcolor,pady=5,padx=10)
    keyEntryLabel = tkinter.Label(master = keyEntryFame, text = "Block Size (N):",
                              font = 'TkDefaultFont '+str(int(rightBaseFont)+3)+' bold', bg=bgcolor)
    keyEntry = tkinter.Text(master = keyEntryFame, width = 12,height=2,bg="light yellow") #grid entry
    keyEntry.config(fg='black',font='TkDefaultFont '+rightBaseFont+' bold',highlightbackground=bgcolor)
        
    keyEntryLabel.grid(row=0,column=0,sticky='w')
    keyEntry.grid(row=1,column=0)
    keyEntryFame.grid(row=0,column=1)

    #Buttons
    processFrame = tkinter.Frame(master=row1Frame,bg=bgcolor,padx=10)

    #used to have vertical space between categories
    spacerAnalysis = tkinter.Label(processFrame,font='TkDefaultFont 20',bg=bgcolor)
    spacerAnalysis.pack()

    #process button
    processButton = tkinter.Button(master=processFrame,padx=40,pady=5,highlightbackground='light yellow',
                            text = "Analyse Text", command = lambda: callTextAnalysis('ngramCounter'),
                                   height = 3,width = 8)
    processButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processButton.pack(pady=5)

    #processFile button
    processFileButton = tkinter.Button(master=processFrame,padx=40,pady=5,highlightbackground='light yellow',
                            text = "Analyse File", command = lambda: callTextAnalysis('ngramCounter',True),
                                   height = 3,width = 8)
    processFileButton['font']='TkDefaultFont '+str(int(rightBaseFont)+2)+' bold'
    processFileButton.pack(pady=5)                          
    
    processFrame.grid(row=0,column=2,sticky='w')

    #user-text dependent output will be placed in this frame
    userFrame = tkinter.Frame(master=row2Frame,bg=bgcolor,padx=20)
    userFrame.pack()


#called when process button for a cipher is pressed
def encrypt(cipherName, encryptOrDecrypt,file=None):
    global externalFile
    
    mode = encryptOrDecrypt.get() #gets whether to encrypt or decrypt

    if file is None:
        text = textEntry.get("1.0",'end-1c') #gets the contents of the text box
    else:
        result = chooseFile() #tuple, 0 is file name , 1 is text

        if result is False: #if the user didnt select a file
            return
        else:
            file = result[0]
            text = result[1]
        
    text = text.replace('\n',' ')#replace new lines with spaces
    key = keyEntry.get("1.0",'end-1c') #gets the contents of the key box
    output = ''
         
    if cipherName == 'caesar' or cipherName == 'initial':
        if validateCaesar(key):
            output = caesar(mode,int(key),text)
            normalTopLabel(cipherName)
        else:
            topInfoLabel.config(text='Error: Please enter an integer in the key box.',fg='red')

    elif cipherName == 'affine':
        keyContents = key.split()

        if len(keyContents) != 2 or not validateAffine(keyContents[0],keyContents[1]):
            topInfoLabel.config(text="Error: Please enter key in the format 'a b' where a,b are integers.",fg='red')
        else:
            output = affine(mode,text,int(keyContents[0]),int(keyContents[1]))
            normalTopLabel(cipherName)

    elif cipherName == 'atbash':
        output = atbash(mode,text)

    elif cipherName == 'morse':
        output = morse(mode,text)
        if output == False:
            topInfoLabel.config(text="Error: Please enter valid morse code.",fg='red')
            output = ''
        else:
            normalTopLabel(cipherName)

    elif cipherName == 'keyword':
        output = keywordSub(mode,key,text)
        
    elif cipherName == 'alphaSub':
        if not validateAlphabetKey(key):
            topInfoLabel.config(text="Error: The key should be the same length as the alphabet (current length: "+str(len(key))+")",fg='red')
        else:
            output = alphabetSub(mode,key,text)
            normalTopLabel(cipherName)

    elif cipherName == 'columnar':
        if not validateTransposition(key,text):
            topInfoLabel.config(text="Error: Please enter a key and a text.",fg='red')
        else:
            output = columnarTransposition(mode,key,text)
            normalTopLabel(cipherName)

    elif cipherName == 'rowT':
        if not validateTransposition(key,text):
            topInfoLabel.config(text="Error: Please enter a key and a text.",fg='red')
        else:
            output = rowTransposition(mode,key,text)
            normalTopLabel(cipherName)

    elif cipherName == 'vigenere':
        if not validateVigenere(key):
            topInfoLabel.config(text="Error: Please enter a key that contains letters only.",fg='red')
        else:
            output = vigenere(mode,key,text)
            normalTopLabel(cipherName)

    elif cipherName == 'hill':
        parts = key.split()
        if len(parts) != 4: #must consist of 4 parts to be valid
            topInfoLabel.config(text="Error: Please enter key in the format 'a b c d' where a,b,c,d are integers.",fg='red')
        else:
            a = parts[0]
            b = parts[1]
            c = parts[2]
            d = parts[3]
            validation = validateHill(a,b,c,d,26) #the matrix is validated
            if validation is True:
                output = hill(mode,[[int(a),int(b)],[int(c),int(d)]],text)
                normalTopLabel(cipherName)
            else:
                topInfoLabel.config(text=validation,fg='red')

    elif cipherName == 'plugin':
        if externalFile is None:
            topInfoLabel.config(text='Error: Please select an external Python file.',fg='red')
        else:
            result = cipherPlugin(externalFile,mode,key,text)
            
            if result is False:
                if mode == 1: #text changes depending on encrypt/decrypt
                    topInfoLabel.config(text='Error: External file does not contain encrypt(key,text) function.',fg='red')
                else:
                    topInfoLabel.config(text='Error: External file does not contain decrypt(key,text) function.',fg='red')

            else:
                output = result
                normalTopLabel(cipherName)
            
    if file is None: #output to screen  
        outputEntry.delete('1.0','end') #clears the output box
        outputEntry.insert('1.0',output)
        if output != '' and copyChoice.get() == 1:
            copyToClipboard(output)
    elif output != '': #output to text file
        if mode == 0:
            prepend = "DECRYPTED"
        else:
            prepend = "ENCRYPTED"

        file = file.split('/')
        file[-1] = prepend + file[-1]
        file = '/'.join(file)

        writeToFile(file,output)

#changes the top label to contain the cipher name (instead of an error message)    
def normalTopLabel(cipherName):
    topInfoLabel.config(text=cipherInfo[cipherName][0],fg='black')

#called when process button for a text manipulation tool is pressed
def callTextManip(toolName, file=None):

    if file is None:
        text = textEntry.get("1.0",'end-1c') #gets the contents of the text box
    else:
        result = chooseFile() #tuple, 0 is file name , 1 is text

        if result is False: #if the user didnt select a file
            return
        else:
            file = result[0]
            text = result[1]

    text = text.replace('\n','')
    output = ''

    if toolName == 'addSpaces':
        key = keyEntry.get("1.0",'end-1c').strip() #gets the contents of the key box
        validation = validateAddSpaces(text,key)

        if validation is True:
            output = addSpaces(text,int(key))
            topInfoLabel.config(text="Split Text into Blocks",fg='black')
        else:
            topInfoLabel.config(text=validation,fg='red')

    elif toolName == 'convertCase':
        output = convertCase(text,upperOrLower.get())

    if file is None:
        outputEntry.delete('1.0','end') #clears the output box
        outputEntry.insert('1.0',output)
        if output != '' and copyChoice.get() == 1:
            copyToClipboard(output)
    elif output != '':
        file = file.split('/')
        file[-1] = "PROCESSED" + file[-1]
        file = '/'.join(file)
        writeToFile(file,output)

#called when process button for a text analysis tool is pressed
def callTextAnalysis (toolName, file = None):
    
    if file is None:
        text = textEntry.get("1.0",'end-1c') #gets the contents of the text box
    else:
        result = chooseFile() #tuple, 0 is file name , 1 is text

        if result is False: #if the user didnt select a file
            return
        else:
            file = result[0]
            text = result[1]

    #the user text frequencies frame is cleared
    for widget in userFrame.winfo_children(): 
        widget.destroy()

    text = text.replace('\n','').strip()

    if toolName == 'frequency':
        result = charFreq(text)
    
        if len(result) == 0: #checks if the text contains any letters
            return           #no output if it doesnt
        
        userFreqLabel = tkinter.Label(master = userFrame, text = "Input Text Letter Frequencies (%)",
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
        userFreqLabel.grid(row=0,column=0,sticky='w')
            
        userLetterFreqFrame = tkinter.Frame(master=userFrame,bg=bgcolor,padx=20)
        
        for i in range(0,len(result)): #for each letter in the text
            letterLabel = tkinter.Label(master = userLetterFreqFrame, text = result[i][2],
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
            
            freqLabel = tkinter.Label(master = userLetterFreqFrame, text = result[i][1],
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)-2)+' bold', bg=bgcolor)
            
            letterLabel.grid(row=0,column=i) #place the letter name in the grid
            freqLabel.grid(row=1,column=i)   #place its frequency in the grid
            
        userLetterFreqFrame.grid(row=1,column=0,sticky='w')        
        userFrame.pack(anchor='w')

        plotFrequencyGraph(result) #graph is plotted

    elif toolName == 'ngramCounter':
        key = keyEntry.get("1.0",'end-1c').strip() #gets the contents of the key box
        if not validateNgram(key):
            topInfoLabel.config(text="Error: Please enter a positive integer for the block size (N).",fg='red')
            
        elif len(text.replace(' ','')) != 0:    #if there is a text
            
            topInfoLabel.config(text=textAnalysisInfo['ngramCounter'][0],fg='black')
            ngramLabel = tkinter.Label(master = userFrame, text = "N-gram Occurences:",
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)+2)+' bold', bg=bgcolor,anchor='w')
            #ngramLabel.grid(row=0,column=0,sticky='w')
            ngramLabel.pack()
            
            ngramFrame = tkinter.Frame(master=userFrame,bg=bgcolor,padx=20)
            text = ''.join([x for x in text if x.isalpha()]) #keeps only letters in text
            result = ngramCounter(text,int(key))
            
            for i in range (0, min(27,len(result))): #loops for each ngram (or up to a maximum)
                ngramLineFrame = tkinter.Frame(master=ngramFrame,bg=bgcolor,padx=5)
                ngramItemName = tkinter.Label(master = ngramLineFrame, text = result[i][1],
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
                ngramCountLabel = tkinter.Label(master = ngramLineFrame, text = result[i][0],
                                      font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)
                ngramItemName.grid(row=0,column=0)  #place the ngram name in the grid
                ngramCountLabel.grid(row=0,column=1)#place the ngram's count in the grid

                ngramLineFrame.grid(row=i%9,column=i//9) #row and column id calculated
            
            
            ngramFrame.pack()

            if len(result) > 0: #plot only if there is data to plot
                plotNgramGraph(result)


#Graph Plotting
def plotEnglishFreq(xvalues):
    #adding all of these to a dictionary
    data = {}
    for i in range (26):
        data[letters[i]] = english[i]

    #the letters are ordered in order of the xvalues
    orderedFreq = []
    for i in xvalues:
        if i not in data:
            orderedFreq.append(0)
        else:
            orderedFreq.append(data[i])

    #these values are plotted onto the graph
    plt.plot(xvalues,orderedFreq,color = 'red')
    
def plotFrequencyGraph(textFreq):
    if not graph: #if user does not have the module installed
        return
    
    plt.close() #clear any previously existing graph

    xval = [x[2] for x in textFreq] #x and y values to be plotted
    yval = [x[1] for x in textFreq]

    plt.title('Frequency Analysis')
    plt.ylabel('Frequency as Percentage')
    plt.xlabel('Character') 
  
    plotEnglishFreq(xval) #the english frequencies are plotted
    plt.bar(xval,yval) #our data is plotted
    plt.legend(['English','Your text']) 

    plt.show(block=False)

def plotNgramGraph(ngramFreq):
    if not graph: #if user does not have the module installed
        return

    plt.close() #clear any previously existing graph

    xval = [x[1] for x in ngramFreq] #x and y values to be plotted
    yval = [x[0] for x in ngramFreq]

    fig,ax = plt.subplots(1) #creates figure and axis instances

    #title and labels set
    plt.title('N-gram Analysis')
    ax.set_xlabel('N-gram') 
    ax.set_ylabel('Number of Occurences')
    
    if len(xval[0]) <= 2: #if small ngrams are checked, xlabels are used
        xval = xval[:20] #number of x values is limited to fit on screen
        yval = yval[:20] #number of y values is limited to fit on screen
        plt.bar(xval,yval) #the data is plotted

    else: #for large ngrams
        xval = xval[:100] #number of x values is limited
        yval = yval[:100] #number of y values is limited

        plt.bar(xval,yval) #the normal data is plotted
        ax.set_xticks([]) #remove the xlabels (wouldnt fit screen)
        
    plt.show(block=False)

#File processing
def chooseFile(): #allows user to choose a file
    #only .txt allowed
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    #if user doesnt choose a file
    if not filepath:
        return False

    #if a valid file is chosen, the text is read
    with open(filepath, "r") as input_file:
        text = input_file.read()
        return (filepath, text)
      

def writeToFile(filepath, text): #text is written to the file
    with open(filepath, "w") as file: 
        file.write(text)
        
def copyToClipboard(text): #copies the given text to the clipboard
    window.clipboard_clear()        #clipboard is first cleared
    window.clipboard_append(text)

def updateExternalFile(): #updates the cipher plugin file
    global externalFile
    
    #only py files allowed
    filepath = askopenfilename(filetypes=[("Text Files", "*.py"), ("All Files", "*.*")])

    if filepath: #if user chooses a file
        externalFile = filepath #update external file
        normalTopLabel('plugin')
    
#Constants

#key is tool name, value is tuple which stores cipher title and cipher info
cipherInfo = { 
    'initial':("Welcome, Pick Any Tool!",""), #initial setting
    'caesar':("Caesar Cipher","The Caesar cipher is one of the earliest and most popular substitution ciphers, firstly used by Julius Caesar. The key for the cipher is an integer. Each letter in the text is replaced by the letter that is key letters after it. For example, if the key is 3, A becomes D, B becomes E etc."),
    'affine':("Affine Cipher","The Affine cipher is a substitution cipher which uses two integers a and b as the key, which can be entered in the form 'a b'. Each letter in the alphabet is replaced by another letter using the function (ax+b) mod 26, where x is the index of the letter (i.e. A=0, B=1, C=2...)."),
    'atbash':("Atbash Cipher","In the Atbash cipher, the substitution alphabet is formed by reversing the English alphabet, meaning that A is encrypted by Z, B is encrypted by Y etc. A key is not required for this cipher as the substitution is already defined. The Atbash cipher was originally used to encrypt the Hebrew alphabet."),
    'morse':("Morse Code","Morse Code is one of the most popular forms of monoalphabetic substitution. Each character is replaced by a unique set of dots and dashes.  Characters are separated by spaces and words are separated by the symbol /. Morse Code was used in telegraph communications to transmit text. To improve efficiency, the code length for the most common letters is the shortest."),
    'keyword':("Keyword Substitution","In Keyword Substitution, a keyword is used as the key, which determines the substitution alphabet. Repeating letters in the keyword are removed and the letters not in the keyword are appended to the substitution alphabet in alphabetical order. For example, the key 'FERMAT' would lead to 'FERMATBCDGHIJKLNOPQSUVWXYZ', and 'A' would be encrypted as 'F', 'B' as 'E' etc."),
    'alphaSub':("Alphabet Substitution","In Alphabet Substitution, the key is the substitution alphabet which is 26 characters long (length of the alphabet). For example, if the key is 'FERMATDIOPHNUSYGZBJCKLQVWX', 'A' would be encrypted by 'F', 'B' by 'E' etc. Also note that, for a one-to-one cipher, every letter in the key must be different."),
    'columnar':("Columnar Transposition","The Columnar Transposition cipher uses a keyword as a key to produce a permutation of the input text. The encryption process involves writing out the plaintext into a table which has n columns, where n is the number of letters in the key. The ciphertext is generated by reading off the columns in alphabetical order according to the key."),
    'rowT':("Row Transposition","The Row Transposition cipher is similar to Columnar Transposition. In this cipher, the table is generated in the same way as a Columnar Transposition cipher. The table is filled out by writing in columns and the ciphertext is generated by reading off each row in alphabetical order according to the key."),
    'vigenere':("Vigenere Cipher","The Vigenere cipher uses multiple alphabets which are generated by a keyword to encrypt a text. The key is written out repeatedly under the plaintext, and the encryption is performed by shifting each  letter in the text by the corresponding key index. This is similar to the Caesar shifts, except multiple shifts are used instead of one which makes it a lot harder to crack."),
    'hill':("Hill Cipher","The Hill cipher is a polygraphic cipher based on linear algebra, where the key is a 2x2 matrix which should be entered in the form 'a b c d'. The text is encrypted by converting every pair of letters into a 2x1 vector which is multiplyied by the key matrix. The resulting vector, which contains numbers that represent letter indices, is converted back to letters which is appended to the ciphertext. Note that the square matrix must be invertible modulo 26, i.e. the determinant of the square matrix is coprime with 26 to produce a one-to-one function."),
    'plugin':("Cipher Plug-in",'The Cipher Plug-in tool allows you to use the graphical interface for other ciphers. Click the "Select Python File" button to import an external file. In order to use this tool correctly, ensure that the file contains functions called encrypt and decrypt which take in key and text as parameters.')
    }


textManipInfo = {
    'addSpaces':('Split Text into Blocks','When running this tool, all of the spaces in the input text are removed and spaces are added at every n characters, leading to a text that consists of blocks of size n. You can also remove spaces from the text by entering 0 into the block size.'),
    'convertCase':('Convert Letter Case','This tool converts all of the letters in the input text into uppercase or lowercase. This process can be used on ciphertext to disguise capital letters that may have been present in the input text. Having the same letter case for all of the letters can also make it easier to analyse the text.',)
    }

textAnalysisInfo = {
    'frequency':('Frequency Analysis','The frequency analysis tool displays the frequency of each letter that occurs in the text, along with the frequency of letters in English. It is a useful tool in identifying substitutions and deciphering ciphertexts. The tool also produces a graph of the letter percentages in the text.'),
    'ngramCounter':('N-gram Counter','The N-gram Counter tool displays the most common n-grams (blocks of size n) that occur in the text. For example, the most common 3-gram in English is "the". A graph that shows the occurrences of the n-grams is also produced.')
    }
    
letters = list('ETAONIHSRLDUCMWYFGPBVKJXQZ') #contains the letter frequencies of the letters in english
freq = '12.6 9.4 8.3 7.7 6.8 6.7 6.1 6.1 5.7 4.2 4.1 2.9 2.7 2.5 2.3 2.0 2.0 1.9 1.7 1.5 1.1 0.9 0.2 0.2 0.1 0.1'.split()
english = [float(x) for x in freq] #used for freq analysis
    
#bgcolor,categorycolor: (gray94,dodgerblue2),
bgcolor = 'gray94'
categoryColor = 'dodgerblue2'
infoTextWidth = 112  #the width of the information at the bottom

os = platform.system() #gets os of user's system

if os == 'Windows':
    #fonts used in labels for WINDOWS
    baseFont = '13'
    rightBaseFont = '12'
    categoryFont = '15' #ideally 15
    titleFont = '18'
    categoryWidth = 23
else:
    #fonts used in labels for MAC (and linux)
    baseFont = '16'
    rightBaseFont = '15'
    categoryFont = '18'
    titleFont = '22'
    categoryWidth = 21

#Global variable
externalFile = None #stores the file path of the external file for cipher plugin

window = tkinter.Tk() #window is created
window.geometry("1300x700")
window.title("Cryptography Tools")
window.configure(bg=bgcolor) #sets background color to the chosen color
window.resizable(False, False) #window cant be resized

#grid
#window.rowconfigure(0,weight=1)
window.columnconfigure(0,minsize = 250,weight=1)#this adds space between the left hand side and the right hand side of the GUI
window.columnconfigure(1,minsize = 950,weight=1)

#first frame is left side second frame is right side of the gui
firstFrame = tkinter.Frame(master=window,bg=bgcolor,pady=15)
secondFrame = tkinter.Frame(master = window, bg=bgcolor,pady=15)

#the two main frames are packed
firstFrame.grid(row = 0, column = 0, sticky = "ns")
secondFrame.grid(row = 0, column = 1, sticky = "nsew")


#Left hand side of GUI:
cryptographyToolsLabel = tkinter.Label(master = firstFrame, text = "Cryptography Tools",width=20,
                          font = 'TkDefaultFont '+titleFont+' bold', bg=bgcolor,pady=12)
cryptographyToolsLabel.pack()


#Text Manipulation
textManipLabel = tkinter.Label(master = firstFrame, text = "Text Manipulation Tools:",
                             font = 'TkDefaultFont '+categoryFont+' bold', fg = categoryColor, bg=bgcolor,pady=2,anchor = 'w',width = categoryWidth)
textManipLabel.pack()


addSpacesLabel = tkinter.Label(master = firstFrame, text = "Split Text into Blocks",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
addSpacesLabel.pack()
addSpacesLabel.bind("<Button-1>", lambda e: toTextManipulation('addSpaces')) #makes the label clickable


convertCaseLabel = tkinter.Label(master = firstFrame, text = "Convert Letter Case",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
convertCaseLabel.pack()
convertCaseLabel.bind("<Button-1>", lambda e: toTextManipulation('convertCase')) #makes the label clickable


#used to have vertical space between categories
spacer1 = tkinter.Label(firstFrame,font='TkDefaultFont 1',bg=bgcolor)
spacer1.pack()

#Text Analysis
textAnalysisLabel = tkinter.Label(master = firstFrame, text = "Text Analysis Tools:",
                             font = 'TkDefaultFont '+categoryFont+' bold', fg = categoryColor, bg=bgcolor, pady=2 ,anchor = 'w',width = categoryWidth)
textAnalysisLabel.pack()


freqLabel = tkinter.Label(master = firstFrame, text = "Frequency Analysis",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
freqLabel.pack()
freqLabel.bind("<Button-1>", lambda e: toFrequencyAnalysis()) #makes the label clickable


ngramLabel = tkinter.Label(master = firstFrame, text = "N-gram Counter",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
ngramLabel.pack()
ngramLabel.bind("<Button-1>", lambda e: toNgramCounter()) #makes the label clickable


#used to have vertical space between categories
spacer2 = tkinter.Label(firstFrame,font='TkDefaultFont 1',bg=bgcolor)
spacer2.pack()

#Monoalphabetic Substitution Ciphers

monoSubLabel = tkinter.Label(master = firstFrame, text = "Monoalphabetic Substitution:",anchor='w',width=categoryWidth,
                             font = 'TkDefaultFont '+categoryFont+' bold', fg = categoryColor, bg=bgcolor,pady=2)
monoSubLabel.pack()

caesarLabel = tkinter.Label(master = firstFrame, text = "Caesar Cipher",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
caesarLabel.pack()
caesarLabel.bind("<Button-1>", lambda e: toCipher('caesar')) #makes the label clickable


affineLabel = tkinter.Label(master = firstFrame, text = "Affine Cipher",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
affineLabel.pack()
affineLabel.bind("<Button-1>", lambda e: toCipher('affine'))


atbashLabel = tkinter.Label(master = firstFrame, text = "Atbash Cipher",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
atbashLabel.pack()
atbashLabel.bind("<Button-1>", lambda e: toCipher('atbash')) #makes the label clickable


morseLabel = tkinter.Label(master = firstFrame, text = "Morse Code",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
morseLabel.pack()
morseLabel.bind("<Button-1>", lambda e: toCipher('morse')) #makes the label clickable


keywordLabel = tkinter.Label(master = firstFrame, text = "Keyword Substitution",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
keywordLabel.pack()
keywordLabel.bind("<Button-1>", lambda e: toCipher('keyword')) #makes the label clickable


alphaSubLabel = tkinter.Label(master = firstFrame, text = "Alphabet Substitution",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
alphaSubLabel.pack()
alphaSubLabel.bind("<Button-1>", lambda e: toCipher('alphaSub')) #makes the label clickable


#used to have vertical space between categories
spacer3 = tkinter.Label(firstFrame,font='TkDefaultFont 1',bg=bgcolor)
spacer3.pack()

#Transposition Ciphers
transpoLabel = tkinter.Label(master = firstFrame, text = "Transposition Ciphers:",
                             font = 'TkDefaultFont '+categoryFont+' bold', fg = categoryColor, bg=bgcolor,pady=2,anchor = 'w',width = categoryWidth)
transpoLabel.pack()


columnarLabel = tkinter.Label(master = firstFrame, text = "Columnar Transposition",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
columnarLabel.pack()
columnarLabel.bind("<Button-1>", lambda e: toCipher('columnar')) #makes the label clickable


rowTLabel = tkinter.Label(master = firstFrame, text = "Row Transposition",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
rowTLabel.pack()
rowTLabel.bind("<Button-1>", lambda e: toCipher('rowT')) #makes the label clickable


#used to have vertical space between categories
spacer4 = tkinter.Label(firstFrame,font='TkDefaultFont 1',bg=bgcolor)
spacer4.pack()

#Polygraphic Ciphers
polygraphicLabel = tkinter.Label(master = firstFrame, text = "Polygraphic Ciphers:",
                             font = 'TkDefaultFont '+categoryFont+' bold', fg = categoryColor, bg=bgcolor,pady=2,anchor = 'w',width = categoryWidth)
polygraphicLabel.pack()


vigenereLabel = tkinter.Label(master = firstFrame, text = "Vigenere Cipher",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
vigenereLabel.pack()
vigenereLabel.bind("<Button-1>", lambda e: toCipher('vigenere'))


hillLabel = tkinter.Label(master = firstFrame, text = "Hill Cipher",
                          font = 'TkDefaultFont '+baseFont+' bold', bg=bgcolor, cursor="hand2")
hillLabel.pack()
hillLabel.bind("<Button-1>", lambda e: toCipher('hill')) #makes the label clickable


#Cipher Plug-in

cipherPluginLabel = tkinter.Label(master = firstFrame, text = "Cipher Plug-in",
                          font = 'TkDefaultFont '+categoryFont+' bold',fg=categoryColor, bg=bgcolor,width=categoryWidth, anchor='w',pady=3, cursor="hand2")
cipherPluginLabel.pack()
cipherPluginLabel.bind("<Button-1>", lambda e: toCipher('plugin')) #makes the label clickable


#RIGHT HAND SIDE OF GUI

#title at the top
topInfoLabel = tkinter.Label(master = secondFrame, text = "Welcome, pick any tool on the left to begin!",
                          font = 'TkDefaultFont '+titleFont+' bold', bg=bgcolor)
topInfoLabel.pack()


#interactive part of the right hands side (buttons, text boxes etc.)
interactiveFrame = tkinter.Frame(master=secondFrame,bg=bgcolor,pady=10)
interactiveFrame.pack()


#bottom of the right hand side (static information)
#toolInfoText = "This is where information about the tool will appear.This is where information about the tool will appear.This is where information about the tool will appear.This is where information about the tool will appear.This is where information about the tool will appear.This is where information about the tool will appear.This is where information about the tool will appear."
toolInfoText = ''
toolInfoText = textwrap.fill(toolInfoText, width=infoTextWidth)

toolInfoLabel = tkinter.Label(master=secondFrame, text = toolInfoText,
           font = 'TkDefaultFont '+str(int(rightBaseFont)+1)+' bold', bg=bgcolor)

toolInfoLabel.pack()

#toCipher('initial') #uncomment if you want the starting screen to have a cipher interface

window.mainloop()
