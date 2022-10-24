from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    a = 0
    for i in range(50000):
        a += i
    return f'{a}'

if __name__ == '__main__':
    app.run()
