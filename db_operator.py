import psycopg2
import json
from get_lamp_data import get_data


def man_db():
    db_name = "postgres"
    user = "postgres"
    password = "1220yangA"
    host = "localhost"
    port = "5432"
    result = json.loads(get_data(5, 7))
    conn = psycopg2.connect(database=db_name, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    # cur.execute("CREATE TABLE test(id serial PRIMARY KEY, num integer,data varchar);")
    name = result[u'name']
    for x in result[u'values']:
        print x[5]
        cur.execute(
            "INSERT INTO lamps(lamp_name,timestamp, voltage, current, power,power_factor, energy) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (name, x[0], x[1], x[2], x[3], x[4], x[5]))
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    #
    man_db()
