import json
import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64

# req_allrec = requests.get('https://api.wegmans.io/meals/recipes?api-version=2018-10-18&Subscription-Key=a5f4b2e170ca42c3b3aaad43d8ed27e0')
# j = req_allrec.json()
# num = 0
# sub_key = "&Subscription-Key=a5f4b2e170ca42c3b3aaad43d8ed27e0"

headers = {
    # Request headers
    'Subscription-Key': 'a5f4b2e170ca42c3b3aaad43d8ed27e0',
}
params = urllib.parse.urlencode({
    # Request parameters
    'results': '100',
    'page': '1',
})
choice= str(input("What type of food do you eat? ")) # vegeterian, vegan, anything

req_allrec = requests.get('https://api.wegmans.io/meals/recipes/search?query='+choice+'&api-version=2018-10-18&Subscription-Key=a5f4b2e170ca42c3b3aaad43d8ed27e0')
q = req_allrec.json()
num = 0

for each in q['results']:
     print(each['name'])
print("\n")
try:
    conn = http.client.HTTPSConnection('api.wegmans.io')
    conn.request("GET", "/meals/recipes/search?query=" + choice + "&api-version=2018-10-18&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
