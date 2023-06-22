import sqlite3


def get_all_data():
    try:
        db = sqlite3.connect("app.db")
        print("connected successfully")
        cr = db.cursor()
        cr.execute("select * from users")
        # results = cr.fetchone()
        results = cr.fetchall()
        print(results)
        print(f"database has {len(results)} rows")

    except sqlite3.Error as er:
        print(f"error reading data{er}")

    finally:
        if (db):
            db.close()
            print("db connection closed")


get_all_data()
