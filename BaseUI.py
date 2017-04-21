import tkinter as tk
import requests


class Application():
    def __init__(self, master):
        self.master = master
        master.title('PyRest')

        self.requestType = tk.StringVar()
        self.requestType.set('GET')
        self.requestOption = tk.OptionMenu(master, self.requestType, 'GET', 'POST', 'PUT', 'DELETE')
        self.requestOption.pack()

        self.close = tk.Button(master, text='Close', command=self.Close)
        self.close.pack()

    def UpdateRequestType(self):
        print('Request type is: {}'.format(self.requestType.get()))

    def Close(self):
        self.master.quit()
        print('Request type is: {}'.format(self.requestType.get()))

root = tk.Tk()
app = Application(root)
root.mainloop()
