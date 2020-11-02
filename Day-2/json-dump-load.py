# import json
# data = {
#     "president": {
#         "name": "Zaphod Beeblebrox",
#         "species": "Betelgeusian"
#     }
# }

# # serialisation
# with open("data_file.json", "w") as write_file:
#     json.dump(data, write_file)
    
# # Note that dump() takes two positional arguments: (1) the data object to be serialized, and (2) the file-like object to which the bytes will be written.

# # Or, if you were so inclined as to continue using this serialized JSON data in your program, you could write it to a native Python str object.
# # or
# json_string = json.dumps(data)

# # Deserialisation
# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)

# # or

# data=json.dumps(json_string)
import json

# serialising

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))

# Deserialising

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')