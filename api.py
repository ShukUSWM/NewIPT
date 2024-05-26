from flask import Flask, jsonify, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)

# Required configurations
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "1234"
app.config["MYSQL_DB"] = "mydb"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/mydb", methods=["GET"])
def get_actors():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM staff"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return make_response(jsonify(data), 200)

if __name__ == "__main__":
    app.run(debug=True)
