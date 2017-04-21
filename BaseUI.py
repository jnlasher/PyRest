import tkinter as tk
import requests


class Application():
    def __init__(self, master):
        self.master = master
        master.title('PyRest')
        master.minsize(width=300, height=100)

        self.requestType = tk.StringVar()
        self.requestType.set('GET')
        self.requestType.trace("w", self.UpdateRequestType)
        self.requestOption = tk.OptionMenu(master, self.requestType, 'GET', 'POST', 'PUT', 'DELETE')
        self.requestOption.pack()

        self.addressLabel = tk.Entry(master)
        self.addressLabel.pack()

        self.close = tk.Button(master, text='Close', command=self.Close)
        self.close.pack()

    def UpdateRequestType(self, *args):
        print('Request type is: {}'.format(self.requestType.get()))

    def GetURI(self):
        print('url is: {}'.format(self.addressLabel.get()))

    def Close(self):
        self.master.quit()


root = tk.Tk()
app = Application(root)
root.mainloop()
