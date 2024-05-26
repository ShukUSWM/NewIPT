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

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/staff", methods=["GET"])
def get_actors():
    data = data_fetch("""select * from staff""")
    return make_response(jsonify(data), 200)

@app.route("/staff/<int:id>", methods=["GET"])
def get_actor_by_id(id):
    data = data_fetch("""SELECT * FROM staff where staff_id = {}""".format(id))
    return make_response(jsonify(data), 200)

@app.route("/staff/<int:id>/job_title", methods=["GET"])
def get_movies_by_actor(id):
    data = data_fetch(
        """
        SELECT staff.first_name, staff.contact_details, staff.job_title, amount_allocated  
        FROM budget 
        INNER JOIN staff ON budget.budget_id = staff.staff_id
        INNER JOIN student ON staff.staff_id = student.student_id  
        WHERE budget.budget_id = {}
    """.format(
            id
        )
    )
    return make_response(
        jsonify({"staff_id": id, "count": len(data), "job_title": data}), 200
    )


if __name__ == "__main__":
    app.run(debug=True)
