from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Flask!'

@app.route("/home")
def home():
    return "홈페이지"

if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)