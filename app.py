from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="website_db"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    cursor = db.cursor()

    query = """
    INSERT INTO contacts(name, email, message)
    VALUES(%s, %s, %s)
    """

    cursor.execute(query, (name, email, message))

    db.commit()

    cursor.close()

    return "Message Sent Successfully!"

if __name__ == '__main__':
    app.run(debug=True)