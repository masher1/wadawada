# WegChef
import json
import requests

file = open("sku.txt","w")
thing = '164850'
req_allrec = requests.get('https://api.wegmans.io/meals/recipes/search?query='+ thing +'&api-version=2018-10-18&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa')
j = req_allrec.json()
num = 0
sub_key = "&Subscription-Key=ecfcb1444dfb46db9e12517128dbdbaa"

for each in j['results']:
    print(each['name'])

    # print(each['name'])
    # reqsin = requests.get("https://api.wegmans.io" + each['_links'][0]['href'] + sub_key)
    # sample = reqsin.json()
    # if "ingredients" in sample:
    #     for each in sample['ingredients']:
    #         if "sku" in each:
    #              #print(each['name'])
    #              print(each['sku'])
    #              #file.write(each['name']+"   ")
    #              file.write(str(each['sku'])+"\n")
