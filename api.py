from flask import Flask, jsonify, make_response, request
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

@app.route("/staff", methods = ["POST"])
def add_staff():
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    cur.execute(
        """INSERT INTO staff (first_name, last_name) VALUE (%s, %s)""", (first_name, last_name),
    )
    mysql.connection.commit()
    print("rows(s) affected :{}".format(cur.rowcount))
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "staff added succesfully", "rows_affected": rows_affected}), 201)



@app.route("/staff/<int:id>", methods=["PUT"])
def update_staff(id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    first_name = info["first_name"]
    last_name = info["last_name"]
    cur.execute(
        """ UPDATE staff SET first_name = %s, last_name = %s WHERE staff_id = %s """,
        (first_name, last_name, id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(jsonify({"message": "staff updated successfully", "rows_affected": rows_affected}), 200)


@app.route("/staff/<int:id>", methods=["DELETE"])
def delete_actor(id):
    cur = mysql.connection.cursor()
    cur.execute(""" DELETE FROM staff where staff_id = %s """, (id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "staff deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )



@app.route("/staff/format", methods=["GET"])
def get_params():
    fmt = request.args.get('id')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format":fmt, "foo":foo}),200)




if __name__ == "__main__":
    app.run(debug=True)
