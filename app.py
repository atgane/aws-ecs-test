import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = 0
    for i in range(30000):
        a += i
    return os.getenv("DOT") + str(a)

if __name__ == '__main__':
    app.run()
