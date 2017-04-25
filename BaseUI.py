import tkinter as tk
from tkinter import ttk
import requests


class Application:
    def __init__(self, master):
        # SETUP
        self.master = master
        master.title('PyRest')
        master.minsize(width=550, height=250)
        val = tk.IntVar()

        # GENERATE LAYOUT
        top = tk.Frame(master)
        bottom = tk.Frame(master)
        top.pack(side=tk.TOP)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # LAYOUT DIVISIONS
        divs = ttk.Notebook(master)
        self.headerPage = ttk.Frame(divs, width = 300, height=100)
        self.bodyPage = ttk.Frame(divs, width = 300, height=100)
        divs.add(self.headerPage, text='Headers')
        divs.add(self.bodyPage, text='Body')
        divs.grid(column=0)
        divs.pack(fill=tk.X, padx=30)

        # CREATE WIDGETS
        self.requestType = tk.StringVar()
        self.requestType.set('GET')
        self.requestType.trace("w", self.UpdateRequestType)
        self.requestOption = tk.OptionMenu(master, self.requestType, 'GET', 'POST', 'PUT', 'DELETE')
        self.requestOption.pack(in_=top, side=tk.LEFT)

        self.addressLabel = tk.Entry(master)
        self.addressLabel.pack(in_=top, side=tk.LEFT)
        # Build the headers subsection
        self.headersLabel = tk.Entry(self.headerPage)
        self.headersLabel.pack(fill=tk.X, padx=30, pady=6)
        self.addHButton = tk.Button(self.headerPage, text = 'Add Header', command= self.AddHeader)
        self.addHButton.pack(side=tk.BOTTOM)
        # Build the body/message subsection
        self.formData = tk.Radiobutton(self.bodyPage, text='form-data', variable=val, value=1).pack(side=tk.LEFT)
        self.urlEncoded = tk.Radiobutton(self.bodyPage, text='x-www-form-urlencoded', variable=val, value=2).pack(side=tk.LEFT)
        self.rawData = tk.Radiobutton(self.bodyPage, text='raw', variable=val, value=3).pack(side=tk.LEFT)
        self.binaryFile = tk.Radiobutton(self.bodyPage, text='binary', variable=val, value=4).pack(side=tk.LEFT)

        self.close = tk.Button(master, text='Submit', command=self.Close)
        self.close.pack(in_=bottom)


#        self.responseBox = tk.Text(master, width=25, height=10)
#        scrollbar = tk.Scrollbar(master)
#        scrollbar.config(command=self.responseBox.yview)
#        self.responseBox.config(yscrollcommand=scrollbar.set)
#        scrollbar.pack(in_=bottom, side=tk.RIGHT, fill=tk.Y)
#        self.responseBox.pack(in_=bottom, side=tk.LEFT, fill=tk.BOTH, expand=True)

    def AddHeader(self):
        newEntry = tk.Entry(self.headerPage)
        newEntry.pack(side=tk.TOP, fill=tk.X, padx=30)
        self.addHButton.pack()

    def AddBody(self):
        newEntry = tk.Entry(self.bodyPage)
        newEntry.pack(side=tk.BOTTOM, fill=tk.X, padx=30)
        self.addBButton.pack(side=tk.BOTTOM)

    def UpdateRequestType(self, *args):
        print('Request type is: {}'.format(self.requestType.get()))

    def GetURI(self):
        print('url is: {}'.format(self.addressLabel.get()))

    def Close(self):
        self.master.quit()


root = tk.Tk()
app = Application(root)
root.mainloop()
