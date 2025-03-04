from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to register a new user
@app.route("/register")
def register():
    return render_template("register.html")

# Route to add a new user to the database
@app.route("/adduser", methods=['POST'])
def adduser():
    if request.method == 'POST':
        try:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            username = request.form['username']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user (firstname, lastname, email, username) VALUES (?, ?, ?, ?)",
                            (firstname, lastname, email, username))
                con.commit()
                msg = "User successfully registered"
        except:
            con.rollback()
            msg = "Error in registration"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to display all users
@app.route('/users')
def users():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    con.close()
    return render_template("users.html", rows=rows)

# Route to add a new pin
@app.route("/addpin", methods=['POST'])
def addpin():
    if request.method == 'POST':
        try:
            image = request.form['image']
            title = request.form['title']
            description = request.form['description']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO pins (image, title, description) VALUES (?, ?, ?)",
                            (image, title, description))
                con.commit()
                msg = "Pin successfully added"
        except:
            con.rollback()
            msg = "Error in adding pin"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to create a board
@app.route("/addboard", methods=['POST'])
def addboard():
    if request.method == 'POST':
        try:
            cover_image = request.form['cover_image']
            title = request.form['title']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO board (cover_image, title) VALUES (?, ?)",
                            (cover_image, title))
                con.commit()
                msg = "Board successfully created"
        except:
            con.rollback()
            msg = "Error in creating board"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to add a pin to a board
@app.route("/addpinboard", methods=['POST'])
def addpinboard():
    if request.method == 'POST':
        try:
            board_id = request.form['board_id']
            pin_id = request.form['pin_id']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO boardPins (board_id, pin_id) VALUES (?, ?)",
                            (board_id, pin_id))
                con.commit()
                msg = "Pin successfully added to board"
        except:
            con.rollback()
            msg = "Error in adding pin to board"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

# Route to add a comment to a pin
@app.route("/addcomment", methods=['POST'])
def addcomment():
    if request.method == 'POST':
        try:
            text = request.form['text']
            pin_id = request.form['pin_id']
            user_id = request.form['user_id']

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO comments (text, pin_id, user_id) VALUES (?, ?, ?)",
                            (text, pin_id, user_id))
                con.commit()
                msg = "Comment successfully added"
        except:
            con.rollback()
            msg = "Error in adding comment"
        finally:
            con.close()
            return render_template('result.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)