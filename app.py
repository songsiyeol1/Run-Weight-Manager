from flask import Flask, render_template,request, redirect
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("fitness.db")
    cur= conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        weight REAL,  
        run_km REAL,
        run_time INTEGER
    )
    """)

    conn.commit()
    conn.close()

@app.route("/",methods = ["GET","POST"])
# get은 웹페이지를 보이게 하는 것
# Post는 입력값을 받아 DB에 저장하는 역할을 한다.



def home():
    if request.method == "POST":
        date = request.form["date"]
        weight = request.form["weight"]
        run_km = request.form["run_km"]
        run_time = request.form["run_time"]

        conn = sqlite3.connect("fitness.db")
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO records (date, weight, run_km, run_time)
        VALUES (?, ?, ?, ?)
        """, (date, weight, run_km, run_time))

        conn.commit()
        conn.close()

        return redirect("/")
    
     # 조회 기능 추가
    conn = sqlite3.connect("fitness.db")
    cur = conn.cursor()

    cur.execute("SELECT id,date, weight, run_km, run_time FROM records")
    records = cur.fetchall()

    dates = []
    weights = []
    run_kms = []

    for row in records:
        dates.append(row[1])
        weights.append(float(row[2]))
        run_kms.append(float(row[3]))

    conn.close()


    return render_template("index.html",
                           records=records, 
                           dates=dates,
                           weights=weights,
                           run_kms=run_kms)


# 삭제 

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("fitness.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM records WHERE id = ?", (id,))

    conn.commit()

    conn.close()

    return redirect("/")



if __name__ == "__main__":
    init_db()
    app.run(debug=True)
