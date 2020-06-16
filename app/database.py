import pymysql
import os

class Database():
    def __init__(self):
        self.db= pymysql.connect(
            host="172.23.0.2",
            user='root',
            password='1234',
            db='wordpress',
            charset='utf8'
            )
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
 
    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self, query, args={}):
        self.cursor.execute(query, args)
 
    def commit(self):
        self.db.commit()
