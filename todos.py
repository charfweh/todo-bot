import json
f = open('configs.json')
data = json.load(f)
print(data['bot_token'])