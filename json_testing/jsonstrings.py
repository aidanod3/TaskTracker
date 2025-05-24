#  https://www.youtube.com/watch?v=-51jxlQaxyA

import json

json_string = '''
    {
        "students": [
            {
                "id": 1,
                "name": "Tim",
                "age": 21,
                "full-time": true
            },
            {
                "id": 2,
                "name": "Joe",
                "age": 33,
                "full-time": false
            }
        ]
    }    
'''

data = json.loads(json_string)  # loads a json string (s for string)
print(data)
# print(type(data))  # data is stored as a python dict

# print(data['students'][0])

# dump python dict into a json string (s for string).
# indent formats it nicely.
# sort_keys sorts the keys.
data['test'] = True
new_json = json.dumps(data, indent=2, sort_keys=True)
print(new_json)

# note: json.load or json.loads can return either a list or a dict depending on the structure of the json file.
