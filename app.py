from flask import Flask
import socket


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello from FLASK. My Hostname is: %s \n" % (socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
