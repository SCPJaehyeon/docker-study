from database import Database
import json
import utils

class UserTable(Database):
    def random(self, n):
        sql = "INSERT INTO wp_random(random) values({});".format(n)
        print("INPUT > {}".format(sql))
        result = None
        self.cursor.execute(sql)
        self.db.commit()
        return result

    def user(self, id):
        sql =  "SELECT user_login FROM wp_users "
        sql += "WHERE id={};".format(id)
        print("INPUT > {}".format(sql))
        result = ()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        result = {} if len(result) == 0 else result[0]
        return result

    def users(self, page=0, itemsInPage=10):
        page = page * itemsInPage;
        sql =  "SELECT user_login FROM wp_users "
        sql += "LIMIT {page},{itemsInPage};".format(page=page,itemsInPage=itemsInPage)
        print("INPUT > {}".format(sql))
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def insert(self, j):
        sql = "INSERT INTO wp_users(id, user_login, user_pass, user_nicename, user_email, user_status, display_name) "
        sql = sql + "values('{id}','{user_login}',MD5('{user_pass}'), '{user_nicename}', '{user_email}', 0, '{display_name}');".format(
            id = j.get("id",""),
            user_login = utils.addslashes(j.get("user_login","")),
            user_pass = utils.addslashes(j.get("user_pass","")),
            user_nicename = utils.addslashes(j.get("user_nicename","")),
            user_email = utils.addslashes(j.get("user_email","")),
            display_name = utils.addslashes(j.get("display_name","")),
            )
        print("INPUT > {}".format(sql))
        result = None
        self.cursor.execute(sql)
        self.db.commit()
        return result

    def update(self, id, j):
        id = j.get("id","")
        user_login = j.get("user_login","")
        sql = "UPDATE wp_user SET "
        if len(id) > 0:
            sql += " id = '{}', ".format(id)
        if len(user_login) > 0:
            sql += " user_login = '{}' ".format(url)
        sql += "WHERE id = {} ".format(id)
        print("INPUT > {}".format(sql))        
        result = None
        self.cursor.execute(sql)
        self.db.commit()
        return result

    def delete(self, id):
        sql =  "DELETE FROM wp_users WHERE id = '{}';".format(id)
        print("INPUT > {}".format(sql))
        result = None
        self.cursor.execute(sql)
        self.db.commit()
        return result

