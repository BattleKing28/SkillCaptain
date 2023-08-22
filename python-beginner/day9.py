dict = {"name": "John"}

# add new key value pair
dict["age"] = 29
print(dict)

# remove a key value pair
del dict["age"]
print(dict)

# update value of a key
dict["name"] = "Mark"
print(dict)

# check if key exists
if "name" in dict:
    print("name exists in dictionary")

# add new key value pair
dict["age"] = 29
print(dict)

# get all keys
print(dict.keys())

# get all values
print(dict.values())
