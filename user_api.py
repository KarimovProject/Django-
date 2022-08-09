
import requests
import json
from pprint import pprint
def get_male_users(data):
    result = data["results"][0]
    name = result['name']
    first = name['first']
    last = name['last']
    country = result['location']['country']
    age = result['dob']['age']
    gender = result['gender'] 

    data1 =  {
                    "first_name":first,
                    "last_name": last,
                    "age":age,
                    "country": country,
                }
    return data1

def get_def(n):
    jami = []
    for i in range(n):
        r = requests.get('https://randomuser.me/api/')
        data = r.json()
        a = get_male_users(data)
        jami.append(a)
        print(f"{len(jami)}/{n}")
    tayyor={"results": jami}
    return tayyor
ready = get_def(200)
data_json = json.dumps(ready, indent=4)

f = open("data_json", "w")

f.write(data_json)
