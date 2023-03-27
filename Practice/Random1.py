import requests
import pprint

url = 'https://api.genshin.dev/characters/zhongli'
response = requests.get(url)

data = response.json()

for key in data:
    print(str(key) + ": " + str(data[key]))

print("\nTHE PPRINT VERSION\n")
pprint.pprint(data)