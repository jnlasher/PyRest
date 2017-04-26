import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master):
        #SETUP
        self.master = master
        master.title('PyREST')
        master.minsize(width=550, height=250)
        self.c_row = 1
        val = tk.IntVar()

        # GENERATE FRAMES
        topFrame = tk.Frame(master, bg='cyan', width = 450, height=50, padx=30, pady=3)
        centerFrame = tk.Frame(master, bg='gray2', width=50, height=40, padx=30, pady=3)
        responseFrame = tk.Frame(master, bg='white', width = 450, height = 45, padx=30, pady=3)
        topFrame.grid_propagate(False)
        topFrame.grid(row=0, sticky='ew')
        centerFrame.grid(row=1, sticky='ew')
        responseFrame.grid(row=3, sticky='ew')
        divs = ttk.Notebook(centerFrame)
        self.headerPage = ttk.Frame(divs)
        self.bodyPage = ttk.Frame(divs)
        divs.add(self.headerPage, text='Headers')
        divs.add(self.bodyPage, text='Body')

        # CREATE WIDGETS
        self.requestType = tk.StringVar()
        self.requestType.set('GET')
        self.requestType.trace('w', self.UpdateRequestType)
        self.requestOption = tk.OptionMenu(topFrame, self.requestType, 'GET','POST','PUT','DELETE')
        self.addressLabel = tk.Entry(topFrame, width=50)
        # First Division
        self.headersKey = tk.Entry(self.headerPage)
        self.headersVal = tk.Entry(self.headerPage, width=39)
        self.addHButton = tk.Button(self.headerPage, text = 'Add Header', command = self.AddHeader)
        # Split
        self.formData = tk.Radiobutton(self.bodyPage, text='form-data', variable=val, value=1)
        self.urlEncoded = tk.Radiobutton(self.bodyPage, text='x-www-form-urlencoded', variable=val, value=2)
        self.rawData = tk.Radiobutton(self.bodyPage, text='raw', variable=val, value=3)
        self.binaryFile = tk.Radiobutton(self.bodyPage, text='binary', variable=val, value=4)

        # CREATE LAYOUT
        self.requestOption.grid(row=0, column=0, padx=3)
        self.addressLabel.grid(row=0, column=1, padx=3)
        divs.grid()
        self.headersKey.grid(row=0, column=0, padx=3)
        self.headersVal.grid(row=0, column=1, padx=3)
        self.addHButton.grid(row=1, column=0)
        # Split
        self.formData.grid(row=0, column=0)
        self.urlEncoded.grid(row=0, column=1)
        self.rawData.grid(row=0, column=2)
        self.binaryFile.grid(row=0, column=3)


    def AddHeader(self):
        newKey = tk.Entry(self.headerPage)
        newVal = tk.Entry(self.headerPage, width=39)
        newKey.grid(row=self.c_row, column = 0)
        newVal.grid(row=self.c_row, column = 1)
        self.addHButton.grid(row=self.c_row+1, column=0)
        self.c_row += 1

    def UpdateRequestType(self, *args):
        print('Request type is: {}'.format(self.requestType.get()))


root = tk.Tk()
app = Application(root)
root.mainloop()
