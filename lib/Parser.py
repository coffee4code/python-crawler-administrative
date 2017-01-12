from datetime import datetime
from lib.Database import Database
import json


class Parser:
    def __init__(self):
        self.time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

    def parse(self, json_data, city_id):
        db = Database()
        districts = []

        if city_id == 3:
            districts = json.loads(json_data)["districts"][0]["districts"][0]["districts"]

        if city_id == 2:
            districts = json.loads(json_data)["districts"][0]["districts"][0]["districts"]

        if city_id == 4:
            districts = json.loads(json_data)["districts"][0]["districts"]

        for i in range(len(districts)):
            dist = districts[i]
            parent_id = self.insert(db, city_id, '0', dist)

            sub_districts = dist['districts']

            if len(sub_districts) == 0:
                sub_districts = [dist]

            for j in range(len(sub_districts)):
                sub_dist = sub_districts[j]
                self.insert(db, city_id, parent_id, sub_dist)

    def insert(self, db, city_id, parent_id, district):
        sql = '''INSERT INTO tbarea VALUES ({0},{1},{2},{3},{4},{5},{6},{7},{8})'''.format(
            'NULL',
            '"' + str(parent_id) + '"',
            '"' + str(city_id) + '"',
            '"' + district['name'] + '"',
            '"' + '' + '"',
            '"' + '1' + '"',
            '"' + '1' + '"',
            '"' + self.time + '"',
            '"' + '0000-00-00 00:00:00' + '"'
        )
        insert_id = db.execute(sql)
        self._log(city_id, parent_id, district, insert_id)
        return insert_id

    def _log(self, city_id, parent_id, district, insert_id):
        if int(parent_id) == 0:
            print("\r\n\r\n\r\n"+'----------------------------------------------------------------------------')
        log_str = '' if int(parent_id) == 0 else '--------'
        log_str += '插入数据：' + "\t"
        log_str += 'insert_id=' + str(insert_id) + "\t"
        log_str += 'city_id=' + str(city_id) + "\t"
        log_str += 'name=' + district["name"] + "\t"
        log_str += 'parent_id=' + str(parent_id) + "\t"
        print(log_str)
