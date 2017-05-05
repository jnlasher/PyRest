#!/usr/bin/env/Python

import tkinter as tk
from tkinter import ttk
import requests
import json


class Application:
    def __init__(self, master):
        #SETUP
        self.master = master
        master.title('PyREST')
        master.minsize(width=800, height=600)
        self.c_row = 0
        self.h_row = 0
        self.r_num = 1
        self.val = tk.IntVar()
        self.formatSel = tk.StringVar()

        # GENERATE FRAMES
        topFrame = tk.Frame(master, bg='#1e3f72', width = 800, height=50, padx=30, pady=3)
        centerFrame = tk.Frame(master, bg='#1e3f72', width=800, height=40, padx=30, pady=3)
        self.responseFrame = tk.Frame(master, bg='#d7d5b4', width = 800, height = 45, padx=30, pady=3)
        topFrame.grid_propagate(False)
        topFrame.grid(row=0, sticky='ew')
        centerFrame.grid(row=1, sticky='ew')
        self.responseFrame.grid(row=3, sticky='ew')
        divs = ttk.Notebook(centerFrame)
        self.headerPage = ttk.Frame(divs, width=200, height=60)
        self.bodyPage = ttk.Frame(divs, width=200, height=60)
        divs.add(self.headerPage, text='Headers')
        divs.add(self.bodyPage, text='Body')
        self.updateFrame = tk.Frame(self.bodyPage, width=360, height=40)
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
        self.addBButton = tk.Button(self.updateFrame, text = 'Add Key/Value', command = self.AddBody)

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
        newRequest = self.UpdateRequestType()
        address = self.addressLabel.get()
        err_flag = None

        headers, body = self._requestBuilder()
        try:
            r = requests.request(method=newRequest, url=address, headers=headers, data=body, verify=False)
        except requests.exceptions.RequestException as err:
            r = err
            err_flag = True

        self.CreateResponse(r, err_flag)

    def AddHeader(self):
        newKey = tk.Entry(self.headerPage)
        newVal = tk.Entry(self.headerPage, width=39)
        self.c_row += 1
        newKey.grid(row=self.c_row, column = 0)
        newVal.grid(row=self.c_row, column = 1)
        self.addHButton.grid(row=self.c_row+1, column=0)

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
            self.addBButton.grid(row=1, column=1)
        elif selection == 2:
            key = tk.Label(self.updateFrame, text='Key: ')
            value = tk.Label(self.updateFrame, text='Value: ')
            encodedKey = tk.Entry(self.updateFrame)
            encodedVal = tk.Entry(self.updateFrame, width=30)
            key.grid(row=0, column=0)
            encodedKey.grid(row=0, column=1)
            value.grid(row=0, column=2)
            encodedVal.grid(row=0, column=3)
            self.addBButton.grid(row=1, column=1)
        elif selection == 3:
            self.formatSel.set('Text')
            self.formatSel.trace('w', self.UpdateFormat)
            self.message = tk.Text(self.updateFrame, height=6)
            entryFormat = tk.OptionMenu(self.updateFrame, self.formatSel, 'Text', 'JSON', 'HTML', 'XML')
            self.message.grid(row=1, column=0)
            entryFormat.grid(row=0, column=0)
            self.addBButton.grid_forget()
        elif selection == 4:
            placeHolder = tk.Label(self.updateFrame, text='Binary file upload coming soon')
            placeHolder.grid()
            self.addBButton.grid_forget()

    def AddBody(self):
        newKey = tk.Entry(self.updateFrame)
        newVal = tk.Entry(self.updateFrame, width=30)
        self.h_row+=1
        newKey.grid(row=self.h_row, column = 1)
        newVal.grid(row=self.h_row, column = 3)
        self.addBButton.grid(row=self.h_row+1, column=1)


    ## Begin Helpers ---------------------------------------------------------------------------------------------------
    def UpdateFormat(self, *args):
        print('Format type is: {}'.format(self.formatSel.get()))

    def UpdateRequestType(self, *args):
        return self.requestType.get()

    def _blankWidgets(self):
        for item in self.updateFrame.grid_slaves():
            item.grid_forget()

    def _updateData(self, data):
        dataType = self.formatSel.get()
        dataKey = {'Text':r'{}'.format(data), 'JSON':json.dumps(data), 'HTML':data, 'XML':data}
        payload = dataKey.get(dataType)
        return payload

    def _requestBuilder(self):
        htemp = []
        btemp = []

        for item in self.headerPage.grid_slaves():
            if isinstance(item, tk.Entry): # Check how many header Entry boxes exist
                if item.get(): # Check if anything was entered
                    htemp.append(item.get())

        headers = dict(zip(*[iter(reversed(htemp))]*2))
        print(headers)

        bodyStatus = self.val.get()

        if bodyStatus == 1 or bodyStatus == 2:
            for item in self.updateFrame.grid_slaves():
                if isinstance(item, tk.Entry): # Check how many header Entry boxes exist
                    if item.get(): # Check if anything was entered
                        btemp.append(item.get())
            payload = dict(zip(*[iter(reversed(btemp))]*2))
        elif bodyStatus == 3:
            data = self.message.get('1.0', 'end-1c')
            payload = self._updateData(data)
        else:
            payload = None
        print('the payload is: ')
        print(payload)
        return headers, payload

    def CreateResponse(self, data, error):
        newResponse = ttk.Frame(self.responseDiv)
        self.responseDiv.add(newResponse, text='Response {}'.format(self.r_num))
        response = tk.StringVar()
        if not error:
            response.set(data.text)
        else:
            response.set('An error occurred during your request. The code is: {}'.format(data))

        responseBox = tk.Text(newResponse)
        responseBox.insert(1.0, response.get())
        self.r_num+=1
        self.responseDiv.grid()
        responseBox.grid()

## End Class -----------------------------------------------------------------------------------------------------------

root = tk.Tk()
app = Application(root)
root.mainloop()
