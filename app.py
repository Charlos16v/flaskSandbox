from flask import Flask
import src.db as db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# test to insert data to the data base
@app.route("/test")
def test():
    db.user_collection.insert_one({"name": "Test"})
    return "Connected to the data base!"


if __name__ == '__main__':
    app.run()
