# coding=utf-8
import json
import random


def generate_eight():
    names = {2: 'CTP East 2 2b425', 3: 'CTP East 3 2b402', 4: 'CTP East 4 2b412', 5: 'CTP East 5 2b3e5',
             6: 'CTP East 6 297b4', 7: 'CTP East 7 2b3dc', 8: 'CTP East 8 2b407'}
    json_file = '1.json'
    f = open(json_file)
    json_str = f.read()
    result = json.loads(json_str)
    data_list = result[u'values']
    for x in names:
        data_dict = {u'name': names[x]}
        offset_w = int(random.uniform(-1, 1) * 40)
        datapoints = []
        for d in data_list:
            u_new = d[3] + 0.15 * random.uniform(-1, 1) * d[3]
            i_new = d[4] + 0.15 * random.uniform(-1, 1) * d[4]
            p_new = d[5] + 0.15 * random.uniform(-1, 1) * d[5]
            cos_phi_new = d[6] + 0.15 * random.uniform(-1, 1) * d[6]
            w_new = d[7] + offset_w
            on_off_new = (1 if p_new > 1 else 0)
            level_new = int(p_new * 100 / 115)
            datapoint_new = [d[0], on_off_new, level_new, u_new, i_new, p_new, cos_phi_new, w_new, d[8]]
            datapoints.append(datapoint_new)
        data_dict[u'values'] = datapoints
        json_str_dst = json.dumps(data_dict)
        f = open(str(x) + ".json", "w+")
        f.write(json_str_dst);
        f.close()


if __name__ == '__main__':
    generate_eight()
