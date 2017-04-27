import tkinter as tk
from tkinter import ttk


class Application:
    def __init__(self, master):
        #SETUP
        self.master = master
        master.title('PyREST')
        master.minsize(width=550, height=250)
        self.c_row = 1
        self.val = tk.IntVar()

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
        self.menuPage = tk.Frame(self.bodyPage, bg='cyan', width=5, height=5)
        divs.add(self.headerPage, text='Headers')
        divs.add(self.bodyPage, text='Body')
        self.updateFrame = tk.Frame(self.bodyPage, width=10, height=10, bg='cyan')


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
        self.formData = tk.Radiobutton(self.bodyPage, text='form-data', variable=self.val, value=1, command=self.UpdateBody)
        self.urlEncoded = tk.Radiobutton(self.bodyPage, text='x-www-form-urlencoded', variable=self.val, value=2, command=self.UpdateBody)
        self.rawData = tk.Radiobutton(self.bodyPage, text='raw', variable=self.val, value=3, command=self.UpdateBody)
        self.binaryFile = tk.Radiobutton(self.bodyPage, text='binary', variable=self.val, value=4, command=self.UpdateBody)

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
        self.updateFrame.grid(row=1)


    def AddHeader(self):
        newKey = tk.Entry(self.headerPage)
        newVal = tk.Entry(self.headerPage, width=39)
        newKey.grid(row=self.c_row, column = 0)
        newVal.grid(row=self.c_row, column = 1)
        self.addHButton.grid(row=self.c_row+1, column=0)
        self.c_row += 1

    def UpdateBody(self):
        print(self.val.get())
        self._blankWidgets()

    def UpdateRequestType(self, *args):
        print('Request type is: {}'.format(self.requestType.get()))

    def _blankWidgets(self):
        print('clearing...')
        for item in self.updateFrame.grid_slaves():
            item.grid_forget()


root = tk.Tk()
app = Application(root)
root.mainloop()
