#!/usr/bin/env/Python

import tkinter as tk
from tkinter import ttk
import requests


class Application:
    def __init__(self, master):
        #SETUP
        self.master = master
        master.title('PyREST')
        master.minsize(width=723, height=570)
        self.c_row = 1
        self.r_num = 1
        self.val = tk.IntVar()
        self.formatSel = tk.StringVar()

        # GENERATE FRAMES
        topFrame = tk.Frame(master, bg='cyan', width = 723, height=50, padx=30, pady=3)
        centerFrame = tk.Frame(master, bg='gray2', width=723, height=40, padx=30, pady=3)
        self.responseFrame = tk.Frame(master, bg='white', width = 723, height = 45, padx=30, pady=3)
        topFrame.grid_propagate(False)
        topFrame.grid(row=0, sticky='ew')
        centerFrame.grid(row=1, sticky='ew')
        self.responseFrame.grid(row=3, sticky='ew')
        divs = ttk.Notebook(centerFrame)
        self.headerPage = ttk.Frame(divs)
        self.bodyPage = ttk.Frame(divs)
        divs.add(self.headerPage, text='Headers')
        divs.add(self.bodyPage, text='Body')
        self.updateFrame = tk.Frame(self.bodyPage, width=360, height=20)
        self.responseDiv = ttk.Notebook(self.responseFrame)

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
        # First Division
        self.headersKey.grid(row=0, column=0, padx=3)
        self.headersVal.grid(row=0, column=1, padx=3)
        self.addHButton.grid(row=1, column=0)
        # Split
        self.formData.grid(row=0, column=0)
        self.urlEncoded.grid(row=0, column=1)
        self.rawData.grid(row=0, column=2)
        self.binaryFile.grid(row=0, column=3)
        self.updateFrame.grid(row=1, columnspan=4, sticky='ew', padx=6)
        # Bottom Layer
        self.Submit = tk.Button(self.responseFrame, text='Submit', command=self.Submit)
        self.Submit.grid(row=0, column=0)

    # Create the HTTP Request ------------------------------------------------------------------------------------------
    def Submit(self):
        htemp = []
        btemp = []
        newRequest = self.UpdateRequestType()
        address = self.addressLabel.get()
        print('{} {}'.format(newRequest, address))

        for item in self.headerPage.grid_slaves():
            if isinstance(item, tk.Entry): # Check how many header Entry boxes exist
                if item.get(): # Check if anything was entered
                    htemp.append(item.get())

        headers = dict(zip(*[iter(reversed(htemp))]*2))
        print(headers)

        for item in self.updateFrame.grid_slaves():
            if isinstance(item, tk.Entry):
                if item.get():
                    btemp.append(item.get())

        body = dict(zip(*[iter(reversed(btemp))]*2))
        print(body)

        if newRequest == 'GET':
            r = requests.get(url=address, headers=headers)
        elif newRequest == 'POST':
            r = requests.post(url=address, headers=headers, data=body)

        self.CreateResponse(r)

    def AddHeader(self):
        newKey = tk.Entry(self.headerPage)
        newVal = tk.Entry(self.headerPage, width=39)
        newKey.grid(row=self.c_row, column = 0)
        newVal.grid(row=self.c_row, column = 1)
        self.addHButton.grid(row=self.c_row+1, column=0)
        self.c_row += 1

    def UpdateBody(self):
        print(self.val.get())
        selection = self.val.get()
        self._blankWidgets()
        if selection == 1:
            key = tk.Label(self.updateFrame, text='Key: ')
            value = tk.Label(self.updateFrame, text='Value: ')
            formKey = tk.Entry(self.updateFrame)
            formVal = tk.Entry(self.updateFrame, width=30)
            key.grid(row=0, column=0)
            formKey.grid(row=0, column=1)
            value.grid(row=0, column=2)
            formVal.grid(row=0, column=3)
        elif selection == 2:
            key = tk.Label(self.updateFrame, text='Key: ')
            value = tk.Label(self.updateFrame, text='Value: ')
            encodedKey = tk.Entry(self.updateFrame)
            encodedVal = tk.Entry(self.updateFrame, width=30)
            key.grid(row=0, column=0)
            encodedKey.grid(row=0, column=1)
            value.grid(row=0, column=2)
            encodedVal.grid(row=0, column=3)
        elif selection == 3:
            self.formatSel.set('Text')
            self.formatSel.trace('w', self.UpdateFormat)
            entry = tk.Text(self.updateFrame)
            entryFormat = tk.OptionMenu(self.updateFrame, self.formatSel, 'Text', 'JSON', 'HTML', 'XML')
            entry.grid(row=1, column=0)
            entryFormat.grid(row=0, column=0)
        elif selection == 4:
            placeHolder = tk.Label(self.updateFrame, text='Binary file upload coming soon')
            placeHolder.grid()

    ## Begin Helpers ---------------------------------------------------------------------------------------------------
    def UpdateFormat(self, *args):
        print('Format type is: {}'.format(self.formatSel.get()))

    def UpdateRequestType(self, *args):
        return self.requestType.get()

    def _blankWidgets(self):
        for item in self.updateFrame.grid_slaves():
            item.grid_forget()

    def CreateResponse(self, data):
        newResponse = ttk.Frame(self.responseDiv)
        self.responseDiv.add(newResponse, text='Response {}'.format(self.r_num))
        response = tk.StringVar()
        response.set(data.text)
        responseBox = tk.Text(newResponse)
        responseBox.insert(1.0, response.get())
        self.r_num+=1
        self.responseDiv.grid()
        responseBox.grid()

## End Class -----------------------------------------------------------------------------------------------------------

root = tk.Tk()
app = Application(root)
root.mainloop()
