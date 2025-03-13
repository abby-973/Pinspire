from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import urllib.parse

app = Flask(__name__, template_folder='templates', static_folder='static')

DATABASE = "pinspire.db"

# Ensure templates directory exists
os.makedirs("templates", exist_ok=True)
os.makedirs("static", exist_ok=True)

# Home Page route
@app.route("/")
def home():
    return render_template("home.html")

# Route to register a new user
@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/adduser", methods=['POST'])
def adduser():
    try:
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        username = request.form['username']

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Users (FName, LName, Email, Username) VALUES (?, ?, ?, ?)",
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
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    con.close()
    return render_template("users.html", rows=rows)

# Route to add a new pin
@app.route("/addpin")
def addpin():
    return render_template("addpin.html")

@app.route("/insertpin", methods=['POST'])
def insertpin():
    try:
        image = request.form['image']
        title = request.form['title']
        description = request.form['description']

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Pins (ImgUrl, Title, Description) VALUES (?, ?, ?)",
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
@app.route("/addboard")
def addboard():
    return render_template("addboard.html")

@app.route("/insertboard", methods=['POST'])
def insertboard():
    try:
        image = urllib.parse.quote(request.form['cover_image'])
        title = request.form['title']
        user_id = request.form['user_id']

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Boards (CoverImgUrl, Title, UserId) VALUES (?, ?, ?)",
                        (image, title, user_id))
            con.commit()
            msg = "Board successfully added"
    except:
        con.rollback()
        msg = "Error in adding board"
    finally:
        con.close()
        return render_template('result.html', msg=msg)

# Route to add a comment
@app.route("/addcomment", methods=['POST'])
def addcomment():
    try:
        user_id = request.form['user_id']
        pin_id = request.form['pin_id']
        comment_text = request.form['comment_text']

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Comments (UserId, PinId, Text) VALUES (?, ?, ?)",
                        (user_id, pin_id, comment_text))
            con.commit()
            msg = "Comment successfully added"
    except:
        con.rollback()
        msg = "Error in adding comment"
    finally:
        con.close()
        return render_template('result.html', msg=msg)

# Route to associate a pin with a board
@app.route("/addboardpin", methods=['POST'])
def addboardpin():
    try:
        board_id = request.form['board_id']
        pin_id = request.form['pin_id']

        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("INSERT INTO BoardPins (BoardId, PinId) VALUES (?, ?)",
                        (board_id, pin_id))
            con.commit()
            msg = "Pin successfully added to board"
    except:
        con.rollback()
        msg = "Error in adding pin to board"
    finally:
        con.close()
        return render_template('result.html', msg=msg)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
