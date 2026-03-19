from flask import Flask

app = Flask(__name__)
@app.route('/user/<name>')
def user(name):
    return f"Hello {name}"

@app.route("/user2/<nickname>")
def user2(nickname):
    return f"안녕하세요, {nickname}님. 소환사에 협곡에 오신것을 환영합니다."

if __name__ == '__main__':
     app.run(debug=True)