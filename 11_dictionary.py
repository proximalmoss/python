dict={
    "key":"value",
    "harry":"code",
    "marks":100,
    "list":[1,2,9],
    "anotherdict":{'harry':'player'}
    }
print(dict)
print(dict["key"])
print(dict['anotherdict']['harry'])
#methods of dictionary
a=dict.items()
print(a)
b=dict.keys()
print(b)
updatedict={
    "friend": "sam"
    }
c=dict.update(updatedict)
print(c)
d=dict.get("key")
print(d)