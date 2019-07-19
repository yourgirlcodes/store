
from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql
import database_sql

@get("/admin")
def admin_portal():
	return template("pages/admin.html")



@get("/")
def index():
    return template("index.html")


@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


@post("/category")
def category_to_database():
    requested_category = request.POST.get("name")
    result = database_sql.insert_category(requested_category)
    return json.dumps(result)


@get("/categories")
def send_categories():
    result = database_sql.return_categories()
    return json.dumps(result)


run(host='0.0.0.0', port=argv[1])
