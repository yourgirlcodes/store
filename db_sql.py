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
