from datetime import datetime
from lib.Database import Database
import json


class Parser:
    def __init__(self):
        self.time = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        print('init parser...')

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
            parent_id = self._insert(db, city_id, '0', dist)

            sub_districts = dist['districts']
            for j in range(len(sub_districts)):
                sub_dist = sub_districts[j]
                sub_id = self._insert(db, city_id, parent_id, sub_dist)
                print(sub_id)

    def _insert(self, db, city_id, parent_id, district):
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
        return insert_id
