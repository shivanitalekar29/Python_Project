import simplejson

"""Write a Python program to convert the Python dictionary object (sort by key) to
# JSON data. Print the object members with indent level 4."""


print(simplejson.dumps(dict(c=21, b="Shivani", a=1.2), sort_keys=True))
