import json
import time
import xlrd


def get_data(row_s, row_e):
    filename = 'RtuDetail1469877712898.xls'
    tablename = 'Sheet2'
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_name(u'Sheet2')
    # print type(table.cell(row_s, 0).value)
    data_dict = {u'name': table.cell(row_s, 0).value}
    datapoints = []
    for x in range(row_s, row_e):
        data_row = table.row_values(x)
        datapoint = data_row[1:]
        datapoint[0] = int(1000 * time.mktime(time.strptime(str(datapoint[0]), '%Y-%m-%d %H:%M:%S')))
        datapoints.append(datapoint)
    data_dict[u'values'] = datapoints
    return json.dumps(data_dict)
    # return data_dict[u'name']


if __name__ == "__main__":
    f = open("example.json", "w+")
    console_print = get_data(5, 7)
    print console_print
    f.write(console_print)
    f.close()
