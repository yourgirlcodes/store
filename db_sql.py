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