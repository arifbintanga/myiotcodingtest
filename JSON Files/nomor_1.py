# Python program to update
# JSON

import requests 
import json

response_users = requests.get("http://jsonplaceholder.typicode.com/users")
listOfUsers = json.loads(response_users.text)

# Opening JSON file
with open("e:\CAD-IT\JSON Files\salary_data.json") as file:
    # returns JSON object as a dictionary
    data = json.load(file)

for (users,salaryIDR) in zip(listOfUsers,data["array"]):
    users.update(salaryIDR)

#call for currency multiplier
response_currency_multiplier = requests.get("https://free.currconv.com/api/v7/convert?q=IDR_USD&compact=ultra&apiKey=eb4e91514761eb46a67e")
currency_multiplier = json.loads(response_currency_multiplier.text)

for users in listOfUsers:
    temp_salary = float(users["salaryInIDR"])*currency_multiplier["IDR_USD"]
    users["salaryInUSD"]= temp_salary    

#print users with updated salary in USD
for users in listOfUsers:
    print(users)

with open("nomor_1.json", "w") as final:
   json.dump(listOfUsers, final)