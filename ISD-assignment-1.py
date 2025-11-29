import os
import sqlite3
from flask import Flask, request

# Start the flask project
app = Flask(__name__)

DB_PASSWORD = "123456"  

def get_connection():
    return sqlite3.connect("users.db")

@app.route("/ping")
def ping():
    host = request.args.get("host")

    # Running user input directly in shell
    return os.popen(f"ping -c 1 {host}").read()

@app.route("/read")
def read_file():
    filename = request.args.get("file")

    with open(filename, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run()
