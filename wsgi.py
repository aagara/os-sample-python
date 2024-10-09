from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "strip rtf package test!"

if __name__ == "__main__":
    application.run()
