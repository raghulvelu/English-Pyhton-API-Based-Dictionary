import pprint
import requests

meaning = input("Word? ")
url = f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{meaning}'
response = requests.get(url)
response.json()

pprint.pprint(response.json()[0]['word'])
pprint.pprint(response.json()[0]['meanings'][0]['partOfSpeech'])
pprint.pprint(response.json()[0]['meanings'][0]['definitions'][0]['definition'])