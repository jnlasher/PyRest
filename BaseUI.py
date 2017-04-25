import tkinter as tk
from tkinter import ttk
import requests


class Application():
    def __init__(self, master):
        # SETUP
        self.master = master
        master.title('PyRest')
        master.minsize(width=550, height=250)

        # GENERATE LAYOUT
        top = tk.Frame(master)
        bottom = tk.Frame(master)
        top.pack(side=tk.TOP)
        bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # LAYOUT DIVISIONS
        divs = ttk.Notebook(master)
        headerPage = ttk.Frame(divs, width = 300, height=100)
        bodyPage = ttk.Frame(divs, width = 300, height=100)
        divs.add(headerPage, text='Headers')
        divs.add(bodyPage, text='Body')
        divs.grid(column=0)
        divs.pack()

        # CREATE WIDGETS
        self.requestType = tk.StringVar()
        self.requestType.set('GET')
        self.requestType.trace("w", self.UpdateRequestType)
        self.requestOption = tk.OptionMenu(master, self.requestType, 'GET', 'POST', 'PUT', 'DELETE')
        self.requestOption.pack(in_=top, side=tk.LEFT)

        self.addressLabel = tk.Entry(master)
        self.addressLabel.pack(in_=top, side=tk.LEFT)

        self.headersLabel = tk.Entry()
        self.bodyLabel = tk.Entry()
        self.bodyLabel.pack()
        self.headersLabel.pack()

        self.close = tk.Button(master, text='Submit', command=self.Close)
        self.close.pack(in_=bottom)


#        self.responseBox = tk.Text(master, width=25, height=10)
#        scrollbar = tk.Scrollbar(master)
#        scrollbar.config(command=self.responseBox.yview)
#        self.responseBox.config(yscrollcommand=scrollbar.set)
#        scrollbar.pack(in_=bottom, side=tk.RIGHT, fill=tk.Y)
#        self.responseBox.pack(in_=bottom, side=tk.LEFT, fill=tk.BOTH, expand=True)


    def UpdateRequestType(self, *args):
        print('Request type is: {}'.format(self.requestType.get()))

    def GetURI(self):
        print('url is: {}'.format(self.addressLabel.get()))

    def Close(self):
        self.master.quit()


root = tk.Tk()
app = Application(root)
root.mainloop()
