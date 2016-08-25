# coding: utf-8
import json

for i in range(1, 9):
    json_file = str(i) + '.json'
    f = open(json_file)
    json_str = f.read()
    result = json.loads(json_str)
    f.close()
    data_list = result[u'values']
    count = 0
    data_list_new = []
    for x in data_list:
        # print (x[0] - 1467304200000) / 1800000, "+++", count
        x = x[0:-1]
        if count == 0:
            print x
        count += 1
        data_list_new.append(x)
    result[u'values'] = data_list_new
    json_file = 'light' + str(i) + '.json'
    f = open(json_file, "w")
    f.write(json.dumps(result))
