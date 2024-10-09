from flask import Flask
from striprtf.striprtf import rtf_to_text

application = Flask(__name__)

@application.route("/")
def hello():
    rtf = "some rtf encoded string"
    text = rtf_to_text(rtf)
    print(text)
    return "strip rtf package test!"

if __name__ == "__main__":
    application.run()
