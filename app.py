import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = 0
    for i in range(80000):
        a += i
    return os.getenv("DOT")

if __name__ == '__main__':
    app.run()
