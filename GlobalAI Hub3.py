d = {}

print(d)
print(type(d))
d = {"python":1, "course":2}
print(d)
my_dictionary = {"machine":"learning", "artificial":"intelligence" }
print(my_dictionary)
print(my_dictionary["artificial"])
print(my_dictionary.get("machine"))
my_dictionary["java"] = "programming"
print(my_dictionary)
my_dictionary["java"] = "programming"
print(my_dictionary)
my_dictionary["ruby"] = "programming"
print(my_dictionary)
var = my_dictionary["ruby"]
my_dictionary.update({"data": "science"})
print(my_dictionary)
my_dictionary.update({"machine": "intelligenge"})
print(my_dictionary)
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
for k in my_dictionary.keys():
  print(k)
for v in my_dictionary.values():
  print(v)
for k,v in my_dictionary.items():
  print("Key: " + k + " Value: " + v)
my_dictionary[1] = [3,4,5]
print(my_dictionary)

#show key with list
