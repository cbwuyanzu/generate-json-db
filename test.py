import json

json_file = '1.json'
f = open(json_file)
json_str = f.read()
result = json.loads(json_str)
data_list = result[u'values']
print len(data_list)
count = 0
for x in data_list:
    print (x[0] - 1467304200000) / 1800000, "+++", count
    count += 1
