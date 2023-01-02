from flask import Flask, render_template, request,redirect
import sqlite3
# from cs50 import SQL

db = sqlite3.connect('C:/Users/hyang/PycharmProjects/freshIMs/database.db', check_same_thread=False, isolation_level=None)
# db = SQL("sqlite:///froshims.db")
cur = db.cursor()
# cur.execute("CREATE TABLE registrants (id INTEGER, name TEXT NOT NULL, sport TEXT NOT NULL, PRIMARY KEY(id));")
# cur.execute("INSERT INTO registrants (name, sport) VALUES (?, ?)", ("TESTTEST11", "Ultimate Frisbee"))
# rows = cur.fetchall()
# for row in rows:
#     print(row)
# cur.execute('select * from registrants order by name desc')

# db.close()
app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/deregister", methods=["POST"])
def deregister():
    ID = request.form.get("number")
    print(ID)
    if ID:
        cur.execute("delete from registrants where id = ?", ID)
    return redirect('/registrants')



@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    print(name, sport)
    if not name:
        print(name)
        return render_template("failure.html")
    # if sport in SPORTS:
    #     print(sport)
    #     return render_template("failure.html")
    # REGISTRANTS[name] = sport
    cur.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", (name, sport))

    return redirect("/registrants")
    # return render_template("success.html")


@app.route("/registrants")
def registrants():
    db = sqlite3.connect('C:/Users/hyang/PycharmProjects/freshIMs/database.db', check_same_thread=False,
                         isolation_level=None)
    # db = SQL("sqlite:///froshims.db")
    cur = db.cursor()
    DATA = cur.execute("SELECT * FROM registrants")
    # print([registrant[2] for registrant in DATA])
    # db.close()
    return render_template("registrants.html", register_data = DATA)


app.run(debug=True)