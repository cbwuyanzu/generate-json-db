# coding=utf-8
import MySQLdb
import json


def man_db(file_str):
    db_name = "dearabao"
    user = "root"
    password = "1220yangA"
    host = "127.0.0.1"
    port = 3306
    json_file = file_str + '.json'
    f = open(json_file)
    json_str = f.read()
    result = json.loads(json_str)
    print len(result[u'values'])
    conn = MySQLdb.connect(db=db_name, user=user, passwd=password, host=host, port=port)
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
    name = result[u'name']
    for x in result[u'values']:
        # print x[5]
        cur.execute(
            "INSERT INTO lamps(lamp_name,updatetime, on_off, level, voltage, current, power,power_factor, energy) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (name, x[8], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    for s in range(2, 9):
        man_db(str(s))
