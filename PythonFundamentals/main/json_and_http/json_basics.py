import json
import urllib.request

trainee_data = {"name":"Alessandra", "course": "data engineering"}

print(type(trainee_data))

# json.dump() - writes JSON to a file object
# json.dumps() serializes json to a formatted string

trainee_data_json_string = json.dumps(trainee_data) # changed our dictionary into a string, which is ow JSON objects are represented in most programming lanagues
print(trainee_data_json_string)
print(type(trainee_data_json_string))

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(trainee_data, jsonfile)

# load - read json files (takes a file)

with open('new_json_file.json', 'r') as jsonfile:
    trainee = json.load(jsonfile) #takes a json string and converts into a dictionary
    print(type(trainee))
    print(trainee)
    print(trainee["name"])
    print(trainee["course"])

# json.loads() - converts a JSON string (takes a string)

trainer_data = '{"name":"Nish", "age":22}'
print(type(trainer_data))

parsed_json_data =  json.loads(trainer_data)
print(parsed_json_data)
print(type(parsed_json_data))


# using request library

url = "https://api.postcodes.io/postcodes/EC2y5as"
with urllib.request.urlopen(url) as raw_json:
    converted_json = json.load(raw_json)
    print(converted_json)
    print(converted_json["status"])
    print(converted_json["result"])
    print(converted_json["result"]["country"])
    with open('postcode.json', 'w') as jsonfile:
        json.dump(converted_json,jsonfile)

