## json file
## java script object notation
# {
#name : 'abc'
#}

import json

employee = {'name':'abcd','age':30}
# employee_lists = ['abcd1','efgh']
# json_str = json.dumps(employee)
#
# print(json_str,type(json_str))
#
# json_employee_dump = json.dumps(employee_lists)
# print(json_employee_dump,type(json_employee_dump))
# # print(len(json_employee_dump))
# obj = json.loads(json_str)
# print(len(json.loads(json_employee_dump)))
# print(obj['name'])

# with open("test.json",'w') as fd:
#     json.dump(employee,fd)

from pprint import pprint
chars = {x:ord(x) for x in "ABCDEFGHIJKL"}
# print(chars)
with open("test.json",'r') as fd:
    details = json.load(fd)
    print(details)


# with open("test_list.json", 'w') as fd:
#     nos = [x for x in range(1,5)]
#     json.dump(nos,fd)
#     # print(details)
#     # pprint(chars, indent=8)
#     #print(fd.readlines())
import xmltodict

xml_file = """<?xml version="1.0" encoding="UTF-8"?>
<note>
  <to>Tove</to>
  <from>Jani</from>
  <heading>Reminder</heading>
  <body>Don't forget me this weekend!</body>
</note>
"""
import xmltodict

with open("test_list.json", 'r') as fd:

    nos =  json.load(fd)
    print(type(nos))


text = xmltodict.parse(xml_file)
print(text['note'])