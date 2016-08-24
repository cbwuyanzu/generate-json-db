# coding: utf-8
import json
import datetime
import random
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
    # max_phi = 0;
    # max_level = 0;
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
        timestamp = long(1000 * time.mktime(time.strptime(str(key), '%Y-%m-%d %H:%M:%S')))
        date_time = datetime.datetime.fromtimestamp(timestamp / 1000)
        num = counts[key]
        u_avg = u_sum[key] / num
        p_avg = p_sum[key] / num
        i_avg = i_sum[key] / num
        w_avg = w_sum[key] / num
        cos_phi_avg = cos_phi_sum[key] / num
        # if cos_phi_avg > max_phi:
        #     max_phi = cos_phi_avg
        #     print max_phi
        on_off = (1 if p_avg > 1 else 0)
        level = int(p_avg * 10 / 115) * 10
        # if level > max_level:
        #     max_level = level
        #     print max_level
        if level > 100:
            level = 100
        # print level
        avg_datapoint = [timestamp, on_off, level, u_avg, i_avg, p_avg, cos_phi_avg, w_avg, str(date_time)]
        datapoints.append(avg_datapoint)
        # print len(datapoints), "++++", (timestamp - 1469980800000) / 1800 / 1000 + 1 #date_time check if datapoint fills all
    datapoints_all = extend_data(datapoints, -40) + extend_data(datapoints, -20) + datapoints + extend_data(datapoints,
                                                                                                            20)
    # datapoints_all = datapoints
    print len(datapoints_all)
    data_dict[u'values'] = datapoints_all
    return json.dumps(data_dict)


def extend_data(raw_data, offset):
    datapoints_new = []
    # max_phi_new = 0;
    for x in raw_data:
        d_raw = datetime.datetime.fromtimestamp(x[0] / 1000)
        d_new = d_raw + datetime.timedelta(offset)
        time_stamp_new = int(1000 * time.mktime(time.strptime(str(d_new), '%Y-%m-%d %H:%M:%S')))
        u_new = x[3] + 0.15 * random.uniform(-1, 1) * x[3]
        i_new = x[4] + 0.15 * random.uniform(-1, 1) * x[4]
        p_new = x[5] + 0.15 * random.uniform(-1, 1) * x[5]
        cos_phi_new = x[6] + 0.025 * random.uniform(-1, 1) * x[6]
        # if cos_phi_new > 0.995:
        #     cos_phi_new = 0.995000
        # if cos_phi_new > max_phi_new:
        #     max_phi_new = cos_phi_new
        #     print max_phi_new
        w_new = x[7] + 13.32 * offset / 20
        on_off_new = (1 if p_new > 1 else 0)
        level_new = int(p_new * 10 / 115) * 10
        if level_new > 100:
            level_new = 100
        datapoint_new = [time_stamp_new, on_off_new, level_new, u_new, i_new, p_new, cos_phi_new, w_new, str(d_new)]
        if (time_stamp_new >= 1467302400000) and (time_stamp_new < 1472659200000):
            datapoints_new.append(datapoint_new)
    return datapoints_new


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
    # get_data(5, 17806)
    f = open("1.json", "w+")
    console_print = get_data(5, 17810)
    # print console_print
    f.write(console_print)
    f.close()
