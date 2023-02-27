import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="service_db1",
                        user="postgres",
                        password="FirEfirE",
                        host="localhost",
                        port="5432")
cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username:
        return render_template('login.html', error="You must enter username.")

    if not password:
        return render_template('login.html', error="You must enter password")

    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = cursor.fetchall()

    if records:
        return render_template('account.html', full_name=records[0][1], login=records[0][2], password=records[0][3])
    return render_template('login.html', error="This user does not exist.")
