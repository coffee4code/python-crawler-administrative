import config
import pymysql.cursors


class Database:
    def execute(self, sql):
        connection = self._connect()
        insert_id = None
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

            connection.commit()
            insert_id = cursor.lastrowid

        finally:
            connection.close()

        return insert_id

    def query(self, sql):
        result = []
        try:
            connection = self._connect()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()

        finally:
            connection.close()

        return result


    def _connect(self):
        return pymysql.connect(host=config.mysql_host, user=config.mysql_user, passwd=config.mysql_pass, db=config.mysql_base, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
