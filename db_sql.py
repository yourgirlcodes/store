<<<<<<< HEAD
import pymysql


connection = pymysql.connect(
        host="localhost",
        user="root",
        password="CoeZohen!12345",       # change this per person
        db="store",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )


def search_category(kitty_name):
    with connection.cursor() as cursor:
        # cat_id = db["last_category_id"] + 1
        sql = f"insert into categories values({cat_id}, '{kitty_name}')"
        try:
            cursor.execute(sql)
            db["last_category_id"] = cursor.lastrowid
            connection.commit()
            result = {
                "STATUS": "SUCCESS",
                "CAT_ID": cat_id,
                "CAT_NAME": cat_name
            }
            return result
        except:
            return {
                "STATUS": "ERROR",
                "MSG": "Problem with database"
            }


def return_categories():
    with connection.cursor() as cursor:
        sql = "select * from categories"
        try:
            cursor.execute(sql)
            categories = cursor.fetchall()
            return {
                "STATUS": "SUCCESS",
                "CATEGORIES": categories
            }
        except:
            return {
                "STATUS": "ERROR",
                "MSG": "Cannot get the categories from the database"
            }
=======
from pymysql import connect, cursors

connection = connect(host='localhost',
                     user='root',
                     password='root',
                     db='store',
                     charset='utf8',
                     cursorclass=cursors.DictCursor)


def find_categories():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM categories"
        try:
            cursor.execute(sql)
            categories = cursor.fetchall()
            result = {
                "STATUS": "SUCCESS",
                "CATEGORIES": categories
            }
            return result
        except:
            result = {
                "STATUS": "ERROR",
                "MSG": "internal error"
            }
            return result


def insert_category(requested_category):
    with connection.cursor() as cursor:
        catId = cursor.lastrowid + 1
        sql = "INSERT into categories values({id}, {requested_category})".format(catId, requested_category)
        try:
            cursor.execute(sql)
            connect.commit()
            result = {
                "STATUS": "SUCCESS",
                "catName": requested_category,
                "catId": catId
            }
            return result
        except:
            result = {
                "STATUS": "ERROR",
                "MSG": "internal error"
            }
            return result
>>>>>>> 0de2ab611beff16aab4834b94427c5d8c6c60d02
