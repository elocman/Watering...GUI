#######################################################################################################################
# Cole Varnado
# CSC 132-002
# Updated 10.29.19
# GUI for taking care of plants
#######################################################################################################################
from Tkinter import *
from random import randint

class Plant(object):
    def __init__(self, plntName, lghtAmnt, watrAmnt):
        self.plntName = plntName
        self.lghtAmnt = lghtAmnt
        self.watrAmnt = watrAmnt

    @property
    def plntName(self):
        return self._plntName
    @plntName.setter
    def plntName(self, value):
        self._plntName = value

    @property
    def lghtAmnt(self):
        return self._lghtAmnt
    @lghtAmnt.setter
    def lghtAmnt(self, value):
        self._lghtAmnt = value

    @property
    def watrAmnt(self):
        return self._watrAmnt
    @watrAmnt.setter
    def watrAmnt(self, value):
        self._watrAmnt = value

    def __str__(self):
        s = "{}: Light={}, Water={}".format(self.plntName, self.lghtAmnt, self.watrAmnt)
        return s

class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    # sets up the GUI
    def setupGUI(self):
        # function to add plant
        def addPlant():
            # variable to check for wrong values
            altr = 0
            # make plant list 6 long
            if (len(plntList) <= nmbrPlnt):
                # check if any input
                if (self.input.get() == ""):
                    stat = ""
                else:
                    # split input by comma
                    stat = self.input.get().split(',')
                # check if Plant class has all inputs needed
                if (len(stat) == 3):
                    # test if user input was a number
                    try:
                        # if user inputs aren't integers it will throw an error
                        stat[1] = int(stat[1])
                        stat[2] = int(stat[2])
                    except:
                        altr = 1
                        # clear input
                        self.input.delete(0, END)
                        print "Please enter numbers for light amount and water amount."
                    # check if plant is already in list
                    for i in range(len(plntNameList)):
                        # if new plant name = plant name in list
                        if (stat[0] == plntNameList[i]):
                            altr = 1
                            # clear input
                            self.input.delete(0, END)
                            print "Please enter a plant that isn't already in the list."
                    if (altr == 0):
                        # create new plant
                        newPlnt = Plant(stat[0], stat[1], stat[2])
                        plntList.append(newPlnt)
                        plntNameList.append(newPlnt.plntName)
                        # new menu for new list
                        self.drop = OptionMenu(self, clicked, *plntNameList)
                        self.drop.grid(row=1, column=0, columnspan=4, sticky=N+S+E+W)
                        # clear input
                        self.input.delete(0, END)
                else:
                    # clear input
                    self.input.delete(0, END)
                    print "Please use format: Plant,LightAmount,WaterAmount"
            else:
                # clear input
                self.input.delete(0, END)
                print "The plant list is full."

        # function to delete plant
        def deletePlant():
            # variable for checking plant
            altr = 0
            # check every plant for one selected
            for i in range(len(plntList)):
                # check which plant to remove
                if (clicked.get() == plntList[i].plntName and i != 0):
                    # j is the index that will be removed
                    j = i
                    altr = 1
            # remove plant
            if (altr == 1):
                # remove from name list and plant list
                plntNameList.remove(plntList[j].plntName)
                plntList.remove(plntList[j])
                # new menu for new list
                clicked.set(plntNameList[0])
                self.drop = OptionMenu(self, clicked, *plntNameList)
                self.drop.grid(row=1, column=0, columnspan=4, sticky=N+S+E+W)
                self.label1 = Label(self, text=plntList[0])
                self.label1.grid(row=3, column=0, columnspan=4, sticky=N+S+E+W)

        # function to apply plant selected
        def apply():
            # find plant selected
            for i in range(len(plntList)):
                if (clicked.get() == plntList[i].plntName):
                    mesg = plntList[i]
            # print plant's items
            self.label1 = Label(self, text=mesg)
            self.label1.grid(row=3, column=0, columnspan=4, sticky=N+S+E+W)

        # default plant in list for name and values
        plntList = [p1]
        plntNameList = [p1.plntName]

        # set drop down
        clicked = StringVar()
        # set default selection
        clicked.set(plntNameList[0])

        # add plant button
        self.button1 = Button(self, text="Add Plant", command=addPlant)
        self.button1.grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)

        # delete plant button
        self.button2 = Button(self, text="Delete Plant", command=deletePlant)
        self.button2.grid(row=0, column=2, columnspan=2, sticky=N+S+E+W)

        # plant drop-down menu
        self.drop = OptionMenu(self, clicked, *plntNameList)
        self.drop.grid(row=1, column=0, columnspan=4, sticky=N+S+E+W)

        # apply button
        self.button3 = Button(self, text="Apply Selection", command=apply)
        self.button3.grid(row=2, column=0, columnspan=4, sticky=N+S+E+W)

        # plant info.
        self.label1 = Label(self, text=plntList[0])
        self.label1.grid(row=3, column=0, columnspan=4, sticky=N+S+E+W)

        # text input
        self.input = Entry(self, bg="white")
        self.input.grid(row=4, column=0, columnspan=4, sticky=N+S+E+W)

        # function which reads input values and displays them
        def update():
            # status
            self.label2 = Label(self, text="Moisture = "+str(randint(0,100))+\
                "\nNutrients = "+str(randint(0,100))+"\nLight = "+str(randint(0,100)))
            self.label2.grid(row=0, column=4, columnspan=4, rowspan=5, sticky=N+S+E+W)
            self.after(1000, update)
        update()

        # resize gui
        for row in range(4):
            Grid.rowconfigure(self, row, weight=1)
        for col in range(8):
            Grid.columnconfigure(self, col, weight=1)

        # pack the GUI
        self.pack(fill=BOTH, expand=1)

#######################################################################################################################
p1 = Plant("Cactus", 8, 10)
nmbrPlnt = 5

root = Tk()
root.title("Watering...")
root.geometry("600x300")
p = MainGUI(root)

root.mainloop()
