#Kelsey Yim
from tkinter import *
win = Tk()

#Frame to hold user entry widget and label
entryFrame = Frame(win)
entryFrame.grid_columnconfigure(0, weight=1)
entryFrame.grid_columnconfigure(1, weight=1)
entryFrame.grid_rowconfigure(0, weight=1)
entryFrame.grid_rowconfigure(1, weight=1)

#attrList to store user entries, finalList to get each entry from attrList
attrList = []
finalList = []

#counter to track how many entries the user makes
counter=0

class userInput(Frame):
    #default constructor
    def __init__(self, parent):
        super().__init__(parent)
        
    def addEntry(self):
        global counter
        attLabel = Label(entryFrame, text = "Attribute Name: ")
        attLabel.grid(column=0, row=counter)
        txtbox = Entry(entryFrame)
        txtbox.grid(column=1, row=counter)
        attrList.append(txtbox) #save each entry into attrList to not lose user input
        counter +=1 
        
    def printList(self):
        for i in range(counter):
            finalList.append(attrList[i].get()) #retrieve data from attrList
        print(finalList)
        for k in finalList:
            print(k)
        
entryFrame.pack(side=TOP, expand=YES, fill=BOTH, padx=5, pady=5)

lbl = userInput(win)
lbl.addEntry()

#Frame to hold save and add buttons
buttonFrame = Frame(win)

#Button Config
addbtn = Button(buttonFrame, text = "Add Attribute: ", command = lbl.addEntry)
savebtn = Button(buttonFrame, text = "Save", command=lbl.printList)
savebtn.pack(side = RIGHT, pady=5, padx=5)
addbtn.pack(side = RIGHT, pady=5)
buttonFrame.pack(side=BOTTOM, expand=YES, fill=BOTH)

#Window Config
win.title("Attributes")
win.mainloop()
