import config
import pymysql.cursors


class Database:
    def __init__(self):
        print('init database...')

    def execute(self, sql):
        connection = pymysql.connect(host=config.mysql_host, user=config.mysql_user, passwd=config.mysql_pass, db=config.mysql_base, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        insert_id = None
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql)

            connection.commit()
            insert_id = cursor.lastrowid

        finally:
            connection.close()

        return insert_id
