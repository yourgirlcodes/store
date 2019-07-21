from pymysql import connect, cursors
from bottle import request

connection = connect(host='localhost',
                     user='root',
                     password='CoeZohen!12345',
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


def insert_category():
    with connection.cursor() as cursor:
        try:
            requested_category = request.POST.get("name")
            sql = "INSERT into categories(name) values('{}');".format(requested_category)
            cursor.execute(sql)
            cat_id = cursor.lastrowid
            result = {
                "STATUS": "SUCCESS",
                "catName": requested_category,
                "catId": cat_id,
                "MSG": "Category created successfully"
            }
            return result
        except Exception as e:
            result = {
                "STATUS": "ERROR",
                "MSG": str(e)
            }
            return result
