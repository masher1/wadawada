# the goal is to input an array of skus and return meals where 60% of the ingredients are contained in the list

import requests
import json


mying = [23792,42994,11232,164850,31197,32200,92624,92646,94177,80133,33864] #list of sku's

thing = '164850'
meals = list()
donthave = list()
#req_allrec = requests.get('https://api.wegmans.io/meals/recipes/search?query='+ thing +'&api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
#j = req_allrec.json()
num = 0
sub_key = "&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa"


def contains(list, number):
    for each in list:
        if number == each:
            return True
    return False

for each in mying:
    thing = str(each)
    req_allrec = requests.get('https://api.wegmans.io/meals/recipes/search?query='+ thing +'&api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
    j = req_allrec.json()
    for things in j['results']:
        meals.append((things['name'],things['id']))

# for p in meals:
#     num_have = 0
#     num_ing = 0
#     reqe = requests.get(
#         'https://api.wegmans.io/meals/recipes/' + str(p[1]) + '/?api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
#     jp = reqe.json()
#     if "ingredients" in jp:
#         for each in jp['ingredients']:
#             if "sku" in each:
#                 if contains2(mying,each['sku']):
#                     num_have +=1
#                 num_ing += 1
#     p[2]: num_have/num_ing
for p in meals:
    print(p)

iwanttoeat = input("\n WHAT THE FUCK DO YOU WANT TO EAT ?!\n")

req_ = requests.get('https://api.wegmans.io/meals/recipes/'+iwanttoeat+'/?api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
jp = req_.json()

if "ingredients" in jp:
    for each in jp['ingredients']:
        if "sku" in each:
            if contains(mying, int(each['sku'])) == False:
                donthave.append((each['name'],each['sku']))

print("YOU DONT HAVE ANY FUCKING: \n")

for d in donthave:
    print(d[0])

print("\nGO BUY THAT SHIT FROM WEGGIES MOTHER FUCKA")