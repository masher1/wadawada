from tkinter import *
from tkinter import scrolledtext
import requests
import json
from tkinter.ttk import *

master = Tk()
master.title("Welcome to Wadawada")
lbl = Label(master, text="Enter up to 5 ingredients that you have: ")
lbl.grid(row=0)

e2 = Entry(master)
e2.grid(row=0, column=1)

mying = []
moveon = False

def ingreddy():
    if len(mying)<5:
        mying.append(e2.get())
        print(mying)
    else:
        def eat():
            iwanttoeat = p2.get()
            txt = scrolledtext.ScrolledText(lister, width=100, height=20)
            txt.grid(row=3, column=0, sticky=W)
            req_ = requests.get('https://api.wegmans.io/meals/recipes/'+iwanttoeat+'/?api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
            jp = req_.json()

            if "ingredients" in jp:
                for each in jp['ingredients']:
                    if "sku" in each:
                        if contains(mying, int(each['sku'])) == False:
                            donthave.append((each['name'],each['sku']))

            txt.insert(INSERT, "YOU DONT HAVE ANY: \n\n")
            for d in donthave:
                txt.insert(INSERT, str(d[0]) + '\n')
            txt.insert(INSERT, "\nBUY THESE INGREDIENTS FROM WEGMANS!")

        calculate_button.grid_remove()
        master.destroy()
        lister = Tk()
        lister.title("We found these recipes")
        lister.geometry('900x700')
        txt = scrolledtext.ScrolledText(lister, width=100, height=20)
        txt.grid(row=0,column=0,sticky=W)
        p2 = Entry(lister)
        p2.grid(row=1,column=0, sticky=W)
        eat = Button(lister,text = "eat!",command = eat)
        eat.grid(row=2, column=0, sticky=W)
        # mying = [23792,42994,11232,164850,31197,32200,92624,92646,94177,80133,33864] #list of sku's
        meals = list()
        donthave = list()
        num = 0
        sub_key = "&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa"

        def contains(list, number):
            for each in list:
                if number == each:
                    return True
            return False

        for each in mying:
            thing = str(each)
            req_allrec = requests.get(
                'https://api.wegmans.io/meals/recipes/search?query=' + thing + '&api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
            j = req_allrec.json()
            if "results" in j:
                for things in j['results']:
                    meals.append((things['name'], things['id']))

        for p in meals:
            txt.insert(INSERT,str(p)+'\n')


        lister.mainloop()


        ###########################################################################



calculate_button = Button(master, text="Calculate", command=ingreddy)
calculate_button.grid(row=1, column=1, sticky=W)

master.geometry('400x400')

vegan = IntVar()
vegetarian = IntVar()
gluten = IntVar()

def func():
    if vegan.get() == 1:
        mying.append("Vegan")
def func1():
    if vegetarian.get() == 1:
        mying.append("Vegetarian")
def func2():
    if gluten.get() == 1:
        mying.append("Gluten")


chk = Checkbutton(master, text="Vegan", variable=vegan, command=func).grid(row=3, sticky=W)
chk1 = Checkbutton(master, text="Vegetarian", variable=vegetarian, command=func1).grid(row=4, sticky=W)
chk2 = Checkbutton(master, text="Gluten", variable=gluten, command=func2).grid(row=5, sticky=W)

########################***MEAL ANALYZRE***################################


# the goal is to input an array of skus and return meals where 60% of the ingredients are contained in the list







master.mainloop()

