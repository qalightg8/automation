import json

future_json_data = {
    'man': {
        'first_name': 'Artem',
        'last_name': 'Svarych',
        'birth_year': 1980
    },
    'woman': {
        'first_name': 'Vira',
        'last_name': 'Svarych',
        'birth_year': 1981
    }
}

json_data = json.dumps(future_json_data)

# print(future_json_data)
# print(json_data)

## Write json into file
with open('json_data.json', 'w') as file:
    file.write(json_data)

## Read json from file and convert to "dict"
with open('json_data.json', 'r') as file:
    data = json.loads(file.read())
    print(data)
