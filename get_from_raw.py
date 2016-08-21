# coding: utf-8
import json
import time
import xlrd
from collections import defaultdict
from collections import OrderedDict


def get_data(row_s, row_e):
    counts = defaultdict(int)
    u_sum = defaultdict(float)
    p_sum = defaultdict(float)
    i_sum = defaultdict(float)
    w_sum = defaultdict(float)
    cos_phi_sum = defaultdict(float)
    filename = 'RtuDetail1471758340358.xls'
    tablename = u'数据'
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name(tablename)
    # print type(table.cell(row_s, 0).value)
    data_dict = {u'name': table.cell(row_s, 1).value}
    datapoints = []
    for x in range(row_s, row_e):
        data_row = table.row_values(x)
        datapoint = data_row[2:8]
        # print len(datapoint[0])
        datapoint[0] = get_roundtime(datapoint)
        counts[datapoint[0]] += 1
        u_sum[datapoint[0]] += float(datapoint[1])
        p_sum[datapoint[0]] += float(datapoint[2])
        i_sum[datapoint[0]] += float(datapoint[3])
        w_sum[datapoint[0]] += float(datapoint[4])
        cos_phi_sum[datapoint[0]] += float(datapoint[5])
    for key in OrderedDict(sorted(counts.items(), key=lambda t: t[0])):
        timestamp = int(1000 * time.mktime(time.strptime(str(key), '%Y-%m-%d %H:%M:%S')))
        num = counts[key]
        u_avg = u_sum[key] / num
        p_avg = p_sum[key] / num
        i_avg = i_sum[key] / num
        w_avg = w_sum[key] / num
        cos_phi_avg = cos_phi_sum[key] / num
        avg_datapoint = [timestamp, u_avg, p_avg, i_avg, w_avg, cos_phi_avg]
        datapoints.append(avg_datapoint)
    data_dict[u'values'] = datapoints
    return json.dumps(data_dict)


def get_roundtime(list_data):
    data_time = list_data[0]
    hour_data_time = data_time[0:14]
    # print hour_data_time
    if int(data_time[14:16]) > 30:
        minite_data_time = u'30:00'
    else:
        minite_data_time = u'00:00'
    # print minite_data_time
    data_time = hour_data_time + minite_data_time
    # print data_time
    return data_time


if __name__ == "__main__":
    # print get_data(5, 300)
    # get_roundtime(get_data(5, 9)[u'values'][0])
    f = open("1.json", "w+")
    console_print = get_data(5, 17806)
    # print console_print
    f.write(console_print)
    f.close()
